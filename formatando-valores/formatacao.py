"""
# limitando a quantidade de casas decimais

num1 = 10
num2 = 3

div = num1/num2
print(f'{div:.2f}')
"""
"""
num = 1
print(f'{num:0>10}')
print(f'{num:0<10}')
print(f'{num:0^10}')

num_float = 1005
print(f'{num_float:.2f}')
"""

nome = 'lucas'

print(f'{nome:*>10}')
print(f'{nome:*<10}')
print(f'{nome:*^10}')

nome_format = '{:@>10}'.format(nome)
print(nome_format)

