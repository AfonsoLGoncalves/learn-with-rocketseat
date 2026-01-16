# pedir o preço de 3 produtos e escolher o menor preço
preco_1 = float(input('Digite o preço do primeiro produto: '))
preco_2 = float(input('Digite o preço do segundo produto: '))
preco_3 = float(input('Digite o preço do terceiro produto: '))

if preco_1 > preco_2 & preco_2 > preco_3:
    print('Vamos comprar o terceiro produto')
elif preco_2 > preco_1 & preco_3 > preco_1:
    print('Vamos comprar o primeiro produto')
else:
    print('Vamos comprar o segundo produto')
