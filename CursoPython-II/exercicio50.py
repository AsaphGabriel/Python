soma = 0
cont = 0
for i in range(1, 7, 1):
    num = int(input('Digite o {}° numero: '.format(i)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('A soma dos {} numeros pares digitados foi: {}'.format(cont, soma))
