# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = int(input("Por favor, informar ângulo em graus:"))

rad = math.radians(angulo)
cos = math.cos(rad)
sen = math.sin(rad)
tan = math.tan(rad)

#print(rad)

print("O valor grau {} é:".format(angulo))
print("Seno:{:.2f}".format(sen))
print("Cosseno:{:.2f}".format(cos))
print("Tangente:{:.2f}".format(tan))