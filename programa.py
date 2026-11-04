frota = {}
embarcacoes = [['porta-aviões', 4, 1],['navio-tanque', 3, 2],['contratorpedeiro', 2, 3],['submarino', 1, 4]]
for embarcacao in embarcacoes:
    nome = embarcacao[0]
    tamanho = embarcacao[1]
    quantidade = embarcacao[2]
    for i in range(quantidade):
        print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')
        valida = False
        while not valida:
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
print(frota)
