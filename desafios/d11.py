import random
tabuleiro = [' ' for _ in range(9)]

def exibir_tabuleiro():
    print('-------------')
    print('|', tabuleiro[0], '|', tabuleiro[1], '|', tabuleiro[2], '|')
    print('-------------')
    print('|', tabuleiro[3], '|', tabuleiro[4], '|', tabuleiro[5], '|')
    print('-------------')
    print('|', tabuleiro[6], '|', tabuleiro[7], '|', tabuleiro[8], '|')
    print('-------------')


def verificar_vencedor(simbolo):
    for i in range(0, 9, 3):
        if tabuleiro[i] == tabuleiro[i + 1] == tabuleiro[i + 2] == simbolo:
            return True
    
    for i in range(3):
        if tabuleiro[i] == tabuleiro[i + 3] == tabuleiro[i + 6] == simbolo:
            return True

    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == simbolo:
        return True
    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == simbolo:
        return True
    
    return False

def pvp():
    jogador = 'X'
    jogadas = 0
    
    while True:
        exibir_tabuleiro()
        escolha = int(input("Escolha uma posição de 1 a 9: ")) - 1
        
        if tabuleiro[escolha] == ' ':
            tabuleiro[escolha] = jogador
            jogadas += 1
            
            if verificar_vencedor(jogador):
                exibir_tabuleiro()
                print("Parabéns! O jogador", jogador, "venceu!")
                break
            
            if jogadas == 9:
                exibir_tabuleiro()
                print("Empate!")
                break
            
            jogador = 'O' if jogador == 'X' else 'X'
        else:
            print("Posição inválida. Tente novamente.")
        
def pve_easy():
    jogador = 'X'
    jogadas = 0

    while True:
        if jogador == 'X':
            exibir_tabuleiro()
            escolha = int(input("Escolha uma posição de 1 a 9: ")) - 1

            if tabuleiro[escolha] == ' ':
                tabuleiro[escolha] = jogador
                jogadas += 1

                if verificar_vencedor(jogador):
                    exibir_tabuleiro()
                    print("Parabéns! Você venceu!")
                    break

                if jogadas == 9:
                    exibir_tabuleiro()
                    print("Empate!")
                    break

                jogador = 'O'
            else:
                print("Posição inválida. Tente novamente.")
#codigo feito por Guilherme
        else:
            
            jogada_maquina = random.choice([i for i, x in enumerate(tabuleiro) if x == ' '])
            tabuleiro[jogada_maquina] = jogador
            jogadas += 1

            if verificar_vencedor(jogador):
                exibir_tabuleiro()
                print("A máquina venceu! Você perdeu!")
                break

            if jogadas == 9:
                exibir_tabuleiro()
                print("Empate!")
                break

            jogador = 'X'

        exibir_tabuleiro()

def jogada_maquina():

    for i in range(9):
        if tabuleiro[i] == ' ':
            tabuleiro[i] = 'O'
            if verificar_vencedor('O'):
                return
            else:
                tabuleiro[i] = ' '  
    
    for i in range(9):
        if tabuleiro[i] == ' ':
            tabuleiro[i] = 'X'
            if verificar_vencedor('X'):
                tabuleiro[i] = 'O'
                return
            else:
                tabuleiro[i] = ' ' 
    
    if tabuleiro[4] == ' ':
        tabuleiro[4] = 'O'
        return
    
    quinas_disponiveis = [0, 2, 6, 8]
    for canto in quinas_disponiveis:
        if tabuleiro[canto] == ' ':
            tabuleiro[canto] = 'O'
            return
    
    # Fazer jogada em qualquer posição vazia
    for i in range(9):
        if tabuleiro[i] == ' ':
            tabuleiro[i] = 'O'
            return

# Função para jogar contra a máquina
def pve_hard():
    jogador = 'X'
    jogadas = 0
    
    while True:
        if jogador == 'X':
            exibir_tabuleiro()
            escolha = int(input("Escolha uma posição de 1 a 9: ")) - 1
            
            if tabuleiro[escolha] == ' ':
                tabuleiro[escolha] = jogador
                jogadas += 1
                
                if verificar_vencedor(jogador):
                    exibir_tabuleiro()
                    print("Parabéns! Você venceu!")
                    break
                
                if jogadas == 9:
                    exibir_tabuleiro()
                    print("Empate!")
                    break
                
                jogador = 'O'
            else:
                print("Posição inválida. Tente novamente.")
        
        else:
            # Vez da máquina
            jogada_maquina()
            jogadas += 1
            
            if verificar_vencedor(jogador):
                exibir_tabuleiro()
                print("A máquina venceu! Você perdeu!")
                break
            
            if jogadas == 9:
                exibir_tabuleiro()
                print("Empate!")
                break
            
            jogador = 'X'
        
        exibir_tabuleiro()

# Iniciar o jogo

option = input(" 1 - PVP \n 2 - PVE \n 3 - HARD PVE \n Insira o modo desejado: ")
if option == "1": 
    pvp()
elif option == "2": 
    pve_easy()
elif option == "3": 
    pve_hard()

# com a ajuda de: alguma dezena de tópicos do stackoverflow 