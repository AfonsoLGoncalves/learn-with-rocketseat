lista = [1, 2, 4, 5, 10, 21, 1, 2, 4]
lista_ordenada = sorted(lista)


def calcular_mediana(lista_de_numeros):

    if len(lista_de_numeros) % 2 == 0:
        posicao = int(len(lista_de_numeros)/2)
        mediana = (lista_de_numeros[posicao+1] + lista_de_numeros[posicao])/2
        return mediana
    else:
        posicao = int((len(lista_de_numeros)/2)+0.5)
        mediana = lista_ordenada[posicao]
        return mediana


resultado = calcular_mediana(lista_ordenada)
print(resultado)
