"""
Recibe una cadena con números separados por | 
y reemplaza solo los números pares por "X" manteniendo la estructura.
"""

def numeros_par(numeros:str)->str:
    elementos = numeros.split("|")  
    result = ["x" if int(i) % 2 == 0 else i for i in elementos]
    return "|".join(result)
        

cadena_numeros = "1|2|3|4|5|6|7|8|9"
salida = numeros_par(cadena_numeros)
print(salida)


