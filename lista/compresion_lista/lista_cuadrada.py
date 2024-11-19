
def cuadrada(elementos):
    cuadrado_list =[i**2 for i in elementos]
    return cuadrado_list

elementos = [2,3,1,4,5,8,9,7]
out = cuadrada(elementos)
print(out)
