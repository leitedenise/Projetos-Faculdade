class No:    #Criação do no, desta vez com o valor e direita e esquerda, e não mais só próximo.
    def __init__(self, val):
        self.esq = None
        self.info = val
        self.dir = None

    def getEsq(self):
        return self.esq

    def getInfo(self):
        return self.info

    def getDir(self):
        return self.dir

    def setEsq(self, x):
        self.esq = x

    def setInfo(self, x):
        self.info = x

    def setDir(self, x):
        self.dir = x

class LDE:                  #Criação da classe da lista.
    def __init__(self):
        self.inicio = None #o início começa con none
        self.fim = None    #e o final tbm

    def insereInicio(self, val): #para inserir no início
        p = No(val)    # aloca um no com o valor que deseja inserir
        p.setEsq(None)   #a esquerda do valor será none
        p.setDir(self.inicio)    #a direita do valor será o início, definindo assim que será inserido antes do inicio, como primeiro valor

        if self.inicio == None:  #se o inicio for none, o fim será o 'p' (valor a inserir)
            self.fim = p

        else:
            self.inicio.setEsq(p)  #se não for, se tiver valor no inicio, o 'p'(valor a inserir), será inserido à esquerda do inicio, e o inicio passa a ser esse valor
        self.inicio = p

    def insereFim(self, val):
        p = No(val) #aloca o no com o valor a inserir
        p.setDir(None) #Como vai inserir por último, o lado direito de 'p' será none
        p.setEsq(self.fim) #a esquerda do valor será o fim, pq ele será inserido depois do último valor, passando ele a ser o último.

        if self.inicio == None: #se a lista estiver vazia.
            self.inicio = p    #o primeiro valor será o valor de 'p', o no alocado ficará em primeiro
        else:
            self.fim.setDir(p)  #se ja houver valores, troca o lado direito do fim pelo valor de 'p'
        self.fim = p   #e o 'p' passa a ser o fim

    def insereDepoisValor(self, r, val):
        p = No(val)     #Aloca o no
        q = r.getDir()  #coloca um 'q' na direita do valor a que se vai adicionar depois dele
        r.setDir(p)     #troca a direita dele pelo 'p' (valor) alocado no no
        q.setEsq(p)     #troca a esquerda do 'q' pelo 'p'(valor alocado)
        p.setEsq(r)     #troca a direita do 'p' (valor alocado) pelo 'r'(valor a qual iria adicionar depois dele)
        p.setDir(q)     #troca a direita do 'p' pelo 'q' (valor que estava depois de 'r' e  que agora ficou depois de 'p', pois 'p' foi adicionado depois do 'r'

    def insereAntesValor(self, r, val):
        p = No(val)      #aloca o no com o valor a adicionar
        q = r.getEsq()   #coloca um 'q' à esquerda do valor a que se adicionará antes dele
        r.setEsq(p)      #troca a esquerda desse valor pelo valor de 'p'(que foi alocado)
        q.setDir(p)      #troca a direita de 'q' que estava antes do 'r' por 'p'
        p.setEsq(q)      #troca a esquerda de 'p'(valor alocado) por 'q'
        p.setDir(r)      #troca a direita do 'p' por 'r', adicionando assim ele antes do 'r'

    def removeInicio(self):
        if self.inicio.getDir() == None: #se o direito de inicio for None significa que só tem um valor na lista
            self.inicio = None  #ai o inicio e o fim voltam a valer None, removendo o único valor da lista
            self.Fim = None

        else:   #se houver mais valores
            self.inicio = self.inicio.getDir()  #o início recebe o direito do inicio

    def removeFim(self):
        if self.inicio.getDir() == None:
            self.inicio = None
            self.Fim = None

        else:
            p = self.fim.getEsq() #coloca-se o 'p' no anterior do fim
            p.setDir(None) #troca o direito pelo None
            self.fim = p  #o fim passa a ser 'p'

    def removeValor(self, r):
        if self.inicio.getDir() == None:
            self.inicio = None
            self.fim = None

        else:
            q = r.getEsq()   #coloca-se um 'q' à esquerda do valor a remover
            p = r.getDir()   #coloca-se um 'p' à direita do valor a remover
            q.setDir(p)      #troca a direita de 'q' por 'p'
            p.setEsq(q)      #troca a esquerda de 'p' por 'q', removendo assim o valor entre eles

    def transfereInicio(self):
        p = self.inicio   #coloca-se um 'p' no inicio
        q = self.fim      #coloca-se um 'q' no fim
        r = self.inicio.getDir()   #coloca-se um 'r' na direita do inicio
        q.setDir(p)       #troca a direita de 'q' (fim) pelo 'p' (inicio)
        p.setEsq(q)       #troca a esquerda de 'p' (inicio) pelo 'q' (fim)
        self.inicio = r   #o inicio passa a ser o 'r' (valor que era a direita do inicio)
        self.fim = p
        r.setEsq(None)    #troca a esquerda de 'r' por none (agora ele é o inicio)
        p.setDir(None)    #troca a direita de 'p' por none (agora 'p', que era o inicio, é o fim)

    def consulta(self, val):
        p = self.inicio #coloca-se o 'p' no inicio
        while p != None and p.getInfo() != val: #anda pela lista até que o 'p' não seja o último e o 'p' não seja o valor a procurar
            p = p.getDir() #vai passando o 'p' pra direita, pro próximo para percorrer a lista

        return p


    def imprime(self):
        p = self.inicio #coloca o 'p' no inicio para printar do começo da lista
        print(f"\nNone", end= '') #printa none antes pra indicar que à esquerda não tem ninguém
        while p != None:    #anda enquanto o 'p' tiver valor
            print(f"<--{p.getInfo()} -->", end='') #printa o valor
            p = p.getDir()   #vai passando o 'p' pra direita pra andar pro próximo valor
        print("None\n")   #printa none de novo pra finalizar, onde não teria mais valor seria none


