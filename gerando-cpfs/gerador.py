from random import randint
cpf = str(randint(100000000, 999999999))

mask_cpf = cpf
reverse = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(mask_cpf[index]) * reverse

    reverse -= 1
    if reverse < 2:
        reverse = 11
        digit = 11 - (total % 11)

        if digit > 9:
            digit = 0
        total = 0
        mask_cpf += str(digit)

print(mask_cpf)