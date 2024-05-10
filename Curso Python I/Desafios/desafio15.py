dias = float(input('Por quantos dias você alugou o carro? '))
diasSm = float(dias * 60)
km = float(input('Quantos Km você percorreu com o carro? '))
kmSm = float(km * 0.15)
smTotal = diasSm + kmSm
print('O total a pagar é de R$:{:.2f}'.format(smTotal))
