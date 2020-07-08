# Jogo de NIM
# Andre Pinto
# January 23, 2020
# Introdução à Ciência da Computação com Python Parte 1 @Coursera


def computador_escolhe_jogada(n, m):
    i = 0
    while(i < m):
        jogada_npc = m - i
        vencedora = n - jogada_npc
        if(checa_multiplos(vencedora,m)):
            return jogada_npc
        i += 1
    return m

def usuario_escolhe_jogada(n, m):
    concluido = False
    while not concluido:
        retirar = int(input("Quantas peças você vai tirar?\n"))
        if(retirar > m) or (retirar > n) or (retirar <= 0):
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            concluido = True
            return retirar

def campeonato():
    pontos_jogador = 0
    pontos_npc = 0
    rodada = 1
    print("Voce escolheu um campeonato!")
    while(rodada < 4):
        print("**** Rodada ", rodada, " ****")
        pontos = partida()
        if (pontos == 1):
            pontos_jogador += 1
        else:
            pontos_npc += 1
        rodada += 1
    print("**** Final do campeonato! ****")
    print("Placar: Você ",pontos_jogador," X ",pontos_npc," Computador")

def partida():
    player_comeca = False
    inicio_jogo = False
    qtd_pecas_atual = 0
    qtd_pecas_return = 0
    qtd_pecas = int(input("Quantas peças?\n"))
    limite_pecas = int(input("Limite de peças por jogada?\n"))
    inicio_jogo = True

    qtd_pecas_atual = qtd_pecas
    if (checa_multiplos(qtd_pecas_atual, limite_pecas)):
        print("Voce começa!")
        player_comeca = True
    else:
        print("Computador começa!")
        player_comeca = False

    #Ciclo de jogo
    while inicio_jogo:
        if player_comeca:
            qtd_pecas_return = usuario_escolhe_jogada(qtd_pecas_atual, limite_pecas)
            print("Você tirou",qtd_pecas_return,plural(qtd_pecas_return))
            player_comeca = False
        else:
            qtd_pecas_return = computador_escolhe_jogada(qtd_pecas_atual, limite_pecas)
            print("O computador tirou",qtd_pecas_return,plural(qtd_pecas_return))
            player_comeca = True

        qtd_pecas_atual = qtd_pecas_atual - qtd_pecas_return

        if qtd_pecas_atual > 0:
            pass
        else:
            inicio_jogo = False
            if not player_comeca:
                print("Você ganhou!")
                return 1
            else:
                print("O computador ganhou!")
                return 0

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    opt = int(input("2 - para jogar um campeonato\n"))
    if opt == 1:
        print("\nVocê escolheu uma partida isolada!\n")
        partida()
    else:
        print("\nVocê escolheu um campeonato!\n")
        campeonato()

def plural(n):
    if n == 1 or n == -1:
        return "peça."
    else:
        return "peças."

def checa_multiplos(n, m):
    if n % (m + 1) == 0:
        return True
    else:
        return False

# COMEÇA O JOGO
main()