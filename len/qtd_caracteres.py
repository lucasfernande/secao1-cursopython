"""""
usuario = input('Digite seu nome de usuário: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('O usuário precisa ter pelo menos 6 letras')
else:
    print('Usuário cadastrado')
"""

ex1 = input('Digite alguma coisa: ')
ex2 = input('Digite outra:  ')

print(f'O total de caracteres foi: {len(ex1) + len(ex2)}')