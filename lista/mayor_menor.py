
def mayor(elementos):
    numero_mayor = elementos[0]
    for i in range(1,len(elementos)):
        if elementos[i] > numero_mayor:
            numero_mayor = elementos[i]
    return numero_mayor

def menor(elementos):
    numero_menor=elementos[0]
    for i in range(1,len(elementos)):
        if elementos[i]<numero_menor:
            numero_menor = elementos[i]
    return numero_menor


elementos = [2,3,90,1,52,12,34,13,87,123]   
out = mayor(elementos)
print(f'numero mayor de la lista >_{out}')  
output =menor(elementos)
print(f'el numero menor de la lista <_{output}')   
