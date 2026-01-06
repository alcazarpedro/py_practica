# definir una funcion
def mi_funcion():
    print("Hola mundo desde una funcion")

# Invocar (Se ejecuta cada vez que se llama)
mi_funcion()
mi_funcion()
# Un argumento dentro de una variable
def saludar(nombre):
    print("Hola,", nombre )

#Invocamos la funcion
saludar("Pedro")
saludar("Arizaid")

#Varios argumentos y de orden estrictos
def saludar(nombre,apellido):
    print("Hola,", nombre , apellido )

#invocar 
saludar("Ariz","campos")
saludar("Clauida","Achis")

#Valores por defecto
def saludo(nombre,apellido = "", nacionalidad ="colombia"):
    #Ejemplo de personalizada
    if apellido:
        print(f'hola {nombre} {apellido} , eres de {nacionalidad}')
    else:
        print(f"hola {nombre},eres de {nacionalidad}")

#invocar 
saludo("Pedro","Alvarez","España")
saludo("Julieta", "Urica")
saludo("Ana")

#devolver un valor 
def suma(a,b):
    return a + b

#invocar 
resultado = suma(34,12)
print(resultado)


#pass
def x():
    pass #evitar un error mientras decides la logica
