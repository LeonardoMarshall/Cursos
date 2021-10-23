#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p1 = float(input("Por favor, informe o preço do produto:"))

d1 = p1*0.95

print("O valor da mercadoria com 5% de desconto é de R${:.2f}".format(d1))