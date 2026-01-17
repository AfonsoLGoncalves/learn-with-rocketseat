qtde_numeros = 1
maior_numero = None
numero_informado = int(input('Digite um número: '))
maior_numero = numero_informado

while qtde_numeros != 5:
    numero_informado = int(input('Digite um número: '))
    if numero_informado > maior_numero:
        maior_numero = numero_informado
        qtde_numeros += 1
print(f'O maior número informado foi o {maior_numero}')
