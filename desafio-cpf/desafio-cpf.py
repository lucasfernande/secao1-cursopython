while True:
    cpf = input('Digite um CPF: ')

    if not cpf.isdigit():
        print('Digite apenas números')
    else:
        mask = cpf[:9]
        reverse = 10
        total = 0

        for index in range(19):
            if index > 8:
                index -= 9

            total += int(mask[index]) * reverse

            reverse -= 1
            if reverse < 2:
                reverse = 11
                digit = 11 - (total % 11)

                if digit > 9:
                    digit = 0
                total = 0
                mask += str(digit)

        if cpf == mask:
            print('CPF válido')
        else:
            print('CPF inválido')
