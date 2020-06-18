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