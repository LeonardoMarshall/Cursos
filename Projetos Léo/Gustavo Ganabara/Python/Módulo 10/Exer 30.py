#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n1 = int(input('Por favor informe um número inteiro:'))

p = n1 % 2

if p == 0:
    print("O número {} é PAR!".format(n1))
else:
    print("O número {} é IMPAR".format(n1))