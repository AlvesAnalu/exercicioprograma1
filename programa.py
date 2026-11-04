from funcoes import (posicao_valida,preenche_frota,posiciona_frota,faz_jogada,afundados)

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += ' ______________________________      ______________________________\n'
    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0'for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|   {linha}| {oponente_info}|\n'
    return texto
    
frota = {}
embarcacoes = [['porta-aviões', 4, 1],['navio-tanque', 3, 2],['contratorpedeiro', 2, 3],['submarino', 1, 4]]
for embarcacao in embarcacoes:
    nome = embarcacao[0]
    tamanho = embarcacao[1]
    quantidade = embarcacao[2]
    for i in range(quantidade):
        valida = False
        while not valida:
            print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            if tamanho > 1:
                escolha = int(input('[1] Vertical [2] Horizontal >'))
                if escolha == 1:
                    orientacao = 'vertical'
                else:
                    orientacao = 'horizontal'
            else:
                orientacao = 'vertical'
            valida = posicao_valida(frota, linha, coluna, orientacao, tamanho)
            if not valida:
                print('Esta posição não está válida!')
        frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
        
frota_oponente = {'porta-aviões': [[[9, 1], [9, 2], [9, 3], [9, 4]]],'navio-tanque': [[[6, 0], [6, 1], [6, 2]],[[4, 3], [5, 3], [6, 3]]],'contratorpedeiro': [[[1, 6], [1, 7]],[[0, 5], [1, 5]],[[3, 6], [3, 7]]],'submarino': [[[2, 7]],[[0, 6]],[[9, 7]],[[7, 6]]]}
tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)
jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    jogada_valida = False
    while not jogada_valida:
        linha = int(input('Linha: '))
        while linha < 0 or linha > 9:
            print('Linha inválida!')
            linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        while coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            coluna = int(input('Coluna: '))
        if tabuleiro_oponente[linha][coluna] in ['X', '-']:
            print(f'A posição linha {linha} e coluna {coluna} ''já foi informada anteriormente!')
        else:
            jogada_valida = True
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)
    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
