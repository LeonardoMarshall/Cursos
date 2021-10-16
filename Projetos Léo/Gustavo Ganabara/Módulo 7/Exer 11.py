#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input("Por favor, informe a largura da parede:"))
h = float(input("Por favor, informe a altura da parede:"))

a = l * h

t = a/2

print("Sua parede tem {:.2f}m²\nPara pintá-la será necessário {:.0f} litros de tinta".format(a, t))