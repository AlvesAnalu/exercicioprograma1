def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == 'horizontal':
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    elif orientacao == 'vertical':
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    return posicoes

def preenche_frota(frota, nome_do_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_do_navio not in frota:
        frota[nome_do_navio] = []
    frota[nome_do_navio].append(posicoes)
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
    
def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        linha = [0] * 10
        tabuleiro.append(linha)
    for nome_do_navio in frota:
        for navio in frota[nome_do_navio]:
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1
    return tabuleiro

def afundados(frota, tabuleiro):
    contagem= 0
    for nome_do_navio in frota:
        for navio in frota[nome_do_navio]:
            acertos= 0
            for posicao in navio:
                linha= posicao[0]
                coluna= posicao[1]
                if tabuleiro[linha][coluna] == 'X':
                    acertos+= 1
            if acertos == len(navio):
                contagem+= 1
    return contagem

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes= define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in posicoes:
        linha_atual= posicao[0]
        coluna_atual= posicao[1]
        if linha_atual<0 or linha_atual>=10:
            return False
        for nome_navio in frota:
           for navio in frota[nome_navio]:
               if posicao in navio:
                   return False
    return True


