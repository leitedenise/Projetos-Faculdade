class No:
    def __init__(self, val):
        self.esq = None
        self.info = val
        self.dir = None

    def getEsq(self):
        return self.esq

    def getDir(self):
        return self.dir

    def getInfo(self):
        return self.info

    def setEsq(self, x):
        self.esq = x

    def setDir(self, x):
        self.dir = x

    def setInfor(self, x):
        self.info = x

def APB(n):
    if n == 0:
        r = None
    else:
        val = int(input("Digite o valor a inserir: "))
        r = No(val)
        r.setEsq(APB(n//2))
        r.setDir(APB(n-n//2-1))

    return r

def Imprime(Raiz):
    if Raiz != None:
        Imprime(Raiz.getEsq())
        print(Raiz.getInfo(), "", end=' ')
        Imprime(Raiz.getDir())

def ImprimeFolhas(Raiz):
    if Raiz != None:
        ImprimeFolhas(Raiz.getEsq())
        if Raiz.getEsq() == None and Raiz.getDir() == None:
           print(Raiz.getInfo(), "", end=' ')
        ImprimeFolhas(Raiz.getDir())

while True:
    print("\n1- Criar Árvore Balanceada"
          "\n2- Imprimir a Árvore"
          "\n3- Imprimir somente as folhas"
          "\n0- Sair do programa")

    op = int(input("\nDigite a opção: "))

    if op == 0:
        break

    elif op == 1:
        Raiz = None
        n = int(input("Digite a quantidade de nós: "))

        Raiz = APB(n)

    elif op == 2:
        if Raiz == None:
            print("\nÁrvore vazia.")

        else:
            print("\nÁrvore: ")
            Imprime(Raiz)

    elif op == 3:
        if Raiz == None:
            print("\nÁrvore vazia.")

        else:
            print("\nFolhas: ")
            ImprimeFolhas(Raiz)






