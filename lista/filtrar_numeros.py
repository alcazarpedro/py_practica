
def filtrar_numero(numeros:list)->dict:
    diccionario_filtrar ={i:"par" if i % 2 == 0 else "impar" for i in numeros}
    return diccionario_filtrar

numeros =[12,1,3,4,5,6,7,22,9,10]
salida = filtrar_numero(numeros)
print(salida)            
