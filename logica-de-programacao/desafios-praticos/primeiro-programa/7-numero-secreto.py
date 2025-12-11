from random import randrange

tentativas = 0
numero_secreto = int(randrange(1, 11))

chute = int(input('Dê um palpite, com sorte você pode acertar: '))
while True:
    if chute == numero_secreto:
        tentativas += 1
        print(f'Voce precisou de apenas {tentativas} tentativas para acertar!')
        break
    else:
        chute = int(input('você errou, mas não desanime, dê outro palpite: '))
        tentativas += 1
