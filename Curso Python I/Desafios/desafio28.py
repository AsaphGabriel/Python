from random import randint

computador = randint(0, 5) #define qual numero aleatorio o computador "pensou"
print('-=-' * 25)
print('Vou pensar em um numero entre 0 e 5, tente adivinhar!')
print('-=-' * 25)

jogador = int(input('Em que numero eu pensei?')) #o jogador tenta adivinhar

if jogador == computador:
    print('Parabens! Você adivinhou corretamente!')
else:
    print('Você errou! eu pensei em {}'.format(computador))
print('-=-' * 25)
