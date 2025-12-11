from random import randrange
from os import system

mapa = [
    [' ', ' ', ' '],  # linha 0
    [' ', ' ', ' '],  # linha 1
    [' ', ' ', ' ']   # linha 2
]

linha_tesouro = 1
coluna_tesouro = 0
tentativas = 0


def exibirMapa():
    for linha in mapa:
        print('|'.join(linha))
        print('-' * 5)


def validarPalpite(linha, coluna):
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        print('❌ Palpite inválido! Valores de linha e coluna devem ser maior que 0 e menor que 2.')
        input("Pressione ENTER para próximo palpite")
        return False
    elif mapa[linha][coluna] == 'X':
        print('⚠️ Palpite inválido! Esse campo do mapa já foi preenchido em algum palpite prévio.')
        input("Pressione ENTER para próximo palpite")
        return False
    else:
        return True


def palpite(linha, coluna):
    global tentativas
    if tentativas == 4:
        print(f'Suas tentativas acabaram! Você perdeu!')
        print(f'O tesouro estava aqui: ')
        mapa[linha][coluna] = '💎'
        exibirMapa()
        return True
    elif linha == linha_tesouro and coluna == coluna_tesouro:
        mapa[linha][coluna] = '💎'
        tentativas += 1
        print(f'Você venceu! E em apenas {tentativas} tentativas!')
        return True
    else:
        mapa[linha][coluna] = 'X'
        tentativas += 1
        print('Essa é sua ultima chance') if tentativas == 4 else print(
            f'Você errou! você tem mais {5 - tentativas} tentativas!')
        return False


while True:
    try:
        system('clear')
        linha = int(input('Digite a linha: '))
        coluna = int(input('Digite a coluna: '))
        if validarPalpite(linha, coluna):
            if palpite(linha, coluna):
                print(
                    'SEE YOU SPACE COWBOY!')
                break
            exibirMapa()
            input("Pressione ENTER para próximo palpite")
    except ValueError:
        print('Os valores devem ser números inteiros!')
