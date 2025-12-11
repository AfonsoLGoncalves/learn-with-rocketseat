def assistente(pergunta):
    match pergunta.lower():
        case 'variaveis':
            print('Variáveis guardam valores. Exemplo: idade = 18')
        case 'função':
            print('Funções são blocos de código que você pode reutilizar! def nome():')
        case _:
            print(
                'Desculpe ainda encontro-me desvendando esse incrivel mundo da programação')


assistente('python')
