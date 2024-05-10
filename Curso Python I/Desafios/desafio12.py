precoN = float(input('Digite o preço atual e confira o preço com desconto R$:'))
desc = precoN - (precoN * 0.05)
print('O preço com desconto desse produto é de R$:{:.2f}'.format(desc))
