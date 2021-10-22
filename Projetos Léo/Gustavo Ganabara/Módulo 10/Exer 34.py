#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Por favor, informe seu salário: R$"))

if salario <= 1250.00:
    aumento = salario * 1.15
    print("Você teve um aumento de: R${:.2f}".format(aumento))
else:
    aumento = salario * 1.10
    print("Você teve um aumento de: R${:.2f}".format(aumento))