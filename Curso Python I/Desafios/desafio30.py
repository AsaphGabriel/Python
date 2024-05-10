num = int(input('Digite um numero e verifique se é par ou impar: '))
imPar = num % 2
if imPar == 0:
    print('O numero {} é par'.format(num))
else:
    print('O numero {} é impar'.format(num))
