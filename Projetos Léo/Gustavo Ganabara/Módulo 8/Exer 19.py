#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

a1 = str(input("Por favor, informe o nome do aluno 1:"))
a2 = str(input("Por favor, informe o nome do aluno 2:"))
a3 = str(input("Por favor, informe o nome do aluno 3:"))
a4 = str(input("Por favor, informe o nome do aluno 4:"))

#Segunda opção:
#lita = [a1,a2,a3,a4]
#rng = random.choice(lista)

rng = random.choice([a1,a2,a3,a4])
print("O aluno: {} será encarregado de apagar o quadro".format(rng))