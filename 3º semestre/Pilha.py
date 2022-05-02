def Push(P, V):
    P.append(V)

def Topo(P):
    return P[len(P)-1]

def Pop(P):
    #P.remove(valor) --> remove o valor passado por parâmetro.
    P.pop() #remove o último valor da lista, por padrão, sem precisar passar parâmetro.

def Imprime(P):
    print('\nPilha:')
    for i in range(len(P)-1, -1, -1):
        print(f'[ {P[i]} ]')

def Converter(P, valor):
    while valor > 0:
        resto = valor % 2
        Push(P, resto)
        valor //= 2

    bin = 0
    while len(P) > 0:
        bin = (bin * 10) + Topo(P)
        Pop(P)

    return bin

def PilhaOrdenada(P, valor):

    aux = []
    while len(P) > 0 and valor > Topo(P):
        Push(aux, Topo(P))
        Pop(P)
    Push(P, valor)

    while len(aux) > 0:
        Push(P, Topo(aux))
        Pop(aux)

def Esvaziar(P):
    print('Sequência ordenada:')
    while len(P) > 0:
        print(Topo(P))
        Pop(P)

#Criando pilha vazia
pilha = []

while True:
    print('\n1- Inserir valor na pilha')
    print('2- Remover valor da pilha')
    print('3- Imprimir a pilha')
    print('4- Converter decimal para binário')
    print('5- Ordenar pilha')

    print('0- Sair do programa')
    op = int(input('Digite a opção: '))

    if op == 0:
        break

    elif op == 1:
        valor = int(input('Digite o valor a ser inserido na pilha: '))
        Push(pilha, valor)

    elif op == 2:
        if len(pilha) == 0:
            print('\nPilha vazia!')

        else:
            valor = Topo(pilha)
            print(f'Valor {valor} removido.')
            Pop(pilha)

    elif op == 3:
        if len(pilha) == 0:
            print('\nPilha vazia!')
        else:
            Imprime(pilha)

    elif op == 4:
        val = int(input('Digite o valor a converter: '))
        bin = Converter(pilha, val)

        print(f'\nValor convertido em binário: {bin}')

    elif op == 5:
        while True:
            val = int(input('Digite um valor ou "0" para sair: '))
            if val == 0:
                break
            else:
                PilhaOrdenada(pilha, val)

        Esvaziar(pilha)