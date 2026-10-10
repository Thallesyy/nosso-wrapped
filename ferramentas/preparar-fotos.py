"""Copia e diminui as fotos do Wrapped pra pasta fotos/.

As fotos originais ficam no site eu-e-voce-react. Pra trocar uma foto, mude o nome
nas listas abaixo e rode de novo:

    python ferramentas/preparar-fotos.py

Não usar: dates17, dates29, dates30, dates1, dates3, dates13, random19, us23, random9.
"""
import os
from PIL import Image, ImageOps

AQUI = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(AQUI)
ORIGEM = os.path.join(SITE, '..', 'eu-e-voce-react 2', 'eu-e-voce-react', 'public')
DESTINO = os.path.join(SITE, 'fotos')

# fotos grandes: nome no site -> foto original
GRANDES = {
    'pedido': 'us10',         # o anel
    'mensagens': 'us19',      # espelho com o celular rosa
    'personalidade': 'us28',
    'resumo': 'us32',
    'final': 'us27',
}

# o mosaico da tela "fotos nossas"
MOSAICO = [
    'us2', 'us5', 'us6', 'us8', 'us9', 'us13', 'us14', 'us21', 'us24',
    'us41', 'us29', 'us30', 'us33', 'us34', 'us37', 'us39', 'us40', 'us42',
]

# capas das músicas (capa1 = Pyramids, capa2 = Love Drought, ...)
CAPAS = ['capa1', 'capa2', 'capa3', 'capa4', 'capa5', 'capa6', 'capa7']

PROIBIDAS = {'dates17', 'dates29', 'dates30', 'dates1', 'dates3', 'dates13',
             'random19', 'us23', 'random9'}


def abrir(nome):
    if nome in PROIBIDAS:
        raise SystemExit('a foto %s está na lista de não usar' % nome)
    im = Image.open(os.path.join(ORIGEM, nome + '.jpg'))
    return ImageOps.exif_transpose(im).convert('RGB')


def salvar(im, nome, qualidade=82):
    caminho = os.path.join(DESTINO, nome + '.jpg')
    im.save(caminho, 'JPEG', quality=qualidade, optimize=True, progressive=True)
    return os.path.getsize(caminho)


def main():
    os.makedirs(DESTINO, exist_ok=True)
    total = 0
    for nome, original in GRANDES.items():
        im = abrir(original)
        im.thumbnail((1100, 1100), Image.LANCZOS)
        total += salvar(im, nome)
    for i, original in enumerate(MOSAICO):
        im = ImageOps.fit(abrir(original), (420, 560), Image.LANCZOS)
        total += salvar(im, 'mosaico%d' % (i + 1), 78)
    for original in CAPAS:
        im = ImageOps.fit(abrir(original), (300, 300), Image.LANCZOS)
        total += salvar(im, original, 80)
    print('%d fotos, %.1f MB' % (len(GRANDES) + len(MOSAICO) + len(CAPAS), total / 1e6))


if __name__ == '__main__':
    main()
