try:
    qtd = int(input('quantidade de notas: '))

    soma = 0

    for x in range(qtd):
        nota = float(input('nota{}: '.format(x+1)))
        if nota >10:
            continue
        soma += nota

    m = soma / qtd

    print("Media final: {}".format(m))

except Exception:
    print('falha!')



