import datetime
anoAtual = datetime.date.today().year
nascimento = int(input("Ano de Nascimento: "))
idade = anoAtual - nascimento
print("O atleta tem {} anos".format(idade))
if idade <= 9:
    print("Clasificação: Mirim")
elif idade <= 14:
    print("Clasificação: Infantil")
elif idade <= 19:
    print("Clasificação: Junior")
elif idade <= 25:
    print("Clasificação: Sênior")
else:
    print("Clasificação: Master")
