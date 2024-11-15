
def longitud(lista):
    lon = []
    for i in lista:
        lon.append(len(i))
    return lon

lista = ['frase','cadena','string']
output = longitud(lista) 
print(output)   