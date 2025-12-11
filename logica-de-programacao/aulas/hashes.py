nomes = [
    'Afonso',
    'Toin',
    'Belchior',
    'Matheus',
    'Leandro',
    'Adão',
    'José'
]

tabela = {}

for nome in nomes:
    qtd = nome[0]
    if qtd not in tabela:
        tabela[qtd] = []
    tabela[qtd].append(nome)

print(tabela)