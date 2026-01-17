lista = [1, 2, 3, 4, 5]
lista_acumulada = [0]

for n in lista:
    soma = n + lista_acumulada[-1]
    lista_acumulada.append(soma)

lista_acumulada.remove(0)
print(lista_acumulada)
