lista = [2, 5, 8, 10, 11, 13, 15, 18, 20]
lista_ordenada = sorted(lista)


def calcular_mediana(lista_ordenada):
    n = len(lista_ordenada)
    if n == 0:
        return 0
    meio = len(lista_ordenada) // 2
    if len(lista_ordenada) % 2 == 0:
        return (lista_ordenada[meio-1] + lista_ordenada[meio]) / 2
    else:
        return lista_ordenada[meio]


# Segundo Quartil (Q2)
def calcular_Q2(lista_ordenada):
    return calcular_mediana(lista_ordenada)


# Primeiro Quartil (Q1)
def calcular_Q1(lista_ordenada):
    meio = len(lista_ordenada) // 2
    return calcular_mediana(lista_ordenada[:meio])


# Terceiro Quartil (Q3)
def calcular_Q3(lista_ordenada):
    meio = len(lista_ordenada) // 2

    # Se a lista for ímpar, pulamos o elemento do meio
    if len(lista_ordenada) % 2 == 0:
        metade_superior = lista_ordenada[meio:]
    else:
        metade_superior = lista_ordenada[meio + 1:]
    return calcular_mediana(metade_superior)


# Execução
q2 = calcular_Q2(lista_ordenada)
q1 = calcular_Q1(lista_ordenada)
q3 = calcular_Q3(lista_ordenada)


# Demonstra resultados em tela
def mostrar_resultados(r1, r2, r3):
    print(f"Primeiro Quartil (Q1) = {r1}")
    print(f"Segundo Quartil (Q2/Mediana) = {r2}")
    print(f"Terceiro Quartil (Q3) = {r3}")


mostrar_resultados(q1, q2, q3)
