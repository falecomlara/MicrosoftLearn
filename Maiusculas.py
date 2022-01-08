nome = str(input('Escreva o seu nome: '))

print(nome.capitalize())
print(10* '-+')
print('Tudo minúsculo', nome.lower())
print('Tudo maiúsculo', nome.upper())
print('Apenas o primeiro maiúsculo', nome.title())
print('Inverte o tamanho que escreveu', nome.swapcase())
print(10* '-+')

print('Esse nome contém', len(nome), 'letras')
for n in nome:
    print('A Letra', n, 'é usada', nome.count(n), 'vez.')