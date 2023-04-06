
# exercicio-2:
class minhaexecao(Exception):
    pass
try:
    dadoUsuario = input("Digite uma frase: ")

    if not dadoUsuario.isupper():
        raise minhaexecao('O numero dever maiuscula !')
except minhaexecao as e:
    print(e)