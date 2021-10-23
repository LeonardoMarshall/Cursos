#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input('Por favor, informe a distância em kilometro da sua viagem:'))

if km <= 200.00:
    custo = km*0.50
    print('Para realizar a viagem de {:.0f} km, o custo da passagem será de:R${:.2f}'.format(km,custo))
else:
    custo = km*0.45
    print('Para realizar a viagem de {:.0f} km, o custo da passagem será de:R${:.2f}'.format(km,custo))