def nome(argumento_posicional, *pacote_de_argumentos):
    print(argumento_posicional,
          pacote_de_argumentos)


def nome_2(argumento_nomeado='Não detenho nada!', **pacote_nomeado):

    print(argumento_nomeado,
          pacote_nomeado
          )
