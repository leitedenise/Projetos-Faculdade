def Push(P, V):  # Passa a lista (pilha) e o valor a ser inserido.
    P.append(V)  # E vai dando apende a cda valor que desejar inserir

def Topo(P):     # Passa a lista (pilha) de parametro. O topo é o último valor que foi inserido na pilha
    return P[len(P)-1]   # Para pegar o ultimo valor da pilha pega-se o valor da posição equivalente ao tamanho da lista -1
                         # (que traz os valores de traz pra frente)

def Pop(P):
    #P.remove(valor) --> remove o valor passado por parâmetro.
    P.pop() #remove o último valor da lista, por padrão, sem precisar passar parâmetro.

def Imprime(P):
    print('\nPilha:')
    for i in range(len(P)-1, -1, -1): # Anda pela lista, de traz pra frente, pois na pilha vai se retirando do último valor até chegar no primeiro inserido
        print(f'[ {P[i]} ]')    # E vai printando o valor equivalente àquela posição da pilha

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

def PilhaOrdenada(P, valor):     # Passa a lista (pilha) e o valor a inserir (de forma ordenada)

    aux = []
    while len(P) > 0 and valor > Topo(P):  # repete até que tenha valores na lista e que o valor a inserir seja maior que o último da pilha
        Push(aux, Topo(P))   # Vai pondo na pilha aux o topo da pilha principal (se ele for maior que o valor a inserir)
        Pop(P)              # remove esse valor da pilha principal, e faz isso até quando os proximos valores forem maior que o valor a inserir
    Push(P, valor)         # quando nao for mais, adiciona o valor à pilha

    while len(aux) > 0:      # depois percorre a pilha aux com os valores tirados da principal
        Push(P, Topo(aux))   # adiciona na principal o ultimo valor da aux e remove ele da aux
        Pop(aux)

def Esvaziar(P):         # para esvaziar passa-se a pilha
    print('Sequência ordenada:')
    while len(P) > 0:    # faz-se até que tenha valores
        print(Topo(P))   # vai printando o topo e removendo, até remover todos os valores e esvaziar a pilha
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