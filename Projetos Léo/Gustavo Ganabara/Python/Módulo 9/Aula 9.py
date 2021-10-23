frase = "Curso em vídeo Python"
print(frase[1:13:2]) #[1: mostra a partir do primeiro caracter :13 vai até o caracter -1 :2 pula de 2 em 2 os caracteres
print(len(frase)) #Retornar o tamanho da string


frase.count("o") #Conta quantas vezes aparece a letra 'o'
frase.count("o",0,13) #Conta quantas vezes aparece a letra 'o' de 0 a 12 caracteres da frase
frase.find("deo") #Mostra aonde ele encontrou o conjunto "deo", se o retorno for -1 significa que não existe na frase
"curso" in frase #Ele retornar true/false se a palavra curso estiver na variável frase
frase.replace("python","android") #Ele encontra a palavra python por android

#TRANSFORMAÇÃO
frase.upper() #Transfroma toda a cadeia de caracteres em maiúsculo
frase.lower() #Transfroma toda a cadeia de caracteres em minúsculo
frase.capitalize() #Ele joga todos os caracteres para minúsculo e só o primeiro caracter fica em maiúsculo
frase.title () #Ele transforma a inicial de todas as palavras em maiúsculo
frase.strip () #Ele remove todos os espaços vazios do começo e do fim da string
frase.rstrip () #Ele remove os espaços vazios do final da string
frase.lstrip () #Ele remove os espaços vazios do começo da string

#DIVISÃO
frase.split () #divide a string nos espaços vazios e cria uma lista

#JUNÇÃO
"-".join(frase) #Junta todos os elementos da frase (normalmente utilizado após a quebra feita com split)