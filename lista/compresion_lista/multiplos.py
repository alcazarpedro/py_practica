
def multiplo(elemento):
    if elemento % 3 ==0:
        return True
    return False


def lista_multiplo(numeros):
    impares=list(filter(multiplo,numeros))
    return impares

numeros = [2,1,3,4,5,6,7,8,12,11,10,9]
out = lista_multiplo(numeros)
print(out)
