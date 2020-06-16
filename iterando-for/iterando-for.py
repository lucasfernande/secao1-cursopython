texto = 'python'
novo = ''

for letra in texto:
    print(letra)

for letra in texto:
    if letra == 'p':
        novo += letra.upper()
    elif letra == 'n':
        novo += letra.upper()
    else:
        novo += letra

print(novo)