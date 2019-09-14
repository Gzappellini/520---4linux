#abre o arquivo e atribui conteudo em uma variavel
with open('teste.txt', 'r') as arq:
    conteudo = arq.readlines()

print(conteudo)
#altera conteudo numerando itens
cont = 0
aux = []
for x in conteudo:
    aux.append('{}- {}'.format(cont, x)) 
    cont += 1
print(aux)


#altera conteudo numerando itens
#conteudo = [f'{c+1}- {x}' for c, x in enumerate(conteudo)]

#reescreve conteudo antigo

with open ('teste.txt', 'w') as arq:
    arq.writelines(aux)


