import random

aposta =[]

while len(aposta)<6:
    n=random.randint(1,60)
    if n in aposta:
        print("Número gerado já está na lista, esse número não será inserido e será gerado outro número!")

    else:
        aposta.append(n)
    aposta.sort()

result=[]
while len(result)<6:
    r=int(input("Informe os números do resultado da megasena>> "))
    if r not in range(1,60+1):
        print("Número inválido, informe somente números no intervalo de de 1 a 60!\n")
    else:
      if r in result:
        print("Número informado já foi digitado, informe outro número!\n")
      else:
          result.append(r)
    result.sort()

acerto=0
for val in aposta:
    if val in result:
        acerto += 1
if acerto == 4:
    print("Você acertou a quadra, com 4 números certos!")
if acerto == 5:
    print("Você acertou a quina, com 5 números certos!")
if acerto == 6:
    print("Parabéns, Você acertou a sena, com 6 números certos!")
elif acerto < 4:
    print("Não foi dessa vez!")

print("Aposta Supresinha=", aposta)
print("Resultado da megasena=", result)



