hora = input('Digite a hora atual: ')

if hora.isdigit():
    hora = int(hora)

    if hora <= 11:
        print('Bom dia.')
    elif hora <= 17:
        print('Boa tarde.')
    else:
        print('Boa noite.')
else:
    print('Erro: o valor digitado não era um número')