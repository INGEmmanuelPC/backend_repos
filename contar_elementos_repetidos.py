lista_repetidos = [2, 3, 5, 7, 11, 13, 17, 2, 2, 29, 31, 37, 2, 43, 47]
def sin_duplicados(lista):
    vistos = set()
    resultado = []
    for x in lista:
        if x not in vistos:
            vistos.add(x)
            resultado.append(x)
    return resultado

lista = [3, 1, 2, 3, 2, 4, 1]
print(sin_duplicados(lista_repetidos))
