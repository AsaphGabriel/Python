num = int(input('De qual numero você quer a tabuada? '))
multi = int(input('Até qual multiplicador? '))
for cont in range(1, multi + 1, 1):
    print('{} x {:2} = {}'.format(num, cont, num * cont))
