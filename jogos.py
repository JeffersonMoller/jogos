import adivinhacaofor
import forca


def jogar():
    print("Selecione um jogo")
    jogo = int(input("(1) Advinhação (2) Forca: "))

    if jogo == 1:
        adivinhacaofor.jogar()
    elif jogo == 2:
        forca.jogar()


if __name__ == "__main__":
    jogar()
