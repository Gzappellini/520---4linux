
qtd = int(input('quantidade de notas: '))

soma = 0

for x in range(qtd):
    nota = float(input('nota{}: '.format(x+1)))
    soma += nota

m = soma / qtd

print("Media final: {}".format(m))
