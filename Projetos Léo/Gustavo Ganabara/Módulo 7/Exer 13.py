#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

n1 = float(input("Por favor, informe seu salário: R$"))

ns = n1 * 1.15

print("Parabéns, você recebeu um aumento de 15% no seu salário, agora receberá: R${:.2f}".format(ns))