print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("você digitou: ", chute_str)
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print("Você deve digitar um numero entre 1 e 100!")
        continue  # Volta para proxima interação

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Voce acertou!")
        break
    else:
        if maior:
            print("Voce errou! seu chute foi maior do que o numero secreto.")
        elif menor:
            print("Voce errou! seu chute foi menor do que o numero secreto.")

    print("Fim Jogo")

    # for rodada in range(1, 10): vai de 1 até 9
    # for rodada in range(1, 10, 2): vai de 1 até 9 pulando de 2 em 2..
    # for rodada in [1, 2, 3, 4, 5]: vai de 1 até 5