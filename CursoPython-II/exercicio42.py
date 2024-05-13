print('-='*20)
r1 = float(input('Digite o primeiro segmento de reta: '))
r2 = float(input('Digite o segundo segmento de reta: '))
r3 = float(input('Digite o terceiro segmento de reta: '))
print('-='*20)
#condição para determinar se as retas formam um triangulo

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    if r1 == r2 == r3:
        print('Os segmentos acima formam um triangulo equilátero!')
    elif r1 != r2 != r3 != r1:
        print('Os segmentos acima formam um triangulo escaleno!')
    else:
        print('Os segmentos acima formam um triangulo isóceles!')
else:
    print('Os segmentos acima não formam um triangulo!')
print('-='*20)