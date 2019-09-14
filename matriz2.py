matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9] 
]

def soma_matriz(matriz:list)-> int:
    
    """
    calcula a soma das diagonais de uma matriz.

    :parametro: matriz
    :return: soma
    """
    cont = 0
    soma = 0

    for m in Matriz:
        soma += m[cont]
        cont += 1
        soma += m[-cont]
    return soma






