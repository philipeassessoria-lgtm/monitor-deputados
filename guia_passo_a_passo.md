# Guia Passo-a-Passo (Para quem não é desenvolvedor)

Objetivo: colocar o sistema automático no ar, rodando todo dia, sem precisar programar. Tempo estimado: 1h se seguir tudo direitinho.

Se travar em qualquer passo, me mande um print e eu desbloqueio.

---

## ETAPA 0 — Crie 3 contas (20 min)

### 0.1 Conta GitHub (grátis)
1. Abra https://github.com/signup
2. Preencha email, senha, username (ex: `philipeassessoria`)
3. Confirme o email que o GitHub mandar
4. Quando pedirem "How many team members?" escolha "Just me"
5. Quando pedirem "What's your interest?" marque qualquer coisa, pode pular
6. Pronto.

### 0.2 Conta Instagram descartável (5 min)
**NÃO use sua conta pessoal.** Crie uma só pra isso.
1. No celular ou computador abra instagram.com
2. Crie conta nova com email diferente (sugestão: crie um gmail novo tipo `monitordeputados2026@gmail.com`)
3. Use nome genérico tipo "Maria Monitora"
4. Não precisa postar nada, não precisa ter seguidor
5. Anote usuário e senha — vamos usar depois

### 0.3 Ativar CallMeBot no seu WhatsApp (3 min)
1. No WhatsApp, salve este contato: `+34 644 51 95 23` com nome `CallMeBot`
2. Abra conversa com ele e envie EXATAMENTE: `I allow callmebot to send me messages`
3. Em até 2 minutos você recebe: `API Activated for your phone number. Your APIKEY is 1234567`
4. **Anote esse APIKEY** — vai precisar.

---

## ETAPA 1 — Crie o repositório no GitHub (10 min)

1. Logado no GitHub, clique no botão `+` no topo direito → `New repository`
2. Nome do repositório: `monitor-deputados` (ou outro nome)
3. Escolha **Public** (importante! GitHub Actions é ilimitado em repo público)
4. Marque a caixa "Add a README file"
5. Clique em `Create repository`
6. Na página do repositório, clique no botão verde `Add file` → `Upload files`
7. Arraste **TODA a pasta `outputs/` que você recebeu** para dentro
8. Espera terminar o upload (barrinha)
9. Embaixo, clique em `Commit changes`

---

## ETAPA 2 — Configure os 4 segredos (5 min)

No repositório recém-criado:
1. Clique em `Settings` (menu no topo, precisa rolar)
2. No menu lateral esquerdo: `Secrets and variables` → `Actions`
3. Clique no botão verde `New repository secret`
4. Adicione estes 4 segredos (um por vez):

| Name | Secret (valor) |
|---|---|
| `IG_USER` | o usuário da sua conta IG descartável |
| `IG_PASS` | a senha da sua conta IG descartável |
| `CALLMEBOT_APIKEY` | o APIKEY que o CallMeBot te mandou |
| `CALLMEBOT_PHONE` | `5583991424780` (seu número com DDI, sem + nem espaços) |

---

## ETAPA 3 — Rode o primeiro teste manual (5 min)

1. No repositório, clique na aba `Actions` (no topo)
2. Se aparecer "Workflows aren't being run..." clique em `I understand my workflows, go ahead and enable them`
3. Na lista, clique em `Daily scrape & digest`
4. Botão `Run workflow` (direita) → clique outro `Run workflow` verde
5. Aguarde 2-3 min → a bolinha amarela vira verde se deu certo (ou vermelha se falhou)

### Se deu verde:
- Você já deve ter recebido mensagem no WhatsApp
- Na aba `Actions`, abra a execução → veja os logs de cada passo
- O dashboard vai estar em: `https://SEUUSUARIO.github.io/monitor-deputados/`

### Se deu vermelho:
- Clique na execução
- Veja qual passo falhou (bolinha vermelha)
- Copie o erro e me mande — eu te digo o que consertar

---

## ETAPA 4 — Ativar GitHub Pages (2 min)

Pra ver o dashboard bonito:
1. `Settings` → menu lateral `Pages`
2. Em "Source" escolha `Deploy from a branch`
3. Em "Branch" escolha `gh-pages` → pasta `/ (root)` → `Save`
4. Aguarde ~2 min
5. O link aparece em cima da página: `https://SEUUSUARIO.github.io/monitor-deputados/`
6. Favorite esse link no celular

---

## ETAPA 5 — Pronto!

O sistema roda **todo dia às 7h da manhã** (automático). Você recebe no WhatsApp o top 10, e pode abrir o dashboard a qualquer momento.

---

## Problemas comuns e soluções

**"Instagram está bloqueando login"**
→ Faça login manual uma vez no celular com a conta descartável pra "limpar" o desafio. Depois o bot consegue.

**"Secret CALLMEBOT_APIKEY não funciona"**
→ Copiou sem espaços no início/fim? Recomece a ativação mandando de novo a frase-chave pro CallMeBot.

**"Workflow não roda diariamente"**
→ O GitHub pausa workflows de repositórios sem atividade por 60 dias. Basta você abrir o repo e dar qualquer commit uma vez por mês (o bot próprio já faz isso).

**"Scrapers de UFs estão retornando vazio"**
→ Normal para o primeiro run: cada Assembleia tem layout próprio. Me mande a lista de UFs que falharam e eu ajusto os seletores.

---

## Se você quer pagar alguém pra fazer isso pra você

Veja o arquivo `brief_freelancer.md` — é o texto pronto pra você colar no Workana/99freelas. Custo típico: R$ 200-500 (pagamento único).
