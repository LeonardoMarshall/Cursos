#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = input("Por favor informe seu nome completo:")
print("Seu nome todo em letra maiúscula: {}".format(nome.upper()))
print("Seu nome todo em letra minúscula: {}".format(nome.lower()))
print("Seu nome tem {} caracteres ao todo".format(len(nome)-nome.count(" ")))
pnome = nome.split()
print("Seu primeiro nome tem {} caracteres ao todo".format(len(pnome[0])))