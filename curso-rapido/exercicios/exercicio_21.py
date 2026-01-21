def elevar_lista(lista_de_numeros, numero_elevado):
    lista_resposta = []
    for numero in lista_de_numeros:
        lista_resposta.append(numero ** numero_elevado)
    return lista_resposta


lista_valores = []

for valor in range(10):
    lista_valores.append(
        int(input('Me diga um número: '))
    )

dicionario = {
    'lista_padrao': lista_valores,
    'lista_quadradra': elevar_lista(lista_valores, 2),
    'lista_cúbica': elevar_lista(lista_valores, 3)
}

print(dicionario)
