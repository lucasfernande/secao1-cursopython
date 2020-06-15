nome = input('Digite seu nome: ')

if nome.isdigit():
    print('Erro: você não digitou seu nome')
else:
    if len(nome) <= 4:
        print('Seu nome é curto.')
    elif len(nome) >= 5 and len(nome) <= 6:
        print('Seu nome é médio.')
    else:
        print('Seu nome é grande')