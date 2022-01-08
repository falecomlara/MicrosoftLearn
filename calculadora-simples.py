n1 = False
n2 = False
operacao = False

print('CALCULADORA SIMPLES')
while n1 is False:
    n1 = input('Primeiro Número: ')
    if n1.isnumeric() is False:
        print('ERRO! Você não digitou um número.')
        n1 = False
while n2 is False:
    n2 = input('Segundo Número: ')
    if n2.isnumeric() is False:
        print('ERRO! Você não digitou um número.')
        n2 = False
while operacao is False:
    operacao = input('Qual a operação? +, -, *, / ')
    if operacao == '+':
        print(n1, '+', n2, '= ', int(n1)+int(n2))
        exit()
    if operacao == '-':
        print(n1, '-', n2, '= ', int(n1)-int(n2))
        exit()
    if operacao == '*':
        print(n1, '*', n2, '= ', int(n1)*int(n2))
        exit()
    if operacao == '/':
        print(n1, '/', n2, '= ', int(n1)/int(n2))
        exit()
    else:
        print('ERRO! Escolha apenas +, -, * ou / ')
        operacao = False
