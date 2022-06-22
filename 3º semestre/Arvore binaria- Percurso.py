class no_arvore:  # criação do no
    def __init__(self, val):
        self.esq = None
        self.info = val
        self.dir = None


def Insere(Raiz, No):  # inserindo valores na arvore
    if Raiz is None:  # se a raiz for nula, ela passa a ser o valor do no
        Raiz = No

    else:
        if (Raiz.info < No.info):  # se a raiz for menor que o no
            if Raiz.dir == None:  # se a direita da raiz for nula, ela passa a ser o no
                Raiz.dir = No
            else:
                Insere(Raiz.dir, No)  # se nao, chama o método de inserir
        else:
            if Raiz.esq == None:  # se a esquerda da raiz for nula, a raiz passa a ser o no
                Raiz.esq = No
            else:
                Insere(Raiz.esq, No)  # se não, chama o método pra achar o local de inserção


# percursos pela arvora:

def pre_order(Raiz):  # percorre passando primeiro pela raiz, depois lado esquerdo e direito por último
    if Raiz != None:
        print(Raiz.info, " ", end='')
        pre_order(Raiz.esq)
        pre_order(Raiz.dir)


def in_order(Raiz):  # percorre passando primeiro pelo lado esquerdo, depois raiz e por último lado direito
    if Raiz != None:
        in_order(Raiz.esq)
        print(Raiz.info, " ", end='')
        in_order(Raiz.dir)


def pos_order(Raiz):  # percorre passando primeiro pelo lado esquerdo, depois direito e por último raiz
    if Raiz != None:
        pos_order(Raiz.esq)
        pos_order(Raiz.dir)
        print(Raiz.info, " ", end='')


def busca(Raiz, val):  # para realizar busca de um valor na árvore
    if Raiz == None:  # se a raiz for nula retorna nulo
        return None
    else:  # se não, testa se a raiz é igual ao valor, ai retorna ela, como o valor encontrado
        if Raiz.info == val:
            return Raiz
        else:  # se não, se a raiz for maior que o valor, busca pela esquerda, passando o lado esquerdo como raiz e o valor a buscar
            if Raiz.info > val:
                return busca(Raiz.esq, val)
            else:
                return busca(Raiz.dir,
                             val)  # se a raiz for menor que o valor, busca pelo lado direito, passando como raiz o lado direito e o valor a buscar


def busca_pai(Raiz, val):  # método para encontrar a raiz do valor (pai)
    if Raiz.esq == val or Raiz.dir == val:  # testa se o lado esquerdo da raiz é o valor ou se o lado direito da raiz é o valor
        return Raiz
    else:
        if val.info > Raiz.info:  # se não, testa se o valor é maior que a raiz, ai busca do lado direito dela
            return busca_pai(Raiz.dir, val)
        else:
            return busca_pai(Raiz.esq, val)  # se nao, se for menor que a raiz, busca do lado esquerdo


# Função para buscar o maior valor à esquerda do no r (3º caso da função remove):

def busca_maior(Raiz):  # A raiz passada é o no à esquerda de r
    if Raiz.dir is not None:   # testa se a direita da raiz não é nula, se não for chama o método novamente passando como raiz esse valor à direita
        busca_maior(Raiz.dir)
        return busca_maior(Raiz.dir)
    else:   # se a direita da raiz for nula, significa que ele é o maior valor à esquerda de r
        return Raiz

def remove(Raiz, r):   # função para remover um no da árvore
    # 1o. caso o nó r é folha, buscar o pai de r, trocar o lado esq ou dir do pai para None
    if r.esq == None and r.dir == None:
        pai = busca_pai(Raiz, r)

        if pai.esq == r:
            pai.esq = None

        else:
            pai.dir = None

    # 2o. caso o nó r possui apenas um filho, buscar o pai de r, trocar o lado esq ou dir do pai com o filho de r
    elif r.dir is None and r.esq != None or r.esq is None and r.dir != None:
        pai = busca_pai(Raiz, r)

        if pai.esq == r:
            if r.dir != None:
                pai.esq = r.dir

            elif r.esq != None:
                pai.esq = r.esq

        elif pai.dir == r:
            if r.dir != None:
                pai.dir = r.dir

            elif r.esq != None:
                pai.dir = r.esq

    # 3o. caso o nó r possui 2 filhos, buscar em p o maior no do lado esquerdo de r, trocar o r.info por p.info,
    # buscar o pai de p, trocar o lado esq ou dir do pai com o filho esq. de p
    elif r.esq is not None and r.dir is not None:

            p = busca_maior(r.esq)
            r.info = p.info
            pai = busca_pai(Raiz, p)

            if pai.esq == p:
                pai.esq = p.esq

            else:
                pai.dir = p.esq

