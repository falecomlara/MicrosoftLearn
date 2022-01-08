print(type('Olá Mundo'))
print(type(7))
print(type(True))

print(1+1==3)
print(1+1==2)

print(20*'=-')

''' OPERADORES
==  Igualdade
!=  Desigualdade
>   Maior que
<   Menor que
>=  Maior ou igual a
<=  Menor ou igual a
'''

primeiro = 5
segundo = 0
verdadeiro = True
falso = False

if primeiro > 1 and primeiro < 10:
    print('O valor é entre 1 e 10')
if primeiro > 1 or segundo > 1:
    print('Pelo menos um valor é maior que 1')
print (verdadeiro, not verdadeiro)
print (falso, not falso)

if not primeiro > 1 and segundo <10:
    print('Os dois valores passaram no teste')
else:
    print('Os dois valores não passaram no teste')

