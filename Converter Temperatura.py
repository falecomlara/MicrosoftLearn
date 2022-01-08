valor = False
fahrenheit = 0

while valor is False:
    valor = input('Qual a temperatura em Fahrenheit? ')
    if valor.isnumeric() is False:
        print('ERRO! Digite um número.')
        valor = False
    fahrenheit = int(valor)
print('Temperatura em Celsius é', (fahrenheit-32)*(5/9))
