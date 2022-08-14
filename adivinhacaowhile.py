import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = round(random.randrange(1, 101))
total_de_tentativas = 0
rodada = 1

print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Define o nível: "))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

while rodada <= total_de_tentativas:
    print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu numero: ")
    print("você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Voce acertou!")
    else:
        if maior:
            print("Voce errou! seu chute foi maior do que o numero secreto.")
        elif menor:
            print("Voce errou! seu chute foi menor do que o numero secreto.")

    rodada = rodada + 1

    print("Fim Jogo")
