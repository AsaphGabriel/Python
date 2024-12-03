escolha = 1
while escolha == 1 :
    tabuada = int(input('Digite um numero e veja sua tabuada: '))
    for i in range(1,11):
        print(f'{tabuada} x {i} = {tabuada * i}')
    escolha = int(input('''
    Quer ver outra tabuada?
    1 - Sim.
    2 - Não.
    '''))