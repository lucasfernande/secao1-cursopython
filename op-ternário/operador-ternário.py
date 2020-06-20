idade = input('Qual a sua idade?: ')
idade = int(idade)

check = (idade >= 18)

msg = 'Pode acessar' if check else 'Não pode acessar'

print(msg)