'''
def filhos(Raiz, r):
    if Raiz is not None:
        if Raiz.info == r:
            if r.esq is not None and r.dir is not None:
                print(r.esq.info)
                print(r.dir.info)
            elif (r.esq is not None and r.dir is None) or (r.dir is not None and r.esq is None):
                if r.esq is not None:
                    print("Só tem um filho")
                    print(r.esq.info)
                else:
                    print("Só tem um filho")
                    print(r.dir.info)
            else:
                print("É folha")
                print("Nao tem filho")
        else:
            filhos(Raiz.esq, r)
            filhos(Raiz.dir, r)
'''

Raiz = None  # arvore vazia

while True:
    print('\n1- Inserir valores'
          '\n2- Percursos'
          '\n3- Buscar valor'
          '\n4- Buscar o pai'
          '\n5- Remover um no da arvore'  
          #'\n6- Exibir os filhos de um no'  
          '\n0- Sair do programa')

    op = int(input("\nDigite a opção: "))

    if op == 0:
        break

    elif op == 1:
        q = int(input("Quantos valores deseja inserir? "))
        for i in range(q):
            val = int(input("\nDigite o valor a inserir na árvore: "))
            no = no_arvore(val)  # aloca-se o no com o valor digitado

            if Raiz == None:  # se a raiz for nula, a raiz passa a ser o valor alocado no no
                Raiz = no

            else:  # se nao chama a função se inserção
                Insere(Raiz, no)

        print('\nValores inseridos com sucesso.')

    elif op == 2:  # impressao de acordo com cada tipo de percurso
        print("\nPré Order: ")
        pre_order(Raiz)
        print()

        print("\nIn Order: ")
        in_order(Raiz)
        print()

        print("\nPós Order: ")
        pos_order(Raiz)
        print()

    elif op == 3:  # busca de um valor na arvore
        val = int(input("Digite o valor a buscar: "))
        r = busca(Raiz, val)  # valor encontrado na busca

        if r == None:  # se for none, o valor nao foi encontrado, se não, retorna o valor
            print("\nValor não existe na árvore! ")

        else:
            print(f"\nValor encontrado: {r.info}")

    elif op == 4:  # busca do pai de um valor na arvore
        val = int(input("Digite o valor a buscar: "))
        r = busca(Raiz, val)  # valor encontrado na busca

        if r == None:  # se for none, o valor nao foi encontrado
            print("\nValor não existe na árvore! ")

        else:
            if r == Raiz:  # se nao, se o valor for igual a raiz, o valor nao tem pai
                print("\nA raiz não tem pai!")
            else:
                pai = busca_pai(Raiz, r)  # se nao, busca o pai (a raiz), do valor
                print(f"\nO pai do {r.info} é: {pai.info}")

    elif op == 5:
        val = int(input("Digite o valor a remover: "))
        r = busca(Raiz, val)  # valor encontrado na busca

        if r == None:  # se for none, o valor nao foi encontrado
            print("\nValor não existe na árvore! ")

        else:
            if r == Raiz:  # se nao, se o valor for igual a raiz, o valor nao pode ser removido
                print("\nA raiz não pode ser removida!")
            else:
                print(f'Valor removido: {r.info}')
                remove(Raiz, r)

                print('\nReorganização da árvore: ')
                print("\nPré Order: ")
                pre_order(Raiz)
                print()

                print("\nIn Order: ")
                in_order(Raiz)
                print()

                print("\nPós Order: ")
                pos_order(Raiz)
                print()

'''
    elif op == 6:
        if Raiz == None:
            print("\nÁrvore vazia.")

        else:
            val = int(input("Digite o Nó a qual deseja exibir os filhos: "))
            r = busca(Raiz, val)
            print(filhos(Raiz, r))
'''

