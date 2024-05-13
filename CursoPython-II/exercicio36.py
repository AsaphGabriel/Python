valorCasa = float(input("Qual é o valor da casa? :"))
salarioCliente = float(input("Qual é o seu salario? :"))
anosParcela = int(input("Em quantos anos quer financiar? :"))
valorParcela = valorCasa / (anosParcela * 12)

if valorParcela >= salarioCliente * 0.3:
    print("Para pagar uma casa de R$:{:.2f} em {} anos a prestação por mês será de R$:{:.2f}! \n".format(valorCasa, anosParcela, valorParcela))
    print("EMPRÉSTIMO NEGADO!")
else:
    print("Para pagar uma casa de R$:{:.2f} em {} anos a prestação por mês será de R$:{:.2f}! \n".format(valorCasa, anosParcela, valorParcela))
    print("EMPRÉSTIMO ACEITO!")
