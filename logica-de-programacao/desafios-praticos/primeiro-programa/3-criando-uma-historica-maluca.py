campos = ['lugar', 'pessoa_famosa', 'objeto', 'numero', 'verbo', 'cor']
respostas = {}

for campo in campos:
    respostas[campo] = input(f'Digite um(a) {campo.replace('_',' ')}: ')

historia = f"""
Em pleno {respostas['lugar']}, um dia completamente normal virou um caos quando {respostas['pessoa_famosa']} apareceu correndo com um(a) {respostas['objeto']} gigante, todo pintado de {respostas['cor']}.
Ninguém entendeu nada, até que ele(a) começou a {respostas['verbo']} como se sua vida dependesse disso — e, sinceramente, parecia mesmo.

De repente, um grupo de {respostas['numero']} turistas sacou os celulares para gravar, achando que era algum tipo de performance artística.
Mas não era.
{respostas['pessoa_famosa']} gritava:
— Não encostem nisso! Ele(a) já está quase tomando consciência própria!

O(a) {respostas['objeto']}, agora brilhando em {respostas['cor']}, começou a vibrar e emitir um som que parecia uma mistura de micro-ondas com uma galinha nervosa.
Os turistas? Aplaudindo.
O pessoal local? Correndo.
E {respostas['pessoa_famosa']}, completamente desesperado(a), só repetia:
— Eu falei que não era pra ter colocado no modo turbo!

No fim, tudo deu certo — ou quase.
O(a) misterioso(a) {respostas['objeto']} acabou fugindo sozinho(a) pela rua, e {respostas['pessoa_famosa']} saiu atrás dele(a) prometendo que, da próxima vez, usaria só a potência mínima.
"""

print(historia)