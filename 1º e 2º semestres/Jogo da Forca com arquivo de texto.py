
from random import choice

def inserePalavras(texto):
        arq = open('palavrasForca.txt', 'r')
        for line in arq:
            text = line.split(';')
            texto[text[0]] = text[1]
        arq.close()
        return texto

def sorteioPalavra(dicio):
    sorteio = choice(list(dicio))
    return sorteio

def tentativas():
    global palavraForc
    global palavraSort
    tentativas = 6
    while tentativas >= 0:
            if palavraForc == palavraSort:
                faixa()
                print(' '.join(palavraForc))
                print('\n"Parabéns, você ganhou o jogo da forca!"')
                break
            elif tentativas == 0:
                faixa()
                print('\n"Que pena, você foi enforcado!"')
                print(f'\nA palavra da forca era: {palavraSort}')
                break

            faixa()
            print('"JOGO DA FORÇA"\n')
            print('Descubra a palavra:\n')
            print(' '.join(palavraForc))
            faixa()
            if len(letrasDigitadas) > 0:
                print(f'Letras já tentadas: {letrasDigitadas}')
            letra = input('Informe uma letra: ').upper()
            letrasDigitadas.append(letra)

            if letra not in palavraSort:
                tentativas -= 1
                print(f'\nA letra informada não se encontra na palavra!')
                if tentativas > 0:
                    if tentativas == 1:
                        print(f'Tente novamente. Você ainda tem {tentativas} chance.')
                    else:
                        print(f'Tente novamente. Você ainda tem {tentativas} chances.')

                if tentativas == 3:
                    for key, value in dicioPalavras.items():
                        if key == palavraSort:
                            faixa()
                            print(f'"DICA: {value}"')
            else:
               palavraSubst = list(palavraForc)
               posi = 0
               for i in range(len(palavraSort)):
                    if letra == palavraSort[i]:
                         palavraSubst[posi] = letra
                    posi += 1
                    palavraForc = "".join(palavraSubst)
def faixa():
    print('=*'*30)


dicioPalavras = dict()
letrasDigitadas = []
inserePalavras(dicioPalavras)
palavraSort = sorteioPalavra(dicioPalavras)
palavraForc = '-' * len(palavraSort)
tentativas()








































