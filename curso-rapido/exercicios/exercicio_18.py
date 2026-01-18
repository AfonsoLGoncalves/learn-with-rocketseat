lista = [2, 5, 8, 10, 11, 13, 15, 18, 20]
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


# Segundo Quartil (Q2)
def calcular_Q2(lista_ordenada):
    resultado_Q2 = calcular_mediana(lista_ordenada)
    calcular_Q1(lista_ordenada, resultado_Q2)
    calcular_Q3(lista_ordenada, resultado_Q2)
    return resultado_Q2


# Primeiro Quartil (Q1)
def calcular_Q1(lista_ordenada, resultado_Q2):
    posicao_Q1 = lista_ordenada.index(resultado_Q2)
    metade_inferior = lista_ordenada[:posicao_Q1-1]
    resultado_Q1 = calcular_mediana(metade_inferior)
    return resultado_Q1


# Terceiro Quartil (Q3)
def calcular_Q3(lista_ordenada, resultado_Q2):
    posicao_Q1 = lista_ordenada.index(resultado_Q2)
    metade_inferior = lista_ordenada[posicao_Q1+1:]
    resultado_Q1 = calcular_mediana(metade_inferior)
    return resultado_Q1


# Demonstra resultados em tela
def mostrar_resultados(lista_ordenada):
