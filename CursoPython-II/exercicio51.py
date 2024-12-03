inicio = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = inicio + (10-1) * razao
for c in range(inicio, decimo + razao, razao):
    print('{} '.format(c), end='→ ')
print('ACABOU')
