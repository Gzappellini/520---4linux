
b = lambda x,y: x+y 

b(5,7)

(lambda x,y: x+y)(6,6)

def soma(x,y):
    return x+y

soma(5,7)
print(soma)

nomes = ['guilherme', 'zappellini']
result = map(lambda x: x.title(), nomes)

print(result)