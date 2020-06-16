"""
i = 1

while i <= 10: # contando até 10
    print(i)
    i += 1
    
"""

while True:
    print()
    x1 = input('Digite um número: ')
    x2 = input('Digite um segundo número: ')


    if not x1.isnumeric() or not x2.isnumeric():
        print('Você precisa digitar apenas números')
        continue
    else:
        x1 = int(x1)
        x2 = int(x2)

        op = input('Digite o operador(+, -, *, /): ')

        if op == '+':
            res = x1 + x2
            print(f'Resultado: {res}')
        elif op == '-':
            res = x1 - x2
            print(f'Resultado: {res}')
        elif op == '*':
            res = x1 * x2
            print(f'Resultado: {res}')
        else:
            res = x1 / x2
            print(f'Resultado: {res}')