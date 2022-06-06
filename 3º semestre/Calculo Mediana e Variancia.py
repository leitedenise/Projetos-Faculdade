def medianaNA(lista):   #função que calcula a mediana para dados não agrupados

    if (len(lista) % 2) == 0:      #testa se o tamanho da lista (número de dados) é par
        mediana = lista[int(len(lista)/2)]
        mediana += lista[int(len(lista)/2 - 1)]  #se for par, soma os dois do meio (o da metade da lista e o anterior
                                                                                   # a ele) e depois divide por 2
        mediana = mediana / 2

    else:
        mediana = lista[int(len(lista)/2)]       #se for impar, só pega o valor que tiver na metade da lista

    return mediana

def varianciaNA(lista, quan):     #função que calcula a variancia para dados não agrupados
    m = sum(lista) // quan        #para a média soma-se os elementos da lista e divide pela quantidade de elementos
    s = 0
    for i in range(len(lista)):    #anda pela lista, somando cada elemento menos a media elevado ao quadrado
        s += ((lista[i] - m)**2)
    v = s / (quant -1)             #quando acaba os valores da lista, a variancia recebe a soma desses valores dividido pela quantidade de valores -1
    return v

def medianaA(L, F, T):         #função que calcula a mediana para dados agrupados (tabela de frequencia)
    global ind
    posi = (T+1)/2           #para achar a posição na fac, pega-se o total da frequencia +1, e divide-se por 2

    for i in range(len(F)):      #anda pela lista da fac, testando se o valor atual desse indice é maior que o valor da posição na fac, quando for
        if F[i] >= posi:          #pega-se o indice que esse valor está na fac
            ind = i

            med = L[ind][0]      #ai a mediana vai ser o valor que está na lista dos valores (dados) na linha que for a posição da fac,
            return med           #da coluna 0 que é do xi (valor)

def varianciaA(l, sfi, sxifi):    #Função que calcula a variancia para dados agrupados (tabela de frequencia)
    med = sxifi/sfi                #a media é a soma do xi*fi (elemento * frequencia) dividido pela soma do fi (frequencia)
    s = 0
    for i in range(len(l)):           #anda pela lista
        s += ((l[i][0] - med)**2) * l[i][1]      #variancia vai ser a somatoria de cada elemento menos a media, elevado ao quadrado,
    var = s / (sfi-1)                              #vezes a frequencia de cada um. Depois divide-se essa somatoria pela quantidade de elementos menos 1.
    return var           #e retorna o valor do resultado para o programa principal para ser exibido.

def medianaC(lis, tf, fa, c):    #Função que calcula a mediana para dados contínuos (tabela de classes)
    pos = tf/2             #Acha a posição na coluna da fac
    clasMed = []

    for i in range(len(fa)):      #percorre a lista da fac para comparar os valores e achar a posição
        if fa[i] >= pos:
            indi = i          #Quando acha, guarda o índice em que esse valor está

            m1 = lis[indi][0]   #Limite inferior do intervalo da classe
            m2 = lis[indi][1]   #Limite superior do intervalo de classe
                                #Ambos pega o valor correspondente a posição que foi achada na fac, da lista dos valores
            fM = lis[indi][2]   #a frequencia da classe também é achada no valor correspondente à posição da fac, na lista de valores

            if indi == 0:      #testa se a classe mediana (posição na fac) é a primeira, se for, a faca (frequencia acumulada anterior) é 0
                faca = 0
            else:             #se não, ela vai ser o valor da fac, anterior à posição correspondente à classe mediana
                faca = fa[indi - 1]

            med = (((pos - faca) * c) / fM) + m1  #cálculo da mediana
            clasMed.append([m1, m2])       #valores (limite inferior e superior) da classe mediana, para mostrar na tela

            return clasMed, med

def varianciaC(listaC, Tfi, Txi_fi):  #função que calcula a variância para dados contínuos
    m = (Txi_fi) / Tfi       #media é a soma do xi*fi dividido pela soma da frequencia (fi)
    sV = 0
    for i in range(len(listaC)):    #percorre a lista de valores das classes
        sV += ((listaC[i][3] - m) ** 2) * listaC[i][2]    #para ir somando cada xi (média dos valores de cada classe) menos a média, elevando ao quadrado
                                                         #e multiplicando pela frequencia de cada um
    V = sV / (Tfi - 1)      #ao final do somatório, divide-se a soma pela soma da frequencia (total de valores) menos 1
    return V

# Aceita uma lista com o nome das colunas e com os valores das linhas, uma matriz contendo os valores de cada coluna, na mesma ordem:

