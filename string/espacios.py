"""
Dado un texto con múltiples espacios entre palabras,
normaliza el texto para que tenga un solo espacio entre cada palabra."""

def quitar_espacios(texto:str) -> str:
    return texto.replace("  "," ")
    

texto = "La  curiosidad   es  la  llave  que  abre  todas  las puertas del conocimiento."

salida = quitar_espacios(texto)
print(salida)

print(texto)
