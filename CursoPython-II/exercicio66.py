soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar):'))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos valores foi: {soma} e foram somados {cont} numeros!')
