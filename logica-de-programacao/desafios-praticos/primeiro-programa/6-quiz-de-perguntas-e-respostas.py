perguntas_e_respostas = [['Quanto é 2 + 2?', '4'],
                         ['Qual melhor time do mundo?', 'vasco'],
                         ['Quem é o melhor pai do MUNDO?', 'ademir']
                         ]
acertos = 0

for pergunta, gabarito in perguntas_e_respostas:
    resposta = input(f'{pergunta} ')
    if resposta.lower() == gabarito:
        acertos += 1

print(f'Você acertou {acertos} perguntas! Estás de parabéns!')
