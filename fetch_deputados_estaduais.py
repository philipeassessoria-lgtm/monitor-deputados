"""
fetch_deputados_estaduais.py
Gera um esqueleto de lista dos ~1.059 deputados estaduais do Brasil, agregando
fontes de cada Assembleia Legislativa (ALs) das 27 UFs.

IMPORTANTE:
  - Nao existe API unificada para deputados estaduais como existe na Camara.
  - Cada Assembleia publica dados de forma diferente (algumas tem API aberta,
    outras so HTML, algumas so PDF).
  - Este script organiza as fontes disponiveis e as estrategias recomendadas.

Fontes por UF (mapeadas):
  - AC: https://www.aleac.net.br/deputados/
  - AL: https://www.al.al.leg.br/deputados
  - AM: https://www.ale.am.gov.br/deputados/
  - AP: https://al.ap.leg.br/pagina.php?pg=exibir_depestaduais
  - BA: https://www.al.ba.leg.br/deputados
  - CE: https://www2.al.ce.gov.br/legislativo/deputados.htm
  - DF: https://www.cl.df.gov.br/deputados        (Camara Legislativa do DF)
  - ES: https://www.al.es.gov.br/Deputado
  - GO: https://portal.al.go.leg.br/deputados
  - MA: https://www.al.ma.leg.br/deputados
  - MG: https://www.almg.gov.br/deputados/
  - MS: https://www.al.ms.gov.br/Deputados
  - MT: https://www.al.mt.gov.br/deputados
  - PA: https://www.alepa.pa.gov.br/deputados
  - PB: https://www.al.pb.leg.br/deputado
  - PE: https://www.alepe.pe.gov.br/deputados/
  - PI: https://www.al.pi.leg.br/deputados
  - PR: https://www.assembleia.pr.leg.br/deputados
  - RJ: https://www.alerj.rj.gov.br/Visualizar/Deputados
  - RN: https://www.al.rn.leg.br/portal/deputados
  - RO: https://www.al.ro.leg.br/deputados
  - RR: https://www.al.rr.leg.br/deputados
  - RS: https://www.al.rs.gov.br/agenciaal/deputados
  - SC: https://www.alesc.sc.gov.br/deputados
  - SE: https://www.al.se.leg.br/deputados/
  - SP: https://www.al.sp.gov.br/alesp/deputados/
  - TO: https://www.al.to.leg.br/deputados

ESTRATEGIA RECOMENDADA (mais eficiente):
  1. Use o Apify actor "instagram-profile-scraper" ou equivalente para,
     A PARTIR DE UM NOME, encontrar o perfil verificado do politico.
  2. Ou use a API do Google Custom Search (site:instagram.com "nome do deputado")
     para achar o handle automaticamente.
  3. Mantenha uma tabela manual de correcoes para nomes ambiguos.

Este script demonstra o padrao para MG (ALMG, que tem API aberta) como prova
de conceito. As demais UFs precisam de scraper individual.
"""

import re
import requests
from openpyxl import Workbook

UFS = ["AC","AL","AM","AP","BA","CE","DF","ES","GO","MA","MG","MS","MT","PA",
       "PB","PE","PI","PR","RJ","RN","RO","RR","RS","SC","SE","SP","TO"]


# ---------- Exemplo funcional: Minas Gerais (ALMG tem servico aberto) ----------
def coletar_mg():
    """ALMG expoe um XML/JSON com a lista de deputados."""
    url = "https://dadosabertos.almg.gov.br/ws/deputados/em_exercicio?formato=json"
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.json().get("list_deputado", {}).get("deputado", [])


# ---------- Esqueleto para outras UFs ----------
def coletar_uf_generico(uf: str):
    """
    TEMPLATE. Cada UF precisa de um parser proprio. Retorne dicts com
    chaves: nome, partido, email, instagram (se conseguir extrair).
    """
    # TODO: implementar scraper especifico usando requests + BeautifulSoup
    return []


def descobrir_instagram(nome: str, partido: str, uf: str, api_key: str = None) -> str:
    """
    Usa Google Custom Search (ou SerpAPI) para achar o perfil de IG.
    Para usar de verdade, configure GOOGLE_CSE_ID e GOOGLE_CSE_KEY.
    """
    if not api_key:
        return ""
    q = f'site:instagram.com "{nome}" deputad {uf} {partido}'
    r = requests.get(
        "https://www.googleapis.com/customsearch/v1",
        params={"key": api_key, "cx": "SEU_CSE_ID", "q": q, "num": 3},
        timeout=15,
    )
    for item in r.json().get("items", []):
        m = re.search(r"instagram\.com/([A-Za-z0-9_.]+)", item["link"])
        if m:
            return "@" + m.group(1)
    return ""


def main():
    wb = Workbook()
    ws = wb.active
    ws.title = "Deputados Estaduais"
    ws.append(["UF", "Nome", "Partido", "Email", "Instagram", "Fonte"])

    # Exemplo real: MG
    try:
        for dep in coletar_mg():
            ws.append([
                "MG",
                dep.get("nome", ""),
                dep.get("partido", ""),
                dep.get("email", ""),
                "",  # preencher depois via descobrir_instagram()
                "ALMG API",
            ])
    except Exception as e:
        print("Falha MG:", e)

    # Demais UFs: criar um stub por enquanto
    for uf in UFS:
        if uf == "MG":
            continue
        ws.append([uf, "[pendente - implementar scraper]", "", "", "", ""])

    wb.save("deputados_estaduais_base.xlsx")
    print("Base parcial gerada. Continue implementando um scraper por UF.")


if __name__ == "__main__":
    main()
