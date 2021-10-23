#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Por favor, informar quantos kilometros você rodou com o carro:"))
carro = int(input("Por favor, informar quantos dias está com o carro alugado:"))

precokm = km * 0.15
precocarro = carro * 60

print("-"*60)
print("\nValor a se pagar pelos {:.0f} dias com o carro alugado: R${:.2f}".format(carro,precocarro))
print("Valor a se pagar pelos {:.0f} km rodados com o carro: R${:.2f}\n".format(km,precokm))
print("-"*60)