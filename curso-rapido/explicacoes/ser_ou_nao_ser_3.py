carteira = int(input('Quanto eu tenho? '))
tenis = int(input('Quanto custa meu boot no sonhos? '))
necessidade = input(
    'É uma necessidade real esse boot? ou eu to ficando MALUCO? (S/N)').upper()
if carteira >= tenis and necessidade == 'S':
    print('caraca MEOOOO OVO COMPRAR UM TENISAO DA MASSA!')
else:
    print('PO... Vou comprar depois...')
