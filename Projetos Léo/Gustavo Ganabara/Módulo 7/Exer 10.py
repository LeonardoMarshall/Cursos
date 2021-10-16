#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

n1 = float(input("Por favor, informar seu saldo em dinheiro: R$"))

dol = n1 / 5.51

print(f"Com o saldo disponível, é possível comprar ${dol:.2F} dólares")
