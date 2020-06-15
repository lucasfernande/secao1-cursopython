print('Ímpar ou par?')
print()

num = input('Digite um número: ')

if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print('O número é par')
    else:
        print('O número é ímpar')
else:
    print('Erro: o valor digitado não é um número')