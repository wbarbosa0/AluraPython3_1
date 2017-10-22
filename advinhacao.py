import random

print("*************************************")
print("* Bem vindo ao jogo de Adivinhação! *")
print("*************************************")


#numero_secreto = 42
#numero_secreto = int(random.random()*100+1)
numero_secreto = random.randrange(1,101)
#total_de_tentativas = 3
#rodada_atual = 1
pontos = 1000
total_de_tentativas = 0

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

#while (rodada_atual <= total_de_tentativas):
for rodada_atual in range(1, total_de_tentativas+1):
    print("Tentativa {} de {}".format(rodada_atual, total_de_tentativas))
    chute_str = input("Digite seu palpite entre 1 e 100: ")
    print("Você digitou {}".format(chute_str))
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print("Os palpites devem ser entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Asertô, mizerávi! Toma {} pontos".format(pontos))
        break
    else:
        if(maior):
            print("Errôu! O palpite é maior!")
        elif(menor):
            print("Errôu! O palpite é menor!")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
    rodada_atual=rodada_atual+1

print("Fim de jogo! O número era {}.".format(numero_secreto))