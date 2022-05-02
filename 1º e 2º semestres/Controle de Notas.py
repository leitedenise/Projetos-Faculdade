import random

M = [0]*7
for l in range(7):
    M[l] = [0]*20
    for c in range(20):
        M[l][c] = (round(random.uniform(0,10), 1))

opção = 0

aluno = 'Aluno 1', 'Aluno 2', 'Aluno 3', 'Aluno 4', 'Aluno 5', 'Aluno 6', 'Aluno 7', 'Aluno 8', 'Aluno 9', 'Aluno 10', 'Aluno 11', 'Aluno 12', 'Aluno 13', 'Aluno 14', 'Aluno 15', 'Aluno 16', 'Aluno 17', 'Aluno 18', 'Aluno 19', 'Aluno 20'

disci = ['Matemática', 'ADM', 'Inglês', 'Programação', 'Algoritmo', 'Hardware', 'Arquitetura']

while True:
    print("Menu de Opções:\n ")
    print('''[1] Mostrar as notas de todos os alunos.
[2] Pedir um aluno (1 a 20) e exibir suas notas, informando se ele foi 'aprovado' ou 'reprovado'.
[3] Pedir uma disciplina (1 a 7) e exibir as notas dos alunos, com a média no final.
[4] Sair.''')

    opção = int(input("\nEscolha uma opção >> "))

    if opção == 4:
        print("\nFim do programa.")
        break

    elif opção == 1:
        print()
        print("Controle de notas:\n ")
        print("           Matemática    ADM       Inglês   Programação  Algoritmo  Hardware  Arquitetura\n")

        for l in range(20):
            print(f'{aluno[l]: <10}- ', end=' ')
            for c in range(7):
                print(f"[{M[c][l]:4.1f}]", end='     ')
            print()
        print()

    elif opção == 2:
        aluno = int(input("Escolha um aluno (Número de 1 a 20) >> "))

        print()

        if aluno not in range(1,21):
            print("Aluno inválido!\n")
        else:

            for c in range(7):
             print(f"{disci[c]:12} -  Nota do aluno {aluno}: {M[c][aluno-1]:4.1f}  >> ", end='')

             if M[c][aluno-1] >= 6:
                print(f"ALUNO APROVADO!")
                print()
             else:
                print(f"ALUNO REPROVADO!")
                print()

    elif opção == 3:
        disc = int(input("Escolha uma disciplina (Número de 1 a 7) >> "))

        print()
        if disc not in range(1,8):
            print("Disciplina inválida!\n")
        else:

         print(f"{disci[disc-1]}", end=' ')
         print()
         print(f"\nNotas dos alunos em {disci[disc-1]}: {M[disc-1]}")

         soma = 0
         for l in range(20):
            soma += M[disc-1][l]
            media = soma / 20

         print(f"Média das notas dos alunos em {disci[disc-1]}: {media:4.1f}")
         print()

    elif opção != 1 != 2 != 3 != 4:
        print("\nOpção inválida!\n")


    op = input("Deseja executar novamente? 's' ou 'n' >> ")
    print()
    if op != 's':
        print("Execução finalizada.")
        break















