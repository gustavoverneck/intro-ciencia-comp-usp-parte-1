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
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

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
    s_ab = 0.0
    for i in range(len(as_a)):
        s_ab += abs(as_a[i]-as_b[i])
    return s_ab/6

def calcula_assinatura(texto):
    wal = 0.0# Tamanho médio de palavra
    ttr = 0.0# Relação Type-Token
    hlr = 0.0# Razão Hapax Legomana
    sal = 0.0# Tamanho médio de sentença
    sac = 0.0# Complexidade média da sentença
    pal = 0.0# Tamanho medio de frase
    
    sentencas = separa_sentencas(texto)
    n_sentencas = len(sentencas)
    n_frases = 0
    n_palavras = 0
    todas_palavras = []
    todas_palavras_unicas = []
    for sentenca in sentencas:
        x_sent = sentenca
        if any([' ' in x_sent, ',' in x_sent, '.' in x_sent, ':' in x_sent, '?' in x_sent, "!" in x_sent]):
            x_sent.replace(' ', '')
            x_sent.replace(',', '')
            x_sent.replace('.', '')
            x_sent.replace(':', '')
            x_sent.replace('?', '')
            x_sent.replace('!', '')
            x_sent.replace(";", '')
        sal += len(x_sent)
        frases = separa_frases(sentenca)
        n_frases += len(frases)
        for frase in frases:
            x_frase = frase
            if any([' ' in x_frase, ',' in x_frase, '.' in x_frase, ':' in x_frase, '?' in x_frase, "!" in x_frase]):
                x_frase.replace(' ', '')
                x_frase.replace(',', '')
                x_frase.replace('.', '')
                x_frase.replace(':', '')
                x_frase.replace('?', '')
                x_frase.replace('!', '')
                x_frase.replace(';', '')
            pal += len(x_frase)
            for palavra in separa_palavras(frase):
                n_palavras += 1
                wal += len(palavra)
                todas_palavras.append(palavra)
                if palavra not in todas_palavras_unicas:
                    todas_palavras_unicas.append(palavra)
    ttr = n_palavras_diferentes(todas_palavras)/n_palavras
    hlw = n_palavras_unicas(todas_palavras)/n_palavras_diferentes(todas_palavras)
    wal /= n_palavras   # Tamanho médio de palavra
    pal /= n_frases
    sal /= n_sentencas  # Tamanho médio de Sentença
    sac = n_frases/n_sentencas  # Complexidade de sentença
    hlr = n_palavras_unicas(todas_palavras)/n_palavras

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    resultados = []
    for texto in textos:
        text_ass = calcula_assinatura(texto)
        resultados.append(compara_assinatura(ass_cp, text_ass))
    return resultados.index(min(resultados))+1

if __name__ == '__main__':
    assinatura = le_assinatura()
    textos = le_textos()
    resultado = avalia_textos(textos, assinatura)
    print(f"O autor do texto {resultado} está infectado com COH-PIAH")