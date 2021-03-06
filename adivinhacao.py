import random

def jogar():

    print("**********************************")
    print("bem vindo no jogo de Adivinhação!!")
    print("**********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")

        print("você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("você deve digitar um número de 1 a 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("O seu chute foi maior que o número secreto")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    continuar = int(input("Deseja jogar novamente? (Digite 1 para SIM ou 0 para NÂO) "))
    if (continuar == 1):
        jogar()
    else:
        print("Jogo encerrado")

    print("FIM")

if (__name__ == "__main__"):
    jogar()