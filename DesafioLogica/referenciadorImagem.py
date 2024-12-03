from datetime import date
quant = int(input('Quantas imagens você vai formatar? '))
data = date.today()
dataF = data.strftime('%d/%m/%Y')
texto = ''

for c in range (1, quant + 1, +1):
    link = str(input('Qual é o {}° link?'.format(c)))

    texto += ('FIGURA {} - {} - Acessado em {}\n'.format(c, link, dataF))
print(texto)
