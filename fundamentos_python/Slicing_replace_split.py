#slicing 
texto = "Esto es un texto"

print(texto[0])
print(texto[4])

print(texto[0:4])
print(texto[0:15]) #Corta antes de terminar el texto completo faltaria la o
print(texto[0:]) #una de las formas correctas para obtener toda la oracion
print(texto[:7]) #el inicio hasta el "es"
print(texto[5:]) # Comienza desde el "es" hasta el final
print(texto[5:-2]) # tambien podemos usar negativos cuentas del final asi atras

#replace

curso = "Este es un curso de Javascript"
remplazo = curso.replace("Javascript", "Python")
print(remplazo)

#Split
separador = texto.split(" ")
print(separador)

#Normalizacion 
frase = "Este texto contiene MAYUSCULAS y minusculas"
mayusculas = "mayusculas".lower() in frase.lower()
print(mayusculas)

