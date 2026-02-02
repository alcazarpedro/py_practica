"""
Dada una cadena con registros separados por ; y cada campo por ,, 
extrae solo los correos electrónicos y 
cambia el dominio @gmail.com por @empresa.com."""

def dominios(cadena:str) -> str:
    correos = [reg.split(',')[1].replace('@gmail.com','@empresa.com')for reg in cadena.split(";")]
    return correos

registros = "Juan,juan@gmail.com,MX;Maria,m@outlook.com,ES;Pedro,p@gmail.com,AR"
salida = dominios(registros)
print(salida)