def desenharTabela(colunas, valores):
    quantidadeDeColunas = len(colunas)
    quantidadeDeLinhas = len(valores)

    larguras = []      #Uma lista com a largura de cada coluna. A largura de cada coluna é igual ao tamanho do maior item, em caracteres
    larguraTotal = 0

    # compara o valor anterior com o novo valor, e pega o tamanho do maior:

    for indiceColuna in range(quantidadeDeColunas):
        larguraDaColuna = len(colunas[indiceColuna])

        for indiceLinha in range(quantidadeDeLinhas):
            tamanhoDoValor = len(str(valores[indiceLinha][indiceColuna]))

            larguraDaColuna = max(larguraDaColuna, tamanhoDoValor)

        larguraDaColuna += 1
        larguras.append(larguraDaColuna)
        larguraTotal += larguraDaColuna

    print("+" + ("-" * (larguraTotal + quantidadeDeColunas - 1)) + "+")

    for indiceColuna in range(quantidadeDeColunas):
        nomeDaColuna = colunas[indiceColuna]
        largura = larguras[indiceColuna] - len(nomeDaColuna)

        print("|" + nomeDaColuna + (" " * largura), end="")
    print("|")

    print("+" + ("-" * (larguraTotal + quantidadeDeColunas - 1)) + "+")

    for indiceLinha in range(quantidadeDeLinhas):
        for indiceColuna in range(quantidadeDeColunas):
            valor = valores[indiceLinha][indiceColuna]
            largura = larguras[indiceColuna] - len(str(valor))

            print("|" + valor + (" " * largura), end="")
        print("|")

    print("+" + ("-" * (larguraTotal + quantidadeDeColunas - 1)) + "+")


dados = []          #lista dos dados não agrupados
dadosAgru = []      #lista dos dados agrupados
fac = []            #lista da coluna da fac
dadosCont = []      #lista dos dados contínuos
facC = []           #lista da coluna da fac, dos dados contínuos

