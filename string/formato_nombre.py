"""
De una cadena con nombres en formato "APELLIDO_NOMBRE", 
genera una nueva cadena en formato "Nombre Apellido" 
respetando mayúsculas y minúsculas.
"""

def cambiar_formato(nombre:str) -> str:
    return nombre.replace("_"," ").capitalize()

registro = "PEDROLUIS_ALCAZAR"
salida = cambiar_formato(registro)
print(salida)
