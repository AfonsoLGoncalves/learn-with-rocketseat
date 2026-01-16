# Faça um programa que receba uma data de nascimento (15/07/87) e imprima

# 'Você nasceu em ‹dia > de ‹mês> de ‹ano>'

data = input('Digite uma data: ')
resultado = data.split('/')
dia, mes, ano = resultado


print(f'Você nasceu em {dia} de {mes} de {ano}')
