lista = [1, 2, 34, 5, 6, 10, 20, 30]


def calcular_amplitude(lista):
    if not lista:
        return 0

    max_valor = max(lista)
    min_valor = min(lista)
    return max_valor - min_valor


print(calcular_amplitude(lista))
