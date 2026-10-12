# O nosso wrapped

O "Wrapped" do namoro, igual ao do Spotify: telas em pé que passam sozinhas, com música,
números grandes e fotos. Conta tudo desde 25/03, o começo de verdade.

As telas, em ordem:

1. **Abertura:** "o nosso wrapped 2026" e o botão começar (o toque libera o som no iPhone).
2. **O começo:** 25/03 e quantos dias se passaram (conta sozinho pela data do aparelho).
3. **A primeira mensagem:** a resposta no story dela no Instagram, num balão.
4. **O primeiro abraço:** 28/03, e a primeira mensagem dela no WhatsApp naquela noite.
5. **WhatsApp** (só aparece se existir o `dados-whatsapp.js`):
   - quantas mensagens, com um gráfico por mês;
   - quem manda mais e quem puxa assunto primeiro;
   - quantos "te amo" (uma vez por mensagem) e o recorde numa mensagem só;
   - o emoji do ano;
   - a hora em que vocês mais conversam;
   - o dia recorde, com horas de ligação, áudios, bons dias e "saudade".
6. **Top momentos:** os 5 momentos, como a lista de músicas do Spotify.
7. **O pedido:** a foto do anel, dias de namoro e quanto falta pro próximo mesversário.
8. **A artista do ano:** Beyoncé (3 das 7 músicas).
9. **Top músicas:** com as capas.
10. **Fotos nossas:** um mosaico de fotos andando e o número 191 (o total de fotos do site eu-e-voce).
11. **Motivos:** os 16 motivos passando rápido.
12. **A personalidade do casal:** sai dos números do WhatsApp ("os grudados", "os da madrugada"...).
13. **O resumo:** o cartão com tudo, e um botão pra salvar como imagem (no iPhone abre o
    compartilhar, e dá pra salvar nas Fotos).
14. **O final:** a carta curta e o "ver de novo".

Ela toca na direita pra passar, na esquerda pra voltar, e segura pra pausar. O botão de som
fica no canto de cima.

## Como abrir

Abra pelo link do GitHub Pages no Safari. No computador, rode um servidor na pasta
(`python -m http.server`) e abra `http://localhost:8000`.

## Trocar coisas

Tudo fica no começo do `<script>` do `index.html`:

- `TEXTOS`: todos os textos (são rascunhos).
- `MOMENTOS`: os top momentos. O primeiro da lista é o número 1.
- `MUSICAS`: as top músicas e as capas.
- `MOTIVOS`: os motivos (copiados do site eu-e-voce).
- `COMECO`, `PEDIDO` e `TOTAL_FOTOS`.

As fotos ficam em `ferramentas/preparar-fotos.py`. Depois de trocar, rode:

    python ferramentas/preparar-fotos.py

## Os números do WhatsApp

1. Exporte a conversa com ela **sem mídia** e salve o `.zip` em `Documentos\wrapped`
   (fora desta pasta, pra conversa nunca ir pro GitHub).
2. Rode:

       python ferramentas/contar-whatsapp.py "C:/Users/thale/Documents/wrapped"

3. Ele grava o `dados-whatsapp.js`, que tem **só números** (quantidades, horas, emojis),
   nenhuma mensagem. Se ele não descobrir quem é quem, rode com `--ela "nome dela"`.

Se o WhatsApp não guardou a conversa desde 25/03, a tela das mensagens avisa desde quando
estão contando.

## Arquivos

- `index.html`: o site inteiro
- `dados-whatsapp.js`: os números da conversa (gerado)
- `fotos/`: as fotos diminuídas (geradas)
- `musicas/`: as músicas cortadas (copiadas do toca-discos)
- `ferramentas/`: os scripts das fotos e do WhatsApp

## Para testar

- `index.html?teste=1&historia=pedido`: abre parado no fim dessa tela (pra print).
- `&t=3`: parado no segundo 3 da tela.
- `&hoje=2026-10-20`: finge que hoje é outro dia.
- `&semwhats=1`: como fica sem as telas do WhatsApp.

No modo `teste=1` nada anda sozinho. Pra ver normal, abra sem ele.
