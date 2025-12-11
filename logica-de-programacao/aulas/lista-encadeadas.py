lista = {
    'valor': 5,
    'proximo': None
}

def exibeLista(lista):
    if not lista:
        print('Lista encontra-se vazia')
        return
    elemento = lista

    while elemento != None:
        print(elemento['valor'], end=' ')
        elemento = elemento['proximo']
    print('.')

def adicionaNoFim(elemento):
    global lista
    if not lista:
        lista = { 'valor': elemento, 'proximo': None}
        return
    atual = lista
    while atual['proximo'] != None:
        atual = atual['proximo']
    atual['proximo'] = {'valor': elemento, 'proximo': None}

exibeLista(lista)
print('Adicionando o número 5...')
adicionaNoFim(5)
exibeLista(lista)
print('Adicionando o número 4...')
print('Adicionando o número 3...')
adicionaNoFim(4)
adicionaNoFim(3)
exibeLista(lista)
