funcionarios = []
def veriifivadorA (dado):
    valorA = dado
    while True:
        verificar = False
        if (valorA == 'G' or valorA == 'O'):
            verificar = True
        else:
            valorA = input('Informe o cargo (G = Gerente e O = Operário): ').upper()
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

def iserirDados():
    funcionario = []
    funcionario.insert(0, 'Preencimento')
    funcionario.insert(1, float(input('Informe o Horário: ')))
    funcionario.insert(2, verificador(input('Informe o turno (M = Matutino, V = Vespertino e N = Noturno): ').upper()))
    funcionario.insert(3, veriifivadorA(input('Informe o cargo (G = Gerente e O = Operário): ').upper()))
    return funcionario

def horaExtra(dados):
    salarioBase = 1320
    salario = 0
    if (dados[3] == 'G' and dados[2] == 'N'):
        salario = salarioBase + (((10 * salarioBase)/100)*dados[1])
    elif (dados[3] == 'G' and (dados[2] == 'M' or dados[2] == 'V')):
        salario = salarioBase + (((15 * salarioBase) / 100)*dados[1])
    elif (dados[3] == 'O' and dados[2] == 'N'):
        salario = salarioBase + (((9 * salarioBase)/100)*dados[1])
    elif (dados[3] == 'O' and (dados[2] == 'M' or dados[2] == 'V')):
        salario = salarioBase + (((14 * salarioBase) / 100)*dados[1])
    return salario
i = 0
def printE(dados, dado):
    for i in range(0, len(dados)):
        print(f"Nome: {dados}")
        print(f'Salario: {dado}')
        i=+1

nome = []
resp = ""
while True:

    if (resp == ""):
        nome.append(input('Informe o nome: '))
        dados = horaExtra(iserirDados())
        funcionarios.append(dados)
        resp = input('Deseja continuar [Enter P/Sim] [Digite qualquer coisa para não!]')
    else:
        break
print(printE(nome, funcionarios))












