#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez

frase = str(input("Por favor, elabore uma frase:"))
frase = frase.upper()
print("A frase apresenta {} vezes a letra 'A'".format(frase.count("A")))
print("O primeiro 'A' está localizado na posição: {}".format(frase.find("A")))
print("O último 'A' está localizado na posição: {}".format(frase.rfind("A")))
