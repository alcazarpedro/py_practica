auto = {
    'marca': 'Renault',
    'modelo': 'clio',
    'año': 2025
}
print(auto)
#Acceder a clave y valores con get y corchetes
print(auto['marca'])
print(auto.get('modelo'))
#Claves y Valores
print(auto.keys()) #clave
print(auto.values()) #valores
#modificar,agregar, Actualizar(update)
#Modificando un valor existente
auto['año'] = 2021
#Agregar un nuevo par de clave - valor
auto['color'] = 'negro'
print(auto)
#Update puedes modificar y agregar en una sola linea
auto.update({'marca': 'Ram','puertas': 4})
print(auto)
#Verificar existensias y sensibilidad con las mayusculas con in
if 'marca' in auto:
    print('marca es una de las propiedad de este diccionario')

if 'MARCA' in auto:             #Sensibilidad a las mayusculas
    print("No se imprime ")

#Eliminar , recorrer , incluso  anidado un diccionario
#eliminar por clave
#auto.pop('puertas')
#eliminar el ultimo por insertado
#auto.popitem()
#vaciar el diccionario por completo
#auto.clear()
#print(auto)
#recorrer claves,valores,parejas por for item
#solo claves
for k in auto:
    print(k)
#solo por valores
for v in auto:
    print(v)
#Clave , valor 
for k,v in auto.items():
    print(k,v)
#Diccionario anidado
familia = {
    'hijo uno': {'nombre':'Hume', 'edad':9},
    'hijo dos': {'nombre': 'Pedro', 'edad': 12},
    'hijo tres': {'nombre': 'Juan','edad':10}
}  

print(familia['hijo uno']['nombre'])


