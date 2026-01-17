lista_de_compras = []
reposta = None
while reposta != 'acabou':
    reposta = input('O que vamos comprar? ')
    if reposta != 'acabou':
        lista_de_compras.append(reposta)

print(lista_de_compras)
