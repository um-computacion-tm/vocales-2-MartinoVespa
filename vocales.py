def contar_vocales(mi_string):
    vocales = ('a', 'e', 'i', 'o', 'u')
    resultado = {}
    mi_string = mi_string.lower()
    for letra in mi_string:
        # if letra in 'aeiou':
        if letra in vocales:
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1
    return resultado
