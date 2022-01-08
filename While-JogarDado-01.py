import random

dado = 0
contador = 0
resultado = 0

resultado = int(input('Digite um número de 1 a 100: '))
while resultado > 100 or resultado < 1:
    resultado = int(input('Digite um número de 1 a 100: '))

while dado != resultado:
    contador = contador +1
    dado = random.randint(1,100)
    print('Você jogou o dado', dado)
print('Você precisou jogar', contador, 'vezes para conseguir o resultado', resultado)