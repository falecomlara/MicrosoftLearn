n1 = False
n2 = False

while n1 == False:
    n1 = input('Digite primeiro número: ')
    if n1.isnumeric() == False:
        print('ERRO! Você não digitou um número.')
        n1 = False
while n2 == False:
    n2 = input('Digite segundo número: ')
    if n2.isnumeric() == False:
        print('ERRO! Você não digitou um número')
        n2 = False
print(n1, '+', n2, '=', int(n1)+int(n2))
