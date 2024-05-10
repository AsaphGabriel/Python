salario = float(input('Qual é o salario do funcionario? R$:'))
#calcula o aumento percentual com base no valor do salario
aumento = float
if salario <= 1250.00:
    aumento = salario + (salario * 0.15)
else:
    aumento = salario + (salario * 0.10)
print('O funcionario que ganhava R$:{:.2f} passará a ganhar R$:{:.2f}'.format(salario, aumento))