L = LDE()
while True:
    print('''\n1- Inserir no início
2- Inserir no fim
3- Imprimir a lista
4- Remover no início
5- Remover no fim
6- Consultar um valor na lista
7- Remover um valor da lista
8- Inserir depois de um valor
9- Inserir antes de um valor
10-Transferir o valor do início para o fim
0- Sair do programa''')

    op = int(input('\nInforme a opção desejada: '))

    if op == 0:
        break

    elif op == 1:
        val = int(input('\nDigite o valor a inserir: '))

        L.insereInicio(val)
        print('\nValor inserido no início da lista.')

    elif op == 2:
        val = int(input('\nDigite o valor a inserir: '))

        L.insereFim(val)
        print('\nValor inserido ao final da lista.')

    elif op == 3:
        if L.inicio == None:   #se o inicio for none a lista não tem valores
            print('\nLista Vazia!')

        else:
            print('\nLista: ')
            L.imprime()

    elif op == 4:
        if L.inicio == None:
            print('\nLista Vazia!')

        else:
            print(f'\nValor removido do início da lista: {L.inicio.getInfo()} ')
            L.removeInicio()

    elif op == 5:
        if L.inicio == None:
            print('\nLista Vazia!')

        else:
            print(f'\nValor removido do final da lista: {L.fim.getInfo()} ')
            L.removeFim()

    elif op == 6:
        val = int(input('\nDigite o valor a procurar na lista: '))
        r = L.consulta(val)

        if r == None: #se 'r' for none o valor nao foi encontrado na lista
            print('\nValor não encontrado na lista.')

        else:
            print(f'\nValor encontrado: {r.getInfo()}')

    elif op == 7:
        val = int(input('\nDigite o valor a remover da lista: '))
        r = L.consulta(val)

        if r == None:
            print('\nValor não encontrado.')

        else:
            if r == L.inicio:
                L.removeInicio()
                print(f'\nValor removido: {r.getInfo()}')

            elif r == L.fim:
                L.removeFim()
                print(f'\nValor removido: {r.getInfo()}')

            else:
                L.removeValor(r)
                print(f'\nValor removido: {r.getInfo()}')

    elif op == 8:
        val = int(input('\nDigite o valor a procurar na lista: '))
        r = L.consulta(val)

        if r == None:
            print('\nValor não encontrado.')

        else:
            val = int(input('\nDigite o valor a inserir: '))

            if r == L.fim:
                L.insereFim(val)
                print(f'\nValor Inserido com sucesso.')

            else:
                L.insereDepoisValor(r, val)
                print(f'\nValor inserido com sucesso.')

    elif op == 9:
        val = int(input('\nDigite o valor a procurar na lista: '))
        r = L.consulta(val)

        if r == None:
            print('\nValor não encontrado.')

        else:
            val = int(input('\nDigite o valor a inserir: '))

            if r == L.inicio:
                L.insereInicio(val)
                print(f'\nValor Inserido com sucesso.')

            else:
                L.insereAntesValor(r, val)
                print(f'\nValor inserido com sucesso.')

    elif op == 10:
        if L.inicio.getDir() != None:  #se a direita do inicio for none só tem um valor na lista, se não, tem outro(s)

            L.transfereInicio()
            print('\nValor do início adicionado ao fim.')










