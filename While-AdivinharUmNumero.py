import random

boasvindas = 'adivinhe o numero que estou pensando entre 1 a 10'
contador = 0
chutar = 0

numero = random.randint(1,10)
print(numero)
print(boasvindas.upper())

while chutar != numero:
    chutar = input('Eu acho que é o número: ')
    contador = contador + 1
    if chutar.isascii():
        print('Estou pensando em um NÚMERO e NÃO em uma letra')
    if chutar.isnumeric():
        chutar = int(chutar)
        if chutar < numero:
            print('Chute um número MAIOR')
        else:
            print('Chute um número MENOR')
else:
    # O ELSE NEM É NECESSÁRIO, MAS COLOQUEI PARA ENTENDER A SAIDA DO LAÇO WHILE
    print(f'Eu pensei no número {numero} e você adivinhou na {contador} tentativa')