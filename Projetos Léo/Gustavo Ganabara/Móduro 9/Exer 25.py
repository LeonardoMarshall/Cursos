#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome

NomeC = input("Por favor, informe seu nome completo: ")
NomeC = NomeC.upper()

print ("Seu nome contém a palavra 'SILVA'? {}".format("SILVA" in NomeC))