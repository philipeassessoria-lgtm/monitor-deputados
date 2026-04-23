"""
ranquear_engajamento.py
Ranqueia posts coletados e gera top_posts.json pronto para dashboard + WhatsApp.

Uso:
  python ranquear_engajamento.py --top 20
  python ranquear_engajamento.py --top 50 --por-tipo   # top por federal e estadual
"""

import argparse
import json
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="posts_24h.json")
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--por-tipo", action="store_true")
    ap.add_argument("--normalizar", action="store_true",
                    help="Ranqueia pela razao engajamento/followers (justo com pequenos)")
    args = ap.parse_args()

    posts = json.loads(Path(args.input).read_text(encoding="utf-8"))

    if args.normalizar:
        for p in posts:
            f = max(p.get("followers", 1) or 1, 1)
            p["score"] = p["engajamento"] / f
    else:
        for p in posts:
            p["score"] = p["engajamento"]

    if args.por_tipo:
        saida = {}
        for tipo in ("federal", "estadual"):
            filtrados = [p for p in posts if p["tipo"] == tipo]
            filtrados.sort(key=lambda x: x["score"], reverse=True)
            saida[tipo] = filtrados[:args.top]
        out = saida
    else:
        posts.sort(key=lambda x: x["score"], reverse=True)
        out = posts[:args.top]

    Path("top_posts.json").write_text(json.dumps(out, ensure_ascii=False, indent=2),
                                      encoding="utf-8")
    print(f"Top {args.top} salvo em top_posts.json")


if __name__ == "__main__":
    main()
