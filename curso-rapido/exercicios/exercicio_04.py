# Necessário realizar a conversão devido todo input ser por natureza um string
primeiro_numero = int(input('Digite um número inteiro: '))
segundo_numero = int(input('Digite um segundo número inteiro: '))
terceiro_numero = float(input('Digite um terceiro número float: '))

primeiro_resultado = (primeiro_numero * 2) + (segundo_numero / 2)
segundo_resultado = (primeiro_numero * 3) + terceiro_numero
terceiro_resultado = terceiro_numero ** 3

print(
    f'O produto do dobro do primeiro com metade do segundo: {primeiro_resultado};\nA soma do triplo do primeiro com o terceiro: {segundo_resultado};\nO terceiro elevado ao cubo: {terceiro_resultado}'
)
