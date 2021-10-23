#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Por favor, informe a velocidade em km/h que trafega no momento:'))

if v <= 80:
    print('Está dentro da velocidade permitida!')
else:
    multa = (v-80.0)*7.0
    print('Você está trafegando a cima do limite permitido de 80 km/h')
    print('Multa por excesso de velocidade aplicada:R${:.2f}'.format(multa))
