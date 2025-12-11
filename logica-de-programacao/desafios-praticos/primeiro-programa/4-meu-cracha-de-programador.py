campos = ['Nome', 'Idade', 'Linguagem favorita', 'Emoji']
cracha = {}

for campo in campos:
    cracha[campo] = input(f'Digite seu {campo.lower()}: ')

print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
print('👩‍💻 Crachá do Dev')
for campo, informacao in cracha.items():
    print(f'{campo} : {informacao}')
print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
