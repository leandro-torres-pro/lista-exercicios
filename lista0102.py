def veriifivadorA (dado):
    valorA = dado
    while True:
        verificar = False
        if (valorA == 'A' or valorA == 'B' or valorA == 'C'):
            verificar = True
        else:
            valorA = input("ERRO! Informe elevador(A - B - C)").upper()
        if verificar:
            break
    return valorA

def verificador(dado):
    valor = dado
    while True:
        verificar = False
        if (valor == 'G' or valor == 'M' or valor == 'V' )  :
            verificar = True
        else:
            valor = input('ERRO!! Informe o turno (M = Matutino, V = Vespertino e N = Noturno): ').upper()
        if verificar:
            break
    return valor


def seleções():
    selecão = []
    elevador = veriifivadorA(input("Informe elevador(A - B - C)").upper())
    turno = verificador(input('Informe o turno (M = Matutino, V = Vespertino e N = Noturno): ').upper())

    selecão.insert(0, elevador)
    selecão.insert(1, turno)
    return selecão

def contador(dados, elevador):
    quantidades = 0
    for i in range(len(dados)):
        for x in range(len(dados[i])):
            if dados[i][x] in elevador:
                quantidades =+ 1

    return quantidades

dados = []
resp = ""
while True:

    if (resp == ""):
        dados.append(seleções())
        resp = input('Deseja continuar [Enter P/Sim] [Digite qualquer coisa para não!]')
    else:
        break

def printElevador(dados):
    quantA = 0
    quantB = 0
    quantC = 0
    usoElevadores = []
    for i in range(len(dados)):
        for ii in range(len(dados[i])):
            if dados[i][ii] == 'A':
                quantA = quantA + 1
            elif dados[i][ii] == 'B':
                quantB =  quantB + 1
            elif dados[i][ii] == 'C':
                quantC = quantC + 1
    usoElevadores.insert(0, quantA)
    usoElevadores.insert(1, quantB)
    usoElevadores.insert(2, quantC)
    return usoElevadores
def printTurno(dados):
    quantM = 0
    quantV = 0
    quantN = 0
    turnos = []
    for i in range(len(dados)):
        for ii in range(1, len(dados[i])):
            if dados[i][ii] == 'M':
                quantM = quantM + 1
            elif dados[i][ii] == 'V':
                quantV =  quantV + 1
            elif dados[i][ii] == 'N':
                quantN = quantN + 1
    turnos.insert(0, quantM)
    turnos.insert(1, quantV)
    turnos.insert(2, quantN)
    return turnos
def calculador(dadoMaior, dadoMenor):
    porcentagem = (((dadoMaior-dadoMenor)*100)/(dadoMaior+dadoMenor))
    if porcentagem == 0:
        porcentagem = 50
    return porcentagem

def analise(dados1, dados2):
    dadosGerais = []
    mais = 0
    menos = 0
    for i in range(len(dados1)):
        if dados1[i] >= mais:
            mais = dados1[i]
        elif dados1[i] <= mais:
            menos = dados1[i]

    for i in range(len(dados1)):
        if (i == 0) and (mais == dados1[i]):
            usoMaiorElevador = 'A'
        elif (i == 1) and (mais == dados1[i]):
            usoMaiorElevador = 'B'
        elif (i == 2) and (mais == dados1[i]):
            usoMaiorElevador = 'C'

    for i in range(len(dados1)):
        if (i == 0) and (menos == dados1[i]):
            usoMenorElevador = 'A'
        elif (i == 1) and (menos == dados1[i]):
            usoMenorElevador = 'B'
        elif (i == 2) and (menos == dados1[i]):
            usoMenorElevador = 'C'
    maisUso = 0
    menosUso = 1
    maisTurno = 0
    menosTurno = 0
    for i in range(len(dados2)):
        if dados2[i] >= maisTurno:
            maisTurno = dados2[i]
        elif dados2[i] <= maisTurno:
            menosTurno = dados2[i]
    for i in range(len(dados2)):
        if (i == 0) and (maisTurno == dados2[i]):
            usoMaiorTurno = 'M'
            maisUso = dados2[i]
        elif (i == 1) and (maisTurno == dados2[i]):
            usoMaiorTurno = 'V'
            maisUso = dados2[i]
        elif (i == 2) and (maisTurno == dados2[i]):
            usoMaiorTurno = 'N'
            maisUso = dados2[i]
    for i in range(len(dados2)):
        if (i == 0) and (menosTurno == dados2[i]):
            usoMenorTurno = 'M'
            menosUso = dados2[i]
        elif (i == 1) and (menosTurno == dados2[i]):
            usoMenorTurno = 'V'
            menosUso = dados2[i]
        elif (i == 2) and (menosTurno == dados2[i]):
            usoMenorTurno = 'N'
            menosUso = dados2[i]
    diferença = calculador(maisUso,menosUso)

    dadosGerais.insert(0, usoMaiorElevador)
    dadosGerais.insert(1, usoMenorElevador)
    dadosGerais.insert(2, usoMaiorTurno)
    dadosGerais.insert(3, usoMenorTurno)
    dadosGerais.insert(4, diferença)

    return dadosGerais

resultado = []
resultado = (analise(printElevador(dados),printTurno(dados)))
print(resultado)
def filtro(dado):

    if dado[2] == 'M':
        turno = "Matutino"
    elif dado[2] == 'V':
        turno = 'Vespertino'
    elif dado[2] == 'N':
        turno = 'Noturno'
    return turno

print(f'O elevador mais utilizado é: "{resultado[0]}" no período  que concentra o maior fluxo é: {filtro(resultado)}')
print(f'Qual o período mais utilizado de todos: {filtro(resultado)}')
print(f'A diferença de porcentual entre o mais usado dos horários e o menos usado é: {resultado[4]}%')