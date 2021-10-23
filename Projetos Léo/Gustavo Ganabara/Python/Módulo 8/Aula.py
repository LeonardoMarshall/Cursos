#import math #Utilizado para importar a biblioteca inteira
from math import sqrt, ceil #Utilizado para importar somente essa função
num = int(input("Digite um número:"))

#raiz = math.sqrt(num) #Utilizado quando importado a biblioteca inteira
raiz = sqrt(num)

print("A raiz de {} é igual a {}".format(num, ceil(raiz)))
