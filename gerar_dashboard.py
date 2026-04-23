"""
gerar_dashboard.py
Gera dashboard HTML estatico com os top posts do dia (thumbnails, legendas,
engajamento). Ideal para inspiracao visual de planejamento.

Saida: docs/index.html (GitHub Pages le a pasta docs/)

Uso:
  python gerar_dashboard.py --input top_posts.json
"""

import argparse
import html
import json
from datetime import datetime
from pathlib import Path

TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Monitor Deputados - {data}</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        background: #fafafa; color: #262626; }}
header {{ background: linear-gradient(135deg,#833AB4,#FD1D1D,#FCB045);
          color: white; padding: 30px 20px; text-align: center; }}
header h1 {{ font-size: 28px; margin-bottom: 5px; }}
header p {{ opacity: 0.9; }}
.container {{ max-width: 1200px; margin: 20px auto; padding: 0 20px; }}
.filtros {{ display:flex; gap:10px; margin-bottom:20px; flex-wrap:wrap; }}
.filtro {{ padding:8px 16px; background:white; border:1px solid #dbdbdb;
           border-radius:20px; cursor:pointer; font-size:14px; }}
.filtro.ativo {{ background:#262626; color:white; border-color:#262626; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr));
         gap:20px; }}
.card {{ background:white; border-radius:12px; overflow:hidden;
         box-shadow:0 1px 3px rgba(0,0,0,0.1); transition:transform 0.2s; }}
.card:hover {{ transform:translateY(-4px); box-shadow:0 4px 12px rgba(0,0,0,0.15); }}
.card img {{ width:100%; aspect-ratio:1/1; object-fit:cover; background:#efefef; }}
.card-body {{ padding:14px; }}
.deputado {{ font-weight:600; margin-bottom:4px; }}
.uf {{ font-size:12px; color:#8e8e8e; text-transform:uppercase; }}
.stats {{ display:flex; gap:15px; margin:10px 0; font-size:14px; color:#262626; }}
.stats span {{ font-weight:600; }}
.caption {{ font-size:13px; color:#555; max-height:60px; overflow:hidden;
            line-height:1.4; margin-bottom:10px; }}
.link {{ display:inline-block; background:#0095f6; color:white;
         padding:8px 16px; border-radius:6px; text-decoration:none; font-size:13px; }}
.link:hover {{ background:#0081d6; }}
footer {{ text-align:center; padding:30px; color:#8e8e8e; font-size:13px; }}
.badge {{ display:inline-block; padding:2px 8px; border-radius:10px;
          font-size:11px; font-weight:600; margin-left:6px; }}
.badge.federal {{ background:#e3f2fd; color:#1565c0; }}
.badge.estadual {{ background:#f3e5f5; color:#6a1b9a; }}
</style>
</head>
<body>
<header>
  <h1>🔥 Top Posts Deputados</h1>
  <p>{data} - {total} posts das ultimas 24h</p>
</header>
<div class="container">
  <div class="filtros">
    <div class="filtro ativo" data-filter="all">Todos</div>
    <div class="filtro" data-filter="federal">Federais</div>
    <div class="filtro" data-filter="estadual">Estaduais</div>
  </div>
  <div class="grid">
    {cards}
  </div>
</div>
<footer>Atualizado automaticamente - inspiracao para planejamento de conteudo</footer>
<script>
document.querySelectorAll('.filtro').forEach(f => {{
  f.addEventListener('click', () => {{
    document.querySelectorAll('.filtro').forEach(x => x.classList.remove('ativo'));
    f.classList.add('ativo');
    const filter = f.dataset.filter;
    document.querySelectorAll('.card').forEach(c => {{
      c.style.display = (filter==='all' || c.dataset.tipo===filter) ? '' : 'none';
    }});
  }});
}});
</script>
</body>
</html>"""


def gerar_card(p):
    return f"""
<div class="card" data-tipo="{p['tipo']}">
  <img src="{html.escape(p.get('thumbnail_url',''))}" loading="lazy" alt="">
  <div class="card-body">
    <div class="deputado">{html.escape(p['deputado'])}
      <span class="badge {p['tipo']}">{p['tipo']} {p['uf']}</span>
    </div>
    <div class="stats">
      <span>❤ {p['likes']:,}</span>
      <span>💬 {p['comments']:,}</span>
    </div>
    <div class="caption">{html.escape(p.get('caption','')[:200])}</div>
    <a class="link" href="{html.escape(p['url'])}" target="_blank">Ver no Instagram →</a>
  </div>
</div>""".replace(",", ".")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="top_posts.json")
    ap.add_argument("--out", default="docs/index.html")
    args = ap.parse_args()

    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    if isinstance(data, dict):
        posts = data.get("federal", []) + data.get("estadual", [])
    else:
        posts = data
    cards = "\n".join(gerar_card(p) for p in posts)
    html_out = TEMPLATE.format(
        data=datetime.now().strftime("%d/%m/%Y"),
        total=len(posts),
        cards=cards,
    )
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(html_out, encoding="utf-8")
    print(f"Dashboard gerado: {args.out}")


if __name__ == "__main__":
    main()
