nome = input('Digite seu nome: ')
len = len(nome)

if nome.isdigit():
    print('Erro: você não digitou seu nome')
else:
    if len <= 4:
        print('Seu nome é curto.')
    elif len >= 5 and len <= 6:
        print('Seu nome é médio.')
    else:
        print('Seu nome é grande')