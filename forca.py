import random

def jogar():
    banner()

    palavra_secreta = define_palavra_secreta()
    #letras_acertadas = ['_', '_', '_', '_', '_', '_']
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = []

    print(letras_acertadas)
    while (not acertou and not enforcou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            acertou = verificar_acerto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += chute
            desenha_forca(len(erros))
            enforcou = len(erros) == 7
        print(letras_acertadas)
        print("Erros: ", erros)

        print("Jogando...")

    print("Fim do jogo")
    if (acertou):
        mensagem_jogo_ganho()
    else:
        mensagem_jogo_perdido(palavra_secreta)


def mensagem_jogo_perdido(palavra_secreta):
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \        ")
    print("  /                 \       ")
    print("//                   \/\    ")
    print("\|   XXXX     XXXX   | /    ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/      ")
    print("   |\     XXX     /|        ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/        ")
    print("     \_         _/          ")
    print("       \_______/            ")


def mensagem_jogo_ganho():
    print("Asertô, mizerávi!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def pede_chute():
    chute = input("Qual letra? ").strip().upper()
    return chute


def verificar_acerto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = chute
        index += 1
    acertou = not "_" in letras_acertadas
    return acertou


def define_palavra_secreta():
    palavras = []
    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()
    # palavra_secreta = "banana".upper()
    return palavra_secreta


def banner():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


if (__name__ == "__main__"):
    jogar()
