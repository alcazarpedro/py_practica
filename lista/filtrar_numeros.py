import random
def filtrar_numero(numeros:list)->dict:
    diccionario_filtrar ={i:"par" if i % 2 == 0 else "impar" for i in numeros}
    return diccionario_filtrar

numeros = random.sample(range(1,20),10)
salida = filtrar_numero(numeros)
print(salida)            
