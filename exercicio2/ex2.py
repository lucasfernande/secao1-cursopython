hora = input('Digite a hora atual: ')

if hora.isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('O horário deve estar entre 0 e 23')
    else:
        if hora <= 11:
            print('Bom dia.')
        elif hora <= 17:
            print('Boa tarde.')
        else:
            print('Boa noite.')
else:
    print('Erro: o valor digitado não era um número')