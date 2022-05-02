def insereFilaC(F, S):
    global inicioC, fimC
    if ((fimC + 1) % 10 == inicioC):
        return False

    fimC = (fimC+1) % 10
    F[fimC] = S
    return True

def insereFilaP(F, S):
    global inicioP, fimP
    if ((fimP + 1) % 10 == inicioP):
        return False

    fimP = (fimP+1) % 10
    F[fimP] = S
    return True

def primeiro(F, i):
    return F[(i+1) % 10]

def removeFilaC():
    global inicioC
    inicioC = (inicioC + 1) % 10

def removeFilaP():
    global inicioP
    inicioP = (inicioP + 1) % 10


def imprimir(F, i, f):
    ini = i
    while True:
        ini = (ini+1) % 10
        print(F[ini], " ", end='')
        if ini == f:
            break

filaC = [0] * 10
inicioC = 0
fimC = 0
senhaC = 100

filaP = [0] * 10
inicioP = 0
fimP = 0
senhaP = 1000

c = 2

while True:
    print('\n1- Inserir na fila'
          '\n2- Remover da fila'
          '\n3- Mostrar a fila'
          '\n0- Sair')

    op = int(input('Escolha uma opção: '))

    if op == 0:
        break
    elif op == 1:
        print('\nDeseja inserir em qual fila? \n1- Convencional\n2- Prioritária')
        op2 = int(input('Digite "1" para convencional e "2" para prioritária: '))

        if op2 == 1:
            if insereFilaC(filaC, senhaC):
                print('\nInserção realizada com sucesso.')
                senhaC += 1
            else:
                print('\nFila cheia.')

        elif op2 == 2:
            if insereFilaP(filaP, senhaP):
                print('\nInserção realizada com sucesso.')
                senhaP += 1
            else:
                print('\nFila Cheia.')

    elif op == 2:

        if inicioP != fimP and c > 0:
            print(f'\nChamando senha Prioritária: {primeiro(filaP, inicioP)}')
            removeFilaP()
            c -= 1

        else:
            if inicioC != fimC:
                print(f'\nChamando senha Convencional: {primeiro(filaC, inicioC)}')
                removeFilaC()
                c += 2

            else:
                print('\nFila vazia.')

    elif op == 3:
        print('\nDeseja mostrar qual fila? \n1- Convencional\n2- Prioritária')
        op3 = int(input('Digite "1" para convencional e "2" para prioritária: '))

        if op3 == 1:
            if inicioC != fimC:
                print('\nFila Convencional: ')
                imprimir(filaC, inicioC, fimC)
            else:
                print('\nFila vazia.')

        elif op3 == 2:
            if inicioP != fimP:
                print('\nFila Prioritária: ')
                imprimir(filaP, inicioP, fimP)
            else:
                print('\nFila vazia.')

