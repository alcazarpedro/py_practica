
def igualdad(lista_a,lista_b):
    comunes = []
    for i in lista_a:
        if i in lista_b:
            comunes.append(i)
    return comunes

lista_a =[1,2,3,4,5]
lista_b=[6,2,5,1,7]
out = igualdad(lista_a,lista_b)
print(out)        
