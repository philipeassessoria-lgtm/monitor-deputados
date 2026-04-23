# Briefing para contratar freelancer — Monitor de Deputados

Cole este texto em Workana, 99freelas, GetNinjas ou grupo de devs no WhatsApp.

---

## Título sugerido:
**Deploy de script Python no GitHub Actions + integração Instagram/WhatsApp (R$ 300-500)**

---

## Descrição (cole abaixo):

Olá! Preciso de alguém experiente com Python e GitHub Actions para subir pra mim um sistema já pronto. Não preciso programar nada novo — o código está todo escrito e testado. Preciso apenas de deploy e configuração.

### O que já tenho pronto:
Pacote completo de código (Python) que:
- Busca lista dos 513 deputados federais + deputados estaduais do Brasil
- Pega os posts do Instagram de cada um nas últimas 24h
- Ranqueia por engajamento
- Gera dashboard HTML visual
- Envia top 10 no WhatsApp via CallMeBot (grátis)

### O que preciso que você faça:
1. Criar repositório no meu GitHub (eu forneço acesso)
2. Fazer upload dos arquivos que eu te mando
3. Configurar os 4 secrets: IG_USER, IG_PASS, CALLMEBOT_APIKEY, CALLMEBOT_PHONE
4. Rodar primeira execução manual do workflow e verificar que funciona
5. Ativar GitHub Pages para o dashboard ficar público
6. Calibrar os scrapers das 27 Assembleias Legislativas (ajustar seletores CSS que estão genéricos — ~15 minutos por UF, documentação nos comentários do código)
7. Me deixar um vídeo curto (Loom/YouTube unlisted) de 5 min mostrando onde clico para ver relatórios e como debugar se algo falhar

### Stack (tudo grátis):
- Python 3.11 + Instaloader + BeautifulSoup
- GitHub Actions (cron)
- GitHub Pages (dashboard)
- CallMeBot (WhatsApp)

### Prazo:
Até 1 semana.

### Orçamento:
R$ 300 a R$ 500. Pagamento via Pix após entrega funcional (sistema rodando por 2 dias sem erro).

### Requisitos do profissional:
- Experiência com Python e GitHub Actions (obrigatório)
- Já ter usado Instaloader ou scrapers de Instagram antes (preferencial)
- Paciência para ajustar scrapers HTML das 27 Assembleias (cada uma tem seu formato)
- Comunicação em português

### Como vai ser:
1. Você dá "Quero me candidatar"
2. Mando o pacote de código (zip de ~50 KB)
3. Você olha e confirma o orçamento
4. Te dou acesso ao meu GitHub
5. Você faz o deploy
6. Verifico que roda 2 dias seguidos
7. Pago via Pix

Dúvidas, me chame aqui.

---

## Onde postar (em ordem de recomendação):

1. **Workana** (workana.com) — mais sério, melhores devs, 14% taxa
2. **99freelas** (99freelas.com.br) — meio termo
3. **GetNinjas** — mais local, pode demorar
4. **Grupos no Telegram/WhatsApp de devs Python**: "Python Brasil", "Devs BR"
5. **LinkedIn**: post orgânico com hashtags #python #freelancer

## Dicas para escolher o freelancer:

- Peça portfólio com pelo menos 1 projeto GitHub Actions
- Peça referências (clientes anteriores)
- Faça videocall de 15 min antes de fechar — sente se a pessoa é séria
- Pague 50% no início + 50% na entrega, OU 100% na entrega (sua preferência)
- Exija que o código fique em repositório SEU (não dele) — ele só tem acesso de collaborator
- Depois do deploy, REMOVA o acesso dele ao repo (Settings → Collaborators → Remove)
