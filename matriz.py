Matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9] 
]
cont = 0
soma = 0

for m in Matriz:
    soma += m[cont]
    cont += 1
    soma += m[-cont]
    
print(soma)






