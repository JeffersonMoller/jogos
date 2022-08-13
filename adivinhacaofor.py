numero_secreto = 42
total_de_tentativas = 3


for rodada in range(1, total_de_tentativas + 1):
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

    print("Fim Jogo")

    #for rodada in range(1, 10, 2): vai de 1 até 9 pulando de 2 em 2..
    #for rodada in [1, 2, 3, 4, 5] vai de 1 até 5
