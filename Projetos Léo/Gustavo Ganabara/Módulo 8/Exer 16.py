#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc

n1 = float(input("Por favor, informe um número real:"))
i = trunc(n1)

print("O valor inteiro do número {} é {}".format(n1,i))
