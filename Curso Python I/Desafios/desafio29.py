velocidade = float(input('Em qual velocidade você está? :'))
multa = 0
excedente = velocidade - 80
if velocidade > 80:
    multa = excedente * 7
    print('MULTADO! Você excedeu o limite de 80km/h da via!')
    print('A multa foi de R$:{:.2f} '.format(multa))
else:
    print('Tenha um bom dia, dirija com segurança!')
