tempo = int(input('Quantos anos tem seu carro?'))

if tempo <=3:
    print('carro novo!')
else:
    print('carro velho!')
print('--FIM--')


#Segunda forma de executar o if e else
tempo = int(input('Quantos anos tem seu carro?'))

print('carro novo'if tempo <3 else'carro velho')

print('--FIM--')
#-----------------------------------------------------------------------------

#PARTE PRÁTICA

nome = str(input("Qual é seu nome?"))

if nome == 'Leonardo':
    print('Que nome lindo você tem!')
else:
    print("Seu nome é tão normal!")
print("bom dia, {}".format(nome))

#------------------------------------------------------------------------------

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a primeira nota:'))
m = (n1+n2)/2
print('A sua média foi: {:.1f}'.format(m))

if m>=6.0:
    print('Sua média foi boa! Parabéns')
else:
    print('Sua média foi ruim! Vai estudar, vagabundo!')