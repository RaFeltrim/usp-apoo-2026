#!/usr/bin/env python3
"""Consistency check: every message received by a model/controller/view lifeline
in the Tópico 6 sequence diagrams must exist as an operation (same name and arity)
in the target class of the class diagram."""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE = ROOT / "Tópico 6 - Diagrama de Sequencias" / "Entregas" / "Atividade - Diagrama de Sequencias"


def main() -> int:
    cls_src = (BASE / "diagrama-classes-com-metodos.puml").read_text(encoding="utf-8")

    ops: dict[str, dict[str, int]] = {}
    for m in re.finditer(r"(?:class|interface)\s+(\w+)[^{]*\{(.*?)\n\s*\}", cls_src, re.S):
        name, body = m.group(1), m.group(2)
        ops[name] = {}
        for om in re.finditer(r"[+\-#~](\w+)\(([^)]*)\)", body):
            args = [a for a in om.group(2).split(",") if a.strip()]
            ops[name][om.group(1)] = len(args)

    errors: list[str] = []
    checked = 0
    for sd in ("diagrama-sequencia-comprar-passagem.puml", "diagrama-sequencia-notificar-usuario.puml"):
        src = (BASE / sd).read_text(encoding="utf-8")
        alias2cls: dict[str, str] = {}
        for pm in re.finditer(r'^(?:actor|boundary|control|entity|participant)\s+"([^"]+)"\s+as\s+(\w+)', src, re.M):
            cls = pm.group(1).split(":")[-1]
            alias2cls[pm.group(2)] = cls

        for line in src.splitlines():
            mm = re.match(r"\s*(\[|\w+)\s*(->>|->)\s*(\w+)\s*:\s*(?:<<create>>\s*)?(\w+)\(([^)]*)\)", line)
            if not mm:
                continue
            target, meth, args = mm.group(3), mm.group(4), mm.group(5)
            cls = alias2cls.get(target)
            if cls is None:  # actor targets (Passageiro) are not classes
                continue
            arity = len([a for a in args.split(",") if a.strip()])
            checked += 1
            if cls not in ops:
                errors.append(f"{sd}: classe '{cls}' ausente no diagrama de classes")
            elif meth not in ops[cls]:
                errors.append(f"{sd}: {cls}.{meth}() nao existe no diagrama de classes")
            elif ops[cls][meth] != arity:
                errors.append(f"{sd}: {cls}.{meth} aridade {arity} != {ops[cls][meth]}")

    print(f"Mensagens verificadas: {checked}")
    if errors:
        print("\n".join(errors))
        return 1

    print("OK - 0 divergencias")
    return 0


if __name__ == "__main__":
    sys.exit(main())
