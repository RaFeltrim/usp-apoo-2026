#!/usr/bin/env python3
"""Auditoria cruzada em 5 níveis para os artefatos UML/PlantUML do Projeto Final (Tópico 7)."""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "Tópico 7 - Projeto Final" / "Entregas" / "Projeto Final - APOO assistido por LLM"
PUML_DIR = BASE / "Desenvolvimento" / "PUML"
SEQ_DIR = PUML_DIR / "sequencias"
ZIP_DIAG = BASE / "Pacote-ZIP" / "Diagramas"


def resolve_plantuml_cmd() -> list[str]:
    env_jar = os.environ.get("PLANTUML_JAR", "").strip()
    if env_jar:
        jar_path = Path(env_jar)
        if not jar_path.is_file():
            raise FileNotFoundError(f"PLANTUML_JAR configurado nao encontrado: {jar_path}")
        if not shutil.which("java"):
            raise RuntimeError("Java nao encontrado no PATH para executar PLANTUML_JAR.")
        return ["java", "-jar", str(jar_path)]

    plantuml_bin = shutil.which("plantuml")
    if plantuml_bin:
        return [plantuml_bin]

    usr_jar = Path("/usr/share/plantuml/plantuml.jar")
    if usr_jar.is_file():
        if not shutil.which("java"):
            raise RuntimeError("Java nao encontrado no PATH para executar /usr/share/plantuml/plantuml.jar.")
        return ["java", "-jar", str(usr_jar)]

    raise RuntimeError(
        "PlantUML nao encontrado. Instale o binario 'plantuml' ou defina a variavel de ambiente PLANTUML_JAR."
    )


def check_level_1_syntactic() -> tuple[int, int, str]:
    pumls = sorted(PUML_DIR.glob("*.puml")) + sorted(SEQ_DIR.glob("*.puml"))
    base_cmd = resolve_plantuml_cmd()
    cmd = [*base_cmd, "-checkonly", "-charset", "UTF-8", *(str(p) for p in pumls)]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return len(pumls), res.returncode, res.stdout + res.stderr


def parse_classes(puml_path: Path) -> dict[str, dict]:
    text = puml_path.read_text(encoding="utf-8")
    classes: dict[str, dict] = {}
    current = None
    for line in text.splitlines():
        m_cls = re.match(r"^\s*class\s+(\w+)\s*\{", line)
        if m_cls:
            current = m_cls.group(1)
            classes[current] = {"attrs": [], "methods": {}}
            continue
        if current and re.match(r"^\s*\}", line):
            current = None
            continue
        if current:
            m_meth = re.match(r"^\s*[+\-#~]\s*(\w+)\(([^)]*)\)", line)
            if m_meth:
                mname = m_meth.group(1)
                params_str = m_meth.group(2).strip()
                arity = 0 if not params_str else len([p for p in params_str.split(",") if p.strip()])
                classes[current]["methods"][mname] = arity
            else:
                m_attr = re.match(r"^\s*[+\-#~]\s*(\w+)\s*:", line)
                if m_attr:
                    classes[current]["attrs"].append(m_attr.group(1))
    return classes


def check_level_2_structural(classes: dict[str, dict]) -> tuple[int, int, list[str]]:
    seq_files = sorted(p for p in SEQ_DIR.glob("seq-UC*.puml") if "-v1" not in p.name)
    divergences: list[str] = []
    total_calls = 0

    for sf in seq_files:
        text = sf.read_text(encoding="utf-8")
        participants: dict[str, str] = {}
        actors: set[str] = set()
        for line in text.splitlines():
            m_act = re.match(r'^\s*actor\s+(?:"[^"]+"\s+as\s+)?(\w+)', line)
            if m_act:
                actors.add(m_act.group(1))
            m_part = re.match(r'^\s*participant\s+"[^"]*\s*:\s*(\w+)"\s+as\s+(\w+)', line)
            if m_part:
                cls_name, alias = m_part.group(1), m_part.group(2)
                participants[alias] = cls_name
                if cls_name not in classes:
                    divergences.append(f"{sf.name}: participante '{alias}' referencia classe inexistente '{cls_name}'")

        for idx, line in enumerate(text.splitlines(), 1):
            m_call = re.match(r"^\s*(?:\[|\w+)\s*-+>\s*(\w+)\s*:\s*(\w+)\(([^)]*)\)", line)
            if m_call:
                target, method, args = m_call.group(1), m_call.group(2), m_call.group(3).strip()
                if target in actors:
                    continue
                total_calls += 1
                if target not in participants:
                    divergences.append(f"{sf.name}:{idx}: alvo '{target}' nao declarado como participant")
                    continue
                cls_name = participants[target]
                cls_info = classes.get(cls_name)
                if not cls_info:
                    continue
                if method not in cls_info["methods"]:
                    divergences.append(f"{sf.name}:{idx}: metodo '{cls_name}.{method}()' ausente em 04-classes-completo-final.puml")
                    continue
                call_arity = 0 if not args else len([a for a in args.split(",") if a.strip()])
                expected_arity = cls_info["methods"][method]
                if call_arity != expected_arity:
                    divergences.append(
                        f"{sf.name}:{idx}: aridade divergente em '{cls_name}.{method}': chamada={call_arity}, classe={expected_arity}"
                    )
    return len(seq_files), total_calls, divergences


