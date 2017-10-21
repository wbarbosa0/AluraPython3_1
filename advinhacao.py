print("*************************************")
print("* Bem vindo ao jogo de Adivinhação! *")
print("*************************************")

numero_secreto = 42
total_de_tentativas = 3
#rodada_atual = 1

#while (rodada_atual <= total_de_tentativas):
for rodada_atual in range(1, total_de_tentativas+1):
    print("Tentativa {} de {}".format(rodada_atual, total_de_tentativas))
    chute_str = input("Digite seu palpite")
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Asertô, mizerávi!")
    elif(maior):
        print("Errôu! O numero é maior!")
    elif(menor):
        print("Errôu! O numero é menor!")
    rodada_atual=rodada_atual+1

print("Fim de jogo!")