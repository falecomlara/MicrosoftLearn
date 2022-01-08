# OBJETIVO É APRENDER A USAR O WHILE, ELSE, BREAK E CONTINUE
import random

dado = 0
contador = 0
boasvindas = '\n A primeira pessoa que tirar 5, ganha! \n'

print(boasvindas.upper())

nome = input('Qual é o seu nome, OU \'S\' para sair: ')
while dado !=5:
    if nome.upper() == 'S':
        break
        #SAI DO WHILE

    if nome.upper() == '':
        nome = input('Qual é o seu nome, OU \'S\' para sair: ')
        continue
        #FICA NO LOOP WHILE

    contador = contador + 1
    dado = random.randint(1,10)
    print(f'{nome.upper()} jogou o dado e o resultado foi {dado}')
else:
    print(f'VOCÊ GANHOU !!!')

print(f'\n Foi preciso jogar o dado {contador} vezes.')