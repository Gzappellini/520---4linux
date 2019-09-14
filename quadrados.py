#fazer uma função anonima para calcular os 10 primeros quadrados peerfeitos

#quadrados = map(lambda x: x ** 2, range(1,11))

#print(list(quadrados))

quadrados = [(lambda x: x ** 2)(y) for y in range(1,11)]
print(quadrados)