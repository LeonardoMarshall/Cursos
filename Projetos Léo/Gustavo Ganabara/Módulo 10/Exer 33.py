#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


n1 =  int(input('Por favor, informe um número inteiro qualquer: '))
n2 =  int(input('Por favor, informe um número inteiro qualquer: '))
n3 =  int(input('Por favor, informe um número inteiro qualquer: '))

if n1 > n2 and n1>n3:
    print("O {} é o maior número entre todos!".format(n1))
if n2 > n1 and n2 > n3:
    print("O {} é o maior número entre todos!".format(n2))
if n3 > n1 and n3 > n2:
    print("O {} é o maior número entre todos!".format(n3))

if n1 < n2 and n1 < n3:
    print("O {} é o menor número entre todos!".format(n1))
if n2 < n1 and n2 < n3:
    print("O {} é o menor número entre todos!".format(n2))
if n3 < n1 and n3 < n2:
    print("O {} é o menor número entre todos!".format(n3))