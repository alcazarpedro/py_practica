
def contar_vocales(palabra):
    vocales = 'aeiou'
    return sum(1 for vocal in palabra if vocal in vocales)

palabras = ['hola', 'programacion','python','ejemplo']

dict_vocales ={palabra:contar_vocales(palabra) for palabra in palabras}

print( dict_vocales)