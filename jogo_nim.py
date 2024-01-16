def partida(ptsComputador, ptsUsuario, rodada):

    if rodada >= 1:
        print("** Rodada " + str(rodada) + " **")
    
    n = int(input("Quantas peças totais? "))
    m = int(input("Qual é o limite de peças por jogada? "))


    if n % (m+1) == 0:
        print("Você começa!\n")
        if rodada >= 1:
            ptsUsuario += usuario_escolhe_jogada(n, m, rodada) 
        else:
            usuario_escolhe_jogada(n, m, rodada)
    else:
        print("Computador começa!\n")
        if rodada >= 1:
            ptsComputador += computador_escolhe_jogada(n, m, rodada)
        else:
            ptsComputador += computador_escolhe_jogada(n, m, rodada)
    
    return(ptsComputador, ptsUsuario)
    

def computador_escolhe_jogada(n, m, rodada):
    podeJogar = False
    jogada = m

    while not podeJogar:
        if n-jogada >= 0 and (n-jogada) % (m+1) == 0:
            podeJogar = True
        elif jogada > 0:
            jogada -= 1
        else: 
            jogada = m
            podeJogar = True
    
    if jogada == 1:
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou " + str(jogada) + " peças.")

    n -= jogada

    if n == 0:
        print("O computador ganhou!\n")
        return 1
    else:
        quantidadePecas(n)
        usuario_escolhe_jogada(n, m, rodada)
        

def usuario_escolhe_jogada(n, m, rodada):

    eValida = False
    while not eValida:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada <= m and jogada > 0:
            eValida = True
        else:
            print("Ops! Jogada inválida, tente novamente!")

    if jogada == 1:
        print("Você tirou uma peça.")
    else:
        print("Você tirou " + str(jogada) + " peças.")

    n -= jogada

    if n == 0:
        print("Você ganhou!\n")
        return 1
    else:
        quantidadePecas(n)
        computador_escolhe_jogada(n, m, rodada)

def quantidadePecas(n):
    if n == 1:
        print("Agora resta apenas uma peça no tabuleiro.\n")
    else:
        print("Agora restam " + str(n) + " peças no tabuleiro.\n")
    

def menu():
    print("\n      | BOAS-VINDAS AO NIM! |")
    print("\n                MENU:")
    print("1 - para jogar uma partidade isolada")
    print("2- Para jogar um campeonato")
    escolha = int(input())
    print("\n")
    ptsComputador = int(0)
    ptsUsuario = int(0)
    

    if escolha == 1:
        print("Você escolheu a partida única. Boa sorte!\n")
        partida(0, 0, 0)
    else:
        print("Você escolheu melhor de três. Boa sorte!\n")
        rodada = 1
        while rodada <= 3:
            ptsComputador, ptsUsuario = partida(ptsComputador, ptsUsuario, rodada)
            rodada += 1

        print("Final do campeonato!")
        print("Placar: Você " + str(ptsUsuario) + " X " + str(ptsComputador) + " Computador")
        

menu()

