# exercicio-1:

class minhaexecao(Exception):
    pass
try:
    dadoUsuario = int(input("Digite um número inteiro: "))
    numero = dadoUsuario % 2

    if numero != 0:
        raise minhaexecao('O numero dever ser par!')
except minhaexecao as e:
    print(e)

