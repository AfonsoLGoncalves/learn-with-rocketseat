resposta = input('bora rolezar? [s/n]? ')
n = 1
while resposta != 's':
    resposta = input(f'BOR{'A' * n}? [s/n]? ')
    n += 1
    if 'chat' in resposta:
        print('Foi mal nengue')
        break
    else:
        print(f'Então BOR{'A' * n}!')
