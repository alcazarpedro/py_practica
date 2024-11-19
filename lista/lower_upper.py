
def upper_texto(cadena):
    cadena_upper=[]
    for elemetos in cadena:
        elemetos = elemetos.upper() 
        cadena_upper.append(elemetos)
    return cadena_upper

cadena = ['dios','te','bendiga']
out = upper_texto(cadena)
print(out)    