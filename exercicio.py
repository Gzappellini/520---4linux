#abre o arquivo e atribui conteudo em uma variavel
with open('teste.txt', 'r') as arq:
    conteudo = arq.readlines()


#altera conteudo numerando itens
cont = 0
aux = []
for x in conteudo:
    aux.append('{}- {}'.format(cont, x)) 

#altera conteudo numerando itens
#conteudo = [f'{c+1}- {x}' for c, x in enumerate(conteudo)]

#reescreve contteudo antigo

with open ('teste.txt', 'w') as arq:
    arq.writelines(conteudo)


