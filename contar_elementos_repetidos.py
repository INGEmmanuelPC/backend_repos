contador = 0
lista_repetidos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
def contar_elementos_repetidos(lista):
    global contador
    for elemento in lista:
        if elemento in lista_repetidos:
            contador += 1
    return contador
print(contar_elementos_repetidos(lista_repetidos))
