#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”

cidade = str(input("Por favor, informe o nome da sua cidade:"))
print(cidade[:5].lower() == "santo")
