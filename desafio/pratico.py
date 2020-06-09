nome = 'Lucas'
idade = 18
altura = 1.80
peso = 72

anoAtual = 2020

anoNasc = anoAtual - idade

imc = peso / altura  ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O imc de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {anoNasc}')