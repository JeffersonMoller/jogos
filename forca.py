import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    total_de_erros_permitido = 10

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    erros = 0
    print("A palavra possui {} letras".format(len(palavra_secreta)))
    print(letras_acertadas)

    while True:
        print("{} de {} erros".format(erros, total_de_erros_permitido))
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        if erros == total_de_erros_permitido:
            break
        if "_" not in letras_acertadas:
            break
        print(letras_acertadas)

    if "_" not in letras_acertadas:
        print("Você ganhou!!")
    else:
        print("Você perdeu!! a palavra era {}".format(palavra_secreta))

    print("Fim jogo")


if __name__ == "__main__":
    jogar()
