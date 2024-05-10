# Exibe a tabuada de 1 à 10 de um numero digitado

num = int(input('Digite um numero:'))
print('-' * 20)
print('A tabuada de {} é:'.format(num))
for i in range(10):
    multi = i + 1
    result = num * multi
    print('{} x {:2} = {}'.format(num, multi, result))
print('-' * 20)