while True:
      print("\nMenu Principal: ")
      print("\n1- Dados discretos (não agrupados)\n"
            "2- Dados discretos (agrupados)\n"
            "3- Dados contínuos (tabela de classes)\n"
            "0- Sair\n")

      op = int(input("Digite a opção desejada: "))

      if op == 0:
          break

      elif op == 1:
            while True:    #informa-se a quantidade de valores total dos dados, se for maior que 100 (que é o limite do vetor), pede-se de novo até que seja menor que 100
                  quant = int(input("\nDigite a quantidade de valores total: "))
                  if quant > 100:
                     print("\nÉ permitido apenas 100 valores de entrada. Digite novamente!")

                  else:           #quando der a quantidade certa de valores limpa-se a lista dos dados
                    dados.clear()
                    for i in range(quant):      #percorre-se a lista o tanto de vezes que tiver de valores
                        elem = float(input("\nInforme o xi: "))    #digita-se os elementos,
                        dados.append(elem)                         #adcionando à lista dos dados
                        dados.sort()                        #e coloca-se os dados em ordem crescente

                    #Impressão dos dados na tela:

                    print(f"\nDados discretos não agrupados:\n ")
                    for i in range(len(dados)):
                        print(f"{dados[i]} ", '', end=" ")

                    medianaNA(dados)     #chama-se a função que calcula a mediana
                    print(f"\n\nMediana: {medianaNA(dados):.2f}")   #mostra-se o resultado

                    varianciaNA(dados, quant)      #chama-se a função que calcula a variancia
                    print(f"\nVariância: {varianciaNA(dados, quant):.2f}")       #mostra-se o resultado
                    break


      elif op == 2:
          while True:   #pede-se também a quantidade de valores, que tem que ser menor que 100
              quan = int(input("\nDigite a quantidade de valores total: "))
              if quan > 100:
                  print("\nÉ permitido apenas 100 valores de entrada. Digite novamente!")

              else:
                  valDis = int(input("\nInforme a quantidade de valores distintos: "))

                  dadosAgru.clear()   #limpa-se a lista dos dados agrupados, da fac e as variáveis de soma, da fac, xi e xi*fi,
                  fac.clear()         #para quando rodar de novo ela não acumular valor do outro calculo.
                  soma_fac = 0
                  soma_fi = 0
                  soma_xi_fi = 0

                  for i in range(valDis):     #anda-se pela lista a quantidade de vezes que for do total de valores
                      val = float(input("\nInforme o xi: "))    #pedindo o valor e a frequencia com que ele aparece
                      freq = int(input("Informe o fi: "))

                      dadosAgru.append([val, freq, val*freq])    #a lista de dados recebe na primeira posição os valores, na segunda a frequencia,
                      dadosAgru.sort()                           #e na terceira os valores*frequencia (xi*fi), e coloca-se em ordem também

                      soma_fac += freq            #somatório da frequencia acumulada
                      fac.append(soma_fac)        #uma lista à parte recebe esse somatorio, que é a fac

                      soma_fi += freq            #somatorio da coluna da frequencia
                      soma_xi_fi += val*freq     #somatorio da coluna do xi*fi


                  print('\nDados discretos agrupados: ')
                  colunas = ["Xi", "Fi", "xi_fi", "fac"]
                  valores = []

                  #impressão, pra mostrar a tabela de frequencia:

                  #anda pela lista de dados, adicionando à matrix de valores os calculos das colunas
                  for i in range(len(dadosAgru)):
                      valores.append([
                          f'{dadosAgru[i][0]:.1f}',
                          f'{dadosAgru[i][1]:.1f}',
                          f'{dadosAgru[i][2]:.1f}',
                          f'{fac[i]:.1f}'
                      ])

                  valores.append(['Total', str(soma_fi), str(soma_xi_fi), ""])
                  desenharTabela(colunas, valores)


                  medianaA(dadosAgru, fac, soma_fi)             #chama-se a função para calcular a mediana
                  print(f"\nMediana: {medianaA(dadosAgru, fac, soma_fi):.2f}")        #mostra-se o resultado

                  varianciaA(dadosAgru, soma_fi, soma_xi_fi)
                  print(f'\nVariância: {varianciaA(dadosAgru, soma_fi, soma_xi_fi):.2f}')

                  break


      elif op == 3:
          while True:   #pede-se também a quantidade de valores, que tem que ser menor que 100
              quan = int(input("\nDigite a quantidade de valores total: "))
              if quan > 100:
                  print("\nÉ permitido apenas 100 valores de entrada. Digite novamente!")

              else:
                  classes = int(input("\nInforme a quantidade de classes: "))    #quantidade de classes que terá na tabela

                  #limpa as listas e variáveis cada vez que volta para fazer outro cálculo:

                  dadosCont.clear()
                  facC.clear()
                  soma_facC = 0
                  soma_fiC = 0
                  soma_xiC_fiC = 0

                  comp = int(input("\nInforme o comprimento das classes: "))    #comprimento de cada intervalo de classe

                  for i in range(classes):    #repete a quantidade de vezes que for a quantidade de classes

                      while True:
                          li = int(input("\nInforme o limite inferior do intervalo da classe: "))   #pede-se os dois intervalos da classe, e a frequencia
                          ls = int(input("Informe o limite superior do intervalo da classe: "))
                          fi = int(input("Informe a frequência da classes (fi): "))

                          if ls-li != comp:      #se o intervalo estiver incorreto (diferente do informado), repete até que esteja correto
                              print("\nComprimento incorreto do intervalo de classe. ")
                          else:

                            break

                      xi = (li+ls)/2    #soma-se os dois limites de cada intervalo de classe e divide por 2 para achar o xi
                      xi_fi = xi*fi      #valores para a tabela do xi*fi
                      dadosCont.append([li, ls, fi, xi, xi_fi])   #adiciona os intervalos das classes, a frequencia, o xi e o xi*fi, na lista

                      soma_facC += fi            #soma da fac dos dados contínuos
                      facC.append(soma_facC)     #lista da fac dos dados contínuos

                      soma_fiC += fi             #soma da frequencia dos dados contínuos
                      soma_xiC_fiC += xi_fi      #soma do xi*fi

                  print('\nDados contínuos: ')
                  colunas = ["Classes", "fi", "xi", "xi*fi", "fac"]
                  valores = []

                  #impressão dos dados contínuos (tabela de classes):

                  for i in range(len(dadosCont)):
                      valores.append([
                          f'{dadosCont[i][0]} |—— {dadosCont[i][1]}',
                          f'{dadosCont[i][2]}',
                          f'{dadosCont[i][3]:.1f}',
                          f'{dadosCont[i][4]:.1f}',
                          f'{facC[i]}'
                      ])

                  valores.append(['Total', str(soma_fiC), "", str(soma_xiC_fiC), ""])
                  desenharTabela(colunas, valores)


                  clasM, medi = medianaC(dadosCont, soma_fiC, facC, comp)   #recebe o valor retornado da função, da classe e do cálculo da mediana
                  var = varianciaC(dadosCont, soma_fiC, soma_xiC_fiC)    #recebe o valor retornado da função, do cálculo da variância


                  #print da classe mediana, valor da mediana e da variância:

                  for i in range(len(clasM)):

                      print(f'\nClasse mediana: {clasM[i][0]} |—— {clasM[i][1]}')
                  print(f'\nMediana: {medi:.2f}')
                  print(f'\nVariância: {var:.2f}')

              break


















