import datetime
anoAtual = datetime.date.today().year
nascimento = int(input("Em que ano você nasceu? "))
idade = anoAtual - nascimento
print("Quem nasceu em {} tem {} no ano de {}".format(nascimento, idade, anoAtual))

if idade == 18:
    print("Está na hora de se alistar!")
elif idade > 18:
    saldo = idade - 18
    print("Você já deveria ter se alistado há {} anos".format(saldo))
    ano = anoAtual - saldo
    print("Seu alistamento foi em {}".format(ano))
else:
    saldo = 18 - idade
    print("Ainda faltam {} anos para o seu alistamento".format(saldo))
    ano = anoAtual + saldo
    print("Seu alistamento será em {}".format(ano))
