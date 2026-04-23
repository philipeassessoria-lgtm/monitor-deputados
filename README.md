# Monitor de Instagram dos Deputados — Stack 100% Grátis

**Objetivo:** Ter uma biblioteca visual diária dos posts mais engajados dos 513 deputados federais + ~1.059 estaduais para inspirar planejamento de conteúdo.
**Custo:** R$ 0.
**Notificação:** WhatsApp +55 83 99142-4780.

---

## 🎁 O que você recebe neste pacote

```
outputs/
├── README.md                          ← você está aqui
├── arquitetura.md                     ← desenho completo do sistema grátis
├── deputados_template.xlsx            ← schema + 27 fontes + config
│
├── fetch_deputados_federais.py        ← coleta os 513 federais (API Câmara)
├── estaduais/
│   ├── config_ufs.py                  ← URLs + seletores das 27 ALs
│   ├── scraper_estaduais.py           ← scraper genérico para todas UFs
│   └── resolve_instagram.py           ← acha handle IG pelo nome
│
├── instagram/
│   ├── coletar_posts.py               ← Instaloader: posts das últimas 24h
│   └── ranquear_engajamento.py        ← top N por engajamento
│
├── notificacao/
│   ├── whatsapp_callmebot.py          ← WhatsApp grátis
│   └── gerar_dashboard.py             ← HTML estático c/ fotos pra inspiração
│
└── .github/workflows/
    └── daily.yml                      ← GitHub Actions cron diário
```

## 🚀 Passo a passo para subir tudo

### Pré-requisitos (tudo grátis)
- [ ] Conta GitHub (grátis)
- [ ] Ativar CallMeBot seguindo `notificacao/whatsapp_callmebot.py`
- [ ] Python 3.11+ local pra testar

### Setup (30 min)
```bash
# 1. Criar repositório privado no GitHub
# 2. Clonar e copiar estes arquivos pra dentro dele
# 3. Instalar dependências
pip install -r requirements.txt

# 4. Popular lista de deputados federais
python fetch_deputados_federais.py

# 5. Popular lista de estaduais (começa por MG que tem API)
python estaduais/scraper_estaduais.py --uf MG

# 6. Resolver handles de IG (usa busca do Google)
python estaduais/resolve_instagram.py

# 7. Testar coleta de posts (1 deputado só)
python instagram/coletar_posts.py --limite 1

# 8. Testar notificação WhatsApp
python notificacao/whatsapp_callmebot.py --teste

# 9. Configurar GitHub Secrets no repo:
#    CALLMEBOT_APIKEY, CALLMEBOT_PHONE, IG_USER, IG_PASS
# 10. Fazer push → GH Actions roda todo dia às 10h UTC (07h BRT)
```

### Acessando seu dashboard
Depois do 1º deploy, seu dashboard fica em:
```
https://SEU_USUARIO.github.io/NOME_DO_REPO/
```
Uma página por dia, com thumbnails, legendas, engajamento, deputado, link para o post original. Perfeito pra rolar no celular e se inspirar.

## ⚠️ Limites importantes da versão grátis

| Limite | Mitigação |
|---|---|
| Instagram rate-limits sem login | Criar conta "throwaway" e logar via Instaloader |
| ~1.500 perfis em 2h por run | Distribuir em 3 batches/dia ou rotacionar |
| Banimento do IP | Usar VPN no runner ou migrar para Oracle Cloud Free Tier |
| CallMeBot envia só 1 msg a cada ~10s | Enviar digest consolidado (top 10 em 1 msg) |

## 📍 Próximos passos
1. Rode localmente `fetch_deputados_federais.py` e me mande o XLSX.
2. Crie conta IG throwaway (não use a pessoal!) e salve usuário/senha nos GitHub Secrets.
3. Ative CallMeBot (instrução no arquivo).
4. Eu refino os scrapers das UFs que derem problema.
