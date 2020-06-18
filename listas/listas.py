lista = ['A', 'B', 'C']

print(lista[1])

l1 = [1, 2, 3]
l2 = [4, 5 ,6]

l1.extend(l2) # juntando duas listas

print(l1)

l2.insert(0, 'banana') # inserindo um valor dando uma posição a ele

l2.append('b') # inserindo um novo valor na lista
print(l2)

l2.pop() # remove o ultimo valor da lista
print(l2)

l3 = [1, 2, 3, 4, 5, 6]
del(l3[3:5]) # removendo elementos da lista pelo indice
print(l3)
print()

l4 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(f'Maior: {max(l4)}, Menor: {min(l4)}') # encontrando o maior e o menor valor da lista

soma = 0
for valor in l4:
    soma += valor # somando todos os valores da lista 4

print(f'Soma: {soma}')
print()

l5 = ['Lucas', 18, 1.80, True]

for elemento in l5:
    print(f'{elemento}, {type(elemento)}') # encontrando o tipo de cada elemento na lista