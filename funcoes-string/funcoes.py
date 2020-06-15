string = input('Digite um número: ')
string2 = input('Digite outro: ')

# isnumeric, isdigit e isdecimal

if string.isdigit() and string2.isdigit():
    string = int(string)
    string2 = int(string2)

    print(f'Resultado: {string+string2}')
else:
    print('Erro: Digite apenas números')