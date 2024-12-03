repetir = 1
# Solicita os números dos conjuntos ao usuário
entrada_a = input("Digite os números do conjunto A, separados por espaço: ")
conjunto_a = set(entrada_a.split())

entrada_b = input("Digite os números do conjunto B, separados por espaço: ")
conjunto_b = set(entrada_b.split())

# Realiza a união dos conjuntos A e B
uniao = conjunto_a | conjunto_b

# Realiza a interseção dos conjuntos A e B
intersecao = conjunto_a & conjunto_b

# Realiza a diferença entre os conjuntos A e B
diferenca_a_b = conjunto_a - conjunto_b

# Realiza a diferença entre os conjuntos B e A
diferenca_b_a = conjunto_b - conjunto_a
escolha = int(input("""
Escolha uma opção:
1)União
2)Interseção
3)Diferença A - B
4)Diferença B - A"""))
while repetir == 1:
    match escolha:
        case 1:
            print("União:", uniao)
            repetir = 0
            break;
        case 2:
            print("Interseção:", intersecao)
            repetir = 0
            break;
        case 3:
            print("Diferença A - B:", diferenca_a_b)
            repetir = 0
            break;
        case 4:
            print("Diferença B - A:", diferenca_b_a)
            repetir = 0
            break;
        case _:
            print("Digite uma opção valida")
            repetir = 1

# Exibe os resultados


