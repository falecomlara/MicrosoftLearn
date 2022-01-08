import random
dado = random.randint(1, 10)
print(f'Você jogou o dado na mesa e o resultado foi', dado)
print(23*'-=')

#Você pode importar a biblioteca e dar outro nome para ela
import random as apelido
novoDado = apelido.randint(1,100)
print(f'Você jogou o dado na mesa e o resultado foi', novoDado)
print(23*'-=')