#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

nome = str(input("Por favor, digite seu nome completo:"))

nome = nome.strip()
nome = nome.split()
nome = "-".join(nome)
nome1 = nome.find("-")
#print(nome1)
nome2 = nome.rfind("-") + 1
#print(nome2)
print("Seu primeiro nome é:{}".format(nome[:nome1]))
print("Seu segundo nome é:{}".format(nome[nome2:]))