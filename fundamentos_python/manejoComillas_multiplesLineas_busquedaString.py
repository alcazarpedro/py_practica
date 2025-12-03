#Comillas dentro de comillas
print("Hola 'mundo'")
print('Hola "mundo"')

#Multipes lineas entre comillas triples
multiple = """ Hola 
mundo
:)
"""
ingles = "I'm Pedro"
print(ingles)
print(multiple)

#Contar palabras 
palabras = "universo"
print(len(palabras))

#Busqueda de palabras 
texto = "Todos somos un universo en los osjos del astronauta correcto"
estaIncluida= "universo" in texto
estaIncluida1 = "Universo" in texto
print(estaIncluida) # True
print(estaIncluida1) #False por (case sensity)
noestaIncluida = "galaxia" not in texto
print(noestaIncluida) #True

#Transformacion de texto
mayuscula = texto.upper()
minuscula = texto.lower()
print(mayuscula)
print(minuscula)


#La ultima asignacion prevalece
texto = texto.upper()
texto = texto.lower() 
print(texto) # output : minuscula

# limpieza de espacios 
frase = "   ojos correctos   "
sin_espacio = frase.strip()
print(sin_espacio)


