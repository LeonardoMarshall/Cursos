#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math

co = float(input("Por favor informe o Cateto Oposto em metros:"))
ca = float(input("Por favor informe o Cateto Adjacente em metros:"))

h = math.sqrt(math.pow(co,2)+math.pow(ca,2))
# h = hypot(co,ca)
print("A hipotenusa do CO:{} e CA:{} é {:.2f}".format(co,ca,h))