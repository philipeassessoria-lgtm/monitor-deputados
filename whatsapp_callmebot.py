"""
whatsapp_callmebot.py
Envia notificacoes WhatsApp GRATIS via CallMeBot.

COMO ATIVAR (so uma vez, ~2 min):
  1. Adicione +34 644 51 95 23 nos seus contatos (nome: CallMeBot).
  2. Envie pelo WhatsApp a mensagem: "I allow callmebot to send me messages"
  3. Em alguns minutos voce recebe de volta: "API Activated for your phone number.
     Your APIKEY is 123456"
  4. Salve esse APIKEY como env var CALLMEBOT_APIKEY.
  5. Salve seu numero com DDI como env var CALLMEBOT_PHONE (ex: 5583991424780).

Uso:
  python whatsapp_callmebot.py --teste
  python whatsapp_callmebot.py --digest top_posts.json

Limites (versao gratis):
  - ~1 mensagem a cada 10s
  - ~300 caracteres por mensagem (quebrar se maior)
  - Sem midia (so texto + links)
"""

import argparse
import json
import os
import time
from pathlib import Path
from urllib.parse import quote

import requests


def enviar(texto: str, apikey: str = None, phone: str = None):
    apikey = apikey or os.getenv("CALLMEBOT_APIKEY")
    phone = phone or os.getenv("CALLMEBOT_PHONE", "5583991424780")
    if not apikey:
        raise RuntimeError("CALLMEBOT_APIKEY nao definido.")
    url = "https://api.callmebot.com/whatsapp.php"
    params = {"phone": phone, "text": texto, "apikey": apikey}
    r = requests.get(url, params=params, timeout=30)
    if r.status_code != 200 or "Message queued" not in r.text and "Message Sent" not in r.text:
        print(f"Aviso: resposta {r.status_code}: {r.text[:200]}")
    else:
        print("OK: mensagem enviada")


def montar_digest(posts, limite=10):
    linhas = [" TOP POSTS DE ONTEM ", ""]
    for i, p in enumerate(posts[:limite], 1):
        eng = f"{p['likes']:,}❤ {p['comments']:,}💬".replace(",", ".")
        linhas.append(f"{i}. {p['deputado']} ({p['uf']})")
        linhas.append(f"   {eng}")
        linhas.append(f"   {p['url']}")
        linhas.append("")
    return "\n".join(linhas)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--teste", action="store_true", help="Envia mensagem de teste")
    ap.add_argument("--digest", help="Envia digest a partir de top_posts.json")
    ap.add_argument("--limite", type=int, default=10)
    args = ap.parse_args()

    if args.teste:
        enviar("Teste do monitor de deputados - configurado com sucesso!")
        return

    if args.digest:
        data = json.loads(Path(args.digest).read_text(encoding="utf-8"))
        if isinstance(data, dict):
            posts = data.get("federal", []) + data.get("estadual", [])
        else:
            posts = data
        msg = montar_digest(posts, limite=args.limite)
        # CallMeBot limita tamanho, entao enviar em blocos de 2 posts
        linhas = msg.split("\n")
        bloco = []
        for linha in linhas:
            bloco.append(linha)
            if len("\n".join(bloco)) > 300:
                enviar("\n".join(bloco[:-1]))
                bloco = [bloco[-1]]
                time.sleep(12)
        if bloco:
            enviar("\n".join(bloco))


if __name__ == "__main__":
    main()
