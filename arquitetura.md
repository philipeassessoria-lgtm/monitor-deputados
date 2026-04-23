# Arquitetura do Sistema — Zero Custo

## Fluxo diário

```
07:00 BRT  ┌─────────────────────────────────────────────────┐
           │  GitHub Actions (cron: "0 10 * * *")            │
           └────────────────────┬────────────────────────────┘
                                │
     ┌──────────────────────────┼──────────────────────────┐
     ▼                          ▼                          ▼
┌─────────┐              ┌─────────────┐            ┌─────────────┐
│  Step 1 │              │   Step 2    │            │   Step 3    │
│ Carrega │  ──────►     │  Instaloader│  ──────►   │  Rankeia    │
│ lista de│              │  posts 24h  │            │  engajamento│
│ handles │              │  c/ login   │            │             │
└─────────┘              └─────────────┘            └─────────────┘
                                                           │
                                                           ▼
                                              ┌─────────────────────┐
                                              │  Gera 2 saídas:     │
                                              │  (a) dashboard HTML │
                                              │  (b) digest WhatsApp│
                                              └──────────┬──────────┘
                                                         │
                                   ┌─────────────────────┴─────────────────────┐
                                   ▼                                           ▼
                          ┌─────────────────┐                         ┌─────────────────┐
                          │ GitHub Pages    │                         │ CallMeBot       │
                          │ (dashboard pub) │                         │ WhatsApp  +5583 │
                          └─────────────────┘                         └─────────────────┘
```

## Componentes — todos grátis

| Componente | Ferramenta | Custo | Limites |
|---|---|---|---|
| Cron | GitHub Actions | Grátis | 2.000 min/mês em repo privado |
| Scraper IG | Instaloader (Python) | Grátis | IG pode limitar, usar login |
| Scraper ALs | requests + BeautifulSoup | Grátis | Nenhum |
| Descoberta handle | DuckDuckGo HTML search | Grátis | Nenhum prático |
| DB | JSON/SQLite no próprio repo | Grátis | 1 GB repositório |
| Dashboard | HTML estático + GitHub Pages | Grátis | 100 GB/mês de banda |
| Notificação | CallMeBot (WhatsApp API grátis) | Grátis | ~1 msg/10s |
| Fallback notificação | Telegram Bot | Grátis | Sem limites práticos |

## Por que esta arquitetura?

1. **Sem servidor para gerenciar** — GH Actions roda sozinho.
2. **Sem banco externo** — o histórico fica versionado no Git (você até vê o `git blame` de cada update).
3. **Dashboard pública mas com URL difícil de adivinhar** — se quiser privar de verdade, use Vercel + Basic Auth (também grátis).
4. **Rollback fácil** — qualquer dia ruim, `git revert`.

## Plano B: Oracle Cloud Free Tier

Se o GitHub Actions começar a limitar ou o Instagram banir o IP do runner (todo PR usa IPs compartilhados):

- Oracle Cloud oferece **2 VMs ARM sempre grátis** (24 GB RAM total).
- Instalar Python + cron.
- Mesmos scripts rodam lá sem alteração.
- Setup: ~30 min.

## Estratégia contra rate-limit do Instagram

1. Usar conta "throwaway" (NUNCA a pessoal) com login.
2. Respeitar delay de 3-5s entre perfis.
3. Rodar em 3 batches diários (seeds rotativas) ao invés de tudo às 7h.
4. Se banir, trocar conta ou usar VPN no runner (GitHub Actions suporta via addon).
5. Preferir o endpoint GraphQL público que o Instaloader já usa — mais estável que scraping de HTML.

## Estratégia de escala para 1.572 perfis

Com delay de 3s:
- 1.572 × 3s = **78 min por run** ✅ cabe no free tier GH Actions (job max 6h).
- 30 runs/mês = 39h/mês. ✅ cabe nos 2.000 min (33h) **se usar repo público** — em público é **ilimitado**!

**👉 Recomendação forte: repositório PÚBLICO.** GitHub Actions ilimitado. Se quiser privacidade dos dados raspados, salvar em branch `private-data` ou em GitHub Releases com link direto.

## Segurança

- Conta IG throwaway ≠ pessoal.
- API key CallMeBot nos **GitHub Secrets** (nunca no código).
- Credenciais IG também nos Secrets.
- Dashboard: se quiser totalmente privado, mover para Vercel com GitHub OAuth (ainda grátis).

## Monitoramento

- [Healthchecks.io](https://healthchecks.io) — ping grátis toda vez que o job termina. Se falhar, você recebe email.
- Logs ficam nos "Actions" do GitHub por 90 dias.

## Limitações honestas

- **Instagram pode mudar API/HTML a qualquer momento.** Preparar para manutenção ocasional.
- **Posts privados ou contas fechadas:** não raspa. Lista dos públicos é o que interessa mesmo.
- **Engajamento de comentários internos:** Instaloader só pega contagem, não o conteúdo dos comentários (suficiente pra ranking).
- **ALs que mudarem site:** scrapers quebram. Detectar com asserts no código (ex: "esperava N deputados, encontrei M").

---

## Custo real para você: R$ 0

Única coisa: criar 1 conta Instagram extra pra login do scraper (use email descartável). Fora isso, tudo é cadastro grátis.
