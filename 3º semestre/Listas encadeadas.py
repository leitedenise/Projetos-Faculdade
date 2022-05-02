class no:
    def __init__(self, val):
        self.info = val #valor que for alocar no no
        self.prox = None #proximo do valor, que inicialmente é None, pois só tem esse valor na lista

    def getInfo(self):
        return self.info #retorna o valor

    def getProx(self):
        return self.prox #retorna o próximo do valor

    def setInfo(self, val):
        self.info = val #troca o valor por um outro desejável

    def setProx(self, proximo):
        self.prox = proximo #troca o próximo do valor por um outro desejável

class listaEncadeada:
    def __init__(self):
        self.inicio = None #o início começa com None, pois não tem valor na lista

    def InsereInicio(self, val):
        p = no(val) #aloca um 'no' pro valor
        p.setProx(self.inicio) #troca o proximo desse valor pelo inicio
        self.inicio = p #e coloca o início valendo o valor que deseja inserir, dessa forma ele será o primeiro da lista

    def InsereFim(self, val):
        p = no(val) #aloca um 'no' pro valor
        if self.inicio == None: #Lista está vazia
            self.inicio = p #se a lista está vazia coloca-se o valor no inicio

        else: #se não está vazia
            q = self.inicio #coloca-se o ponteiro 'q' no inicio
            while q.getProx() != None: #Anda enquanto o proximo do ponteiro 'q' não for nulo
                q = q.getProx() #vai passando o ponteiro pra frente até chegar no None (final)
            q.setProx(p) #quando o próximo de 'q' é None, ele é o último, então insere ao final da lista o valor alocado inicialmente

    def RemoveInicio(self):
        global val #usa-se a variável de fora da função (do programa principal) como global e não uma para receber um parâmetro,
        # para que se possa retornar a essa variável o valor que ela estiver, dessa forma o valor dela se altera fora da função,
        # ela recebe o valor que foi alterado na função

        p = self.inicio #coloca-se o ponteiro no inicio
        self.inicio = p.getProx() #ai passa o inicio pro proximo, removendo assim o valor que estava no inicio
        val = p.getInfo() #a variável 'val' recebe o valor que estava em p e que foi removido

    def RemoveFim(self):
        global val
        p = self.inicio #coloca-se o 'p' no inicio
        if p.getProx() == None: #se o proximo de 'p' for None, não tem mais valores após o 'p',então remove-se o 'p' (último valor)
            self.inicio = None #Passando o inicio pra none
        else:
            #Quando o 'p' for o último, 'q' será o penúltimo
            while p.getProx() != None: #Anda pela lista enquanto o próximo de 'p' não seja nulo, ou seja, enquanto o valor não for o último
                q = p #cada vez que anda passa o 'q' pra o valor 'p' (agora anterior)
                p = p.getProx() # e passa o 'p' pro seu proximo
            q.setProx(None) #quando o 'p' for o último troca o proximo de 'q' (que é o 'p'- último valor) por none, para remover o ultimo valor

        val = p.getInfo() #recebe fora da função o valor que foi removido

    def Imprime(self):
        p = self.inicio #coloca-se o 'p' no inicio
        while p != None: #anda na lista até que o 'p' não seja nulo
            print(f'{p.getInfo()} --> ', end='') #mostra o valor de 'p', o que ta na variável 'p'.
            p = p.getProx() #o 'p' passa a ter o valor do próximo valor a ele.
            # Ai quando voltar ao laço ele vai mostrar o valor de p, que vai ser o seu próximo, imprimindo a lista toda

        print('None') #quando chegar ao final da lista, onde o proximo de 'p' é nulo mostra o None, indicando o final da lista

    def ConsultaValor(self, val):
        p = self.inicio #coloca o 'p' no inicio
        while p != None and p.getInfo() != val: #anda pela lista até que o 'p' não seja nulo e o valor de 'p' seja diferente do valor que deseja encontrar
            p = p.getProx() #vai passando o 'p' pra frente pra percorrer a lista

        return p #Quando acha o valor, que 'p' seja igual ao valor procurado, retorna o valor.

    def InsereDepois(self, r, val):
        p = no(val) #aloca um no com o valor que deseja inserir
        if r.getProx() != None: # 'r' recebe por parametro o valor encontrado na função anterior. Se ele tiver sido encontrado (não for nulo)
            p.setProx(r.getProx()) #troca o proximo de 'p' (que é o valor que deseja inserir depois de 'r') pelo proximo de 'r' (valor da lista)
            r.setProx(p) #troca o proximo de 'r' pelo 'p', dessa forma inserindo o 'p' após o 'r'

    def InsereAntes(self, r, val):
        p = no(val) #aloca o 'no' com o valor que deseja inserir
        p.setProx(r) #'r' é o valor em que desejo inserir antes dele. Se o proximo do meu 'p' for o 'r' eu estarei inserindo o valor de 'p' antes de 'r'
        q = self.inicio #coloca-se um ponteiro 'q' no inicio

        while q.getProx() != r: #anda pela lista até que o proximo do ponteiro 'q' seja o valor de 'r'
          q = q.getProx() #o valor de 'q' passa a ser o proximo dele, passando o ponteiro pra frente para percorrer toda a lista

        q.setProx(p) #quando o proximo de 'q' for o 'r' troca o proximo de 'q' por 'p', inserindo o valor que está em 'p' antes do 'r'

    def RemoveMeio(self, r):
        q = self.inicio
        while q.getProx() != r: #anda pela lista enquanto o proximo de que não seja o 'r' (valor a ser removido)
            q = q.getProx() #vai passando o ponteiro pra frente até achar o 'r'
        q.setProx(r.getProx()) #quando acha o 'r' troca o proximo de 'q' pelo proximo de 'r', tirando o valor de 'r' que era o proximo de 'q', da lista.