def check_level_3_architectural() -> tuple[int, bool]:
    comp_text = (PUML_DIR / "02-componentes-final.puml").read_text(encoding="utf-8")
    comps = re.findall(r'component\s+"([^"]+)"\s+as\s+(\w+)', comp_text)
    has_ext_pag = "PlataformaPagamento" in comp_text
    has_ext_not = "ServicoNotificacoes" in comp_text
    return len(comps), has_ext_pag and has_ext_not


def check_level_4_behavioral() -> tuple[int, list[str]]:
    seq_files = sorted(p for p in SEQ_DIR.glob("seq-UC*.puml") if "-v1" not in p.name)
    issues: list[str] = []
    ref_uc03 = False
    ref_uc09 = False
    gate_uc04 = False
    for sf in seq_files:
        lines = sf.read_text(encoding="utf-8").splitlines()
        for idx, line in enumerate(lines, 1):
            if re.match(r"^\s*(alt|opt|loop|else)\s+\[", line):
                issues.append(f"{sf.name}:{idx}: colchete manual em bloco de controle")
        full = "\n".join(lines)
        if "UC03" in sf.name and "ref over" in full and "UC04" in full:
            ref_uc03 = True
        if "UC09" in sf.name and "ref over" in full and "UC04" in full:
            ref_uc09 = True
        if "UC04" in sf.name and "[->" in full and "[<--" in full:
            gate_uc04 = True
    if not ref_uc03:
        issues.append("seq-UC03 nao referencia UC04 via ref")
    if not ref_uc09:
        issues.append("seq-UC09 nao referencia UC04 via ref")
    if not gate_uc04:
        issues.append("seq-UC04 nao possui gate ([-> / [<--)")
    return len(seq_files), issues


def check_level_5_traceability() -> tuple[int, int, list[str]]:
    hus_text = (BASE / "Desenvolvimento" / "Historias-de-Usuario.md").read_text(encoding="utf-8")
    hus = sorted(set(re.findall(r"\bHU\d{2}\b", hus_text)))

    uc_puml = (PUML_DIR / "01-casos-de-uso-final.puml").read_text(encoding="utf-8")
    ucs = sorted(set(re.findall(r"\bUC\d{2}\b", uc_puml)))

    desc_text = (BASE / "Desenvolvimento" / "Descricoes-Textuais-UC.md").read_text(encoding="utf-8")
    desc_ucs = sorted(set(re.findall(r"^### (UC\d{2})\b", desc_text, re.M)))
    desc_hus = sorted(set(re.findall(r"\bHU\d{2}\b", desc_text)))

    seq_ucs = sorted(set(re.findall(r"(UC\d{2})", " ".join(p.name for p in SEQ_DIR.glob("seq-UC*.puml") if "-v1" not in p.name))))
    png_ucs = sorted(set(re.findall(r"(UC\d{2})", " ".join(p.name for p in ZIP_DIAG.glob("05-seq-*.png")))))

    missing: list[str] = []
    if set(hus) - set(desc_hus):
        missing.append(f"HUs sem rastreabilidade em Descricoes-Textuais-UC: {sorted(set(hus) - set(desc_hus))}")
    if set(ucs) != set(desc_ucs):
        missing.append(f"Divergencia UCs PUML vs Descricoes: {set(ucs) ^ set(desc_ucs)}")
    if set(ucs) != set(seq_ucs):
        missing.append(f"Divergencia UCs PUML vs Sequencias: {set(ucs) ^ set(seq_ucs)}")
    if set(ucs) != set(png_ucs):
        missing.append(f"Divergencia UCs PUML vs PNGs ZIP: {set(ucs) ^ set(png_ucs)}")
    return len(hus), len(ucs), missing


def main() -> int:
    try:
        n_puml, rc, out = check_level_1_syntactic()
    except (FileNotFoundError, RuntimeError) as exc:
        print(f"ERRO DE CONFIGURACAO: {exc}")
        return 1

    print(f"[NIVEL 1 - SINTATICO] {n_puml} arquivos .puml | exit={rc}")
    if rc != 0:
        print(out)
        return 1

    classes = parse_classes(PUML_DIR / "04-classes-completo-final.puml")
    total_methods = sum(len(c["methods"]) for c in classes.values())
    n_seq, n_calls, divs = check_level_2_structural(classes)
    print(f"[NIVEL 2 - ESTRUTURAL] {len(classes)} classes, {total_methods} metodos | {n_seq} sequencias, {n_calls} chamadas | divergencias={len(divs)}")
    for d in divs:
        print("  DIVERGENCIA:", d)

    n_comp, ext_ok = check_level_3_architectural()
    print(f"[NIVEL 3 - ARQUITETURAL] {n_comp} componentes | externos OK={ext_ok}")

    n_beh, beh_issues = check_level_4_behavioral()
    print(f"[NIVEL 4 - COMPORTAMENTAL] {n_beh} sequencias | problemas={len(beh_issues)}")
    for i in beh_issues:
        print("  PROBLEMA:", i)

    n_hu, n_uc, trace_missing = check_level_5_traceability()
    print(f"[NIVEL 5 - RASTREABILIDADE] {n_hu} HUs -> {n_uc} UCs -> {n_comp} Componentes -> {len(classes)} Classes -> {n_seq} Sequencias | lacunas={len(trace_missing)}")
    for m in trace_missing:
        print("  LACUNA:", m)

    if rc != 0 or divs or not ext_ok or beh_issues or trace_missing:
        return 1
    print("RESULTADO FINAL: 5 NIVEIS APROVADOS COM 0 DIVERGENCIAS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
