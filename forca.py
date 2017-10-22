import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    palavra_secreta = palavras[random.randrange(0,len(palavras))].upper()
    #palavra_secreta = "banana".upper()
    #letras_acertadas = ['_', '_', '_', '_', '_', '_']
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = []

    print(letras_acertadas)
    while (not acertou and not enforcou):
        chute = input("Qual letra? ").strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[index] = chute
                index += 1
            acertou = not "_" in letras_acertadas
        else:
            erros += chute
            enforcou = len(erros) == 6
        print(letras_acertadas)
        print("Erros: ", erros)

        print("Jogando...")

    print("Fim do jogo")
    if (acertou):
        print("Asertô, mizerávi!")
    else:
        print("Errôu! A palavra era {}", palavra_secreta)


if (__name__ == "__main__"):
    jogar()
