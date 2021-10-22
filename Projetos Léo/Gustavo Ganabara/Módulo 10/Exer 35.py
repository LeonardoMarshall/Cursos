#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

t1 = float(input('Por favor, informar a medida de uma reta:'))
t2 = float(input('Por favor, informar a medida de uma reta:'))
t3 = float(input('Por favor, informar a medida de uma reta:'))

if t1 == t2 and t1 == t3:
    print("As três medidas formam um triângulo")

else:
    print('Não é possível formar um triângulo')