lista = listaEncadeada()
val = 0

while True:
    print('\n1- Inserir no início\n'
          '2- Inserir no fim\n'
          '3- Mostrar a lista\n'
          '4- Remover no início\n'
          '5- Remover no fim\n'
          '6- Consultar valor\n'
          '7- Inserir depois de um valor\n'
          '8- Inserir antes de um valor\n'
          '9- Remover um valor\n'
          '10- Inserir Ordenado\n' 
          '0- Sair do programa\n')

    op = int(input('Digite a opção: '))

    if op == 0:
        break

    elif op == 1:
        val = int(input('\nDigite o valor a inserir: '))
        lista.InsereInicio(val)

    elif op == 2:
        val = int(input('\nDigite o valor a inserir: '))
        lista.InsereFim(val)

    elif op == 3:
        if lista.inicio == None:
            print('Lista vazia. ')

        else:
            print('Lista:\n ')
            lista.Imprime()

    elif op == 4:
        if lista.inicio == None:
            print('Lista Vazia. Nenhum elemento a remover.')

        else:
            lista.RemoveInicio()
            print(f'\nValor removido: {val}')

    elif op == 5:
        if lista.inicio == None:
            print('Lista Vazia. Nenhum elemento a remover.')

        else:
            lista.RemoveFim()
            print(f'\nValor removido: {val}')

    elif op == 6:
        val = int(input('Digite o valor que deseja consultar na lista: '))

        r = lista.ConsultaValor(val)

        if r == None:
            print('\nValor não existe na lista.')
        else:
            print(f'\nValor encontrado: {r.getInfo()}')

    elif op == 7:
        val = int(input('Digite o valor que deseja consultar na lista: '))

        r = lista.ConsultaValor(val)

        if r == None:
            print('\nValor não existe na lista.')

        else:
            val = int(input('Digite o valor a inserir: '))

            if r.getProx() == None: #Se o r é o último.
                lista.InsereFim(val)
                print('\nValor inserido com sucesso.')

            else:
                lista.InsereDepois(r, val)
                print('\nValor inserido com sucesso.')

    elif op == 8:

        val = int(input('Digite o valor que deseja consultar na lista: '))

        r = lista.ConsultaValor(val)

        if r == None:
            print('\nValor não existe na lista.')
        else:
            val = int(input('Digite o valor a inserir: '))

            if r == lista.inicio: #r é o primeiro
                lista.InsereInicio(val)
                print('\nValor inserido com sucesso.')
            else:
                lista.InsereAntes(r, val)
                print('\nValor inserido com sucesso.')

    elif op == 9:
        val = int(input('Digite o valor que deseja remover na lista: '))

        r = lista.ConsultaValor(val)

        if r == None:
            print('\nValor não existe na lista.')
        else:

            if r == lista.inicio:  # r é o primeiro
                lista.RemoveInicio()
                print(f'\nValor Removido: {val}.')
            else:
                if r.getProx() == None:  #Se o r é o último
                    lista.RemoveFim()
                    print(f'\nValor removido: {val}')
                else:
                    lista.RemoveMeio(r)
                    print(f'\nValor removido: {val}')

    elif op == 10:
        val = int(input('Digite o valor a inserir: '))
        q = lista.inicio  # coloca-se o q no inicio.

        if q == None: # verifica se o início é nulo, se sim insere no início.
            lista.InsereInicio(val)
            print('\nValor inserido com sucesso.')

        else:
            if val < q.getInfo(): # Verifica se o valor é menor que o que está no início, se for insere no início, antes dele.
                lista.InsereInicio(val)
                print('\nValor inserido com sucesso.')

            else:
                #Anda pela lista comparando cada valor com o que deseja inserir.

                while val > q.getInfo() and q.getProx() != None: # Anda até quando o valor for maior do que o valor  que o 'q' está,
                    # e o próximo dele seja nulo.

                    q = q.getProx() #Vai passando o 'q' pro próximo enquanto o valor for maior que o 'q'.

                if val < q.getInfo(): # Quando o valor for menor que 'q' para e verifica se ele é menor que o valor que o 'q' está, se sim insere antes,
                    lista.InsereAntes(q, val)
                    print('\nValor inserido com sucesso.')

                else: # Se for maior que o valor onde o 'q' está insere depois, ao final, pois ele seria o último da lista.
                    lista.InsereFim(val)
                    print('\nValor inserido com sucesso.')











