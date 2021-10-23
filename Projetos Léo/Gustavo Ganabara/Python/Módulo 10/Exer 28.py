#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from time import sleep
import random

n1 = random.randrange(5)
print("-=-"*26)
n2 = int(input('Me fale um número de zero a cinco e veja se acertou!'))
print("PROCESSANDO...")
print("-=-"*26)
sleep(3)

if n2 == n1:
    print('Parabéns, você acertou!')
else:
    print('Foi quase, era {}.\nMais sorte na próxima'.format(n1))
