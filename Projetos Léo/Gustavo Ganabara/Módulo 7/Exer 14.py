#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c1 = float(input("Por favor, informar a temperatura em Celsius:"))

f1 = ((c1/5)*9)+32


print("A temperatura de {:.2f} Graus Celsius, na conversão para Fahrenheit fica {:.2f} F".format(c1,f1))