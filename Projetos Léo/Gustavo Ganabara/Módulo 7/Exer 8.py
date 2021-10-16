#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n1 = float(input("Por favor, informar a metragem: "))
cm = n1*100
mm = n1*1000

print('A medida de {}m corresponde a {}cm e {}mm'.format(n1, cm, mm))