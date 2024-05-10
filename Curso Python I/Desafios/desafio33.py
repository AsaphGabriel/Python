a = int(input('Primeiro valor: '))
b = int(input('Primeiro valor: '))
c = int(input('Primeiro valor: '))
#verifica qual é o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b :
    menor = c

#verifica qual é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b :
    maior = c
print('o menor valor digitado foi: {} e o maior foi: {}'.format(menor, maior))
