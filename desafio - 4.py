'''
Ramificar a execução do código com base na entrada do usuário
'''

print ('Você gostaria de continuar? [s/n] ')
valor = str.capitalize(input())
print (valor)

if valor == 'S':
    print('Continuando')
elif valor == 'N':
    print('Saindo')
else:
    print('Comando inválido')

print('Fim')