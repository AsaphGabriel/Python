km = float(input('Quantos Km você vai viajar?'))
passagem = float
if km <= 200:
    passagem = km * 0.50
    print('O valor da passagem vai ficar R$: {:.2f}'.format(passagem))
else:
    passagem = km *0.45
    print('O valor da passagem vai ficar R$: {:.2f}'.format(passagem))
