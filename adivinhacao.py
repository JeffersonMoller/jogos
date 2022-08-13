numero_secreto = 42

chute_str = input("Digite o seu numero: ")

chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
    print("Voce acertou!")
else:
    if(maior):
        print("Voce errou! seu chute foi maior do que o numero secreto.")
    elif(menor):
        print("Voce errou! seu chute foi menor do que o numero secreto.")

print("Fim Jogo")

