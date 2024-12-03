peso = float(input('Digite o seu peso (Kg):  '))
altura = float(input('Digite sua altura (M):  '))
imc = peso / (altura ** 2)
print('Seu imc é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está em seu peso ideal.')
elif 25 <= imc < 30:
    print('Você está na faixa do sobrepeso.')
elif 30 <= imc < 40:
    print('Você está na faixa da obesidade.')
else:
    print('Você está na faixa de obesidade mórbida.')
