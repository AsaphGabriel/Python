altura = float(input('Qual a altura da sua parede em metros?'))
largura = float(input('Qual a largura da sua parede em metros?'))
area = (altura * largura)
print('A sua parede tem {}m² de área'.format(area))
# Cada litro de tinta pinta 2m² da parede
tinta = (area / 2)
print('Você vai precisar de {}L de tinta para pintar {}m² de parede'.format(tinta, area))
