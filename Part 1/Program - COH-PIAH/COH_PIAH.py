# Similaridades entre textos - Caso COH-PIAH
# Andre Pinto
# February, 2020
# Introdução à Ciência da Computação com Python Parte 1 @Coursera


import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +
                      " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    sum_tracos = 0

    for i in range(5):
        sum_tracos += (abs(as_a[i] - as_b[i]))

    similaridade = sum_tracos / 6

    return similaridade


def calcula_assinatura(texto):
    # Tamanho médio de palavra: Média simples do número de caracteres por palavra.
    total_letras = 0
    total_palavras = 0
    total_frases = 0
    total_sentencas = 0
    total_caract_sentenc = 0
    total_caract_frase = 0
    lista_palavras = []

    for sentenca in separa_sentencas(texto):
        total_sentencas += 1
        total_caract_sentenc += len(sentenca)
        for frase in separa_frases(sentenca):
            total_frases += 1
            total_caract_frase += len(frase)
            for palavra in separa_palavras(frase):
                lista_palavras.append(palavra)
                total_palavras += 1
    for palavra in lista_palavras:
        total_letras += len(palavra)

    wal = total_letras / len(lista_palavras)

    # Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
    ttr = n_palavras_diferentes(lista_palavras) / total_palavras

    # Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras.
    hlr = n_palavras_unicas(lista_palavras) / total_palavras

    # Tamanho médio de sentença: Média simples do número de caracteres por sentença.
    sal = total_caract_sentenc / total_sentencas

    # Complexidade de sentença: Média simples do número de frases por sentença.
    sac = total_frases / total_sentencas

    # Tamanho médio de frase: Média simples do número de caracteres por frase.
    pal = total_caract_frase / total_frases

    return [wal, ttr, hlr, sal, sac, pal]


def avalia_textos(textos, ass_cp):
    assinaturas = []
    comparacoes = []

    for texto in textos:
        assinaturas.append(calcula_assinatura(texto))

    for assinatura in assinaturas:
        comparacoes.append(compara_assinatura(assinatura, ass_cp))

    ranking = sorted(comparacoes)
    print(comparacoes)

    return comparacoes.index(ranking[0]) + 2
