
def lista_duplicados(elementos):
    nueva_lista = []
    for i in elementos:
        if  i not in nueva_lista:
            nueva_lista.append(i)
    return nueva_lista

elementos = [10,5,6,7,2,1,4,6,5,2]
out = lista_duplicados(elementos)
print(out)        

