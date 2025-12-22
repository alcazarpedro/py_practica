frutas = ["Manzanas","Naranja","Banana"]
print(frutas)    #imprime toda la lista completa
print(type(frutas)) #clase que pertenece 
print(frutas[1])     #imprime el indice que indica de la lista = "Naranja", pero empieza desde 0

#Modificar por indices (Mutabilidad)
frutas[1] = "Fresa"
print(frutas[1])
print(frutas)
#Duplicados
frutas.append("Naranja")  #Ahora hay otra naranja al final
print(frutas)
#Mezclar tipos y medir el largo
mixta = ["Tunombre",26,False]
print(mixta)
print(type(mixta))
print(len(frutas))
print(len(mixta))
#indices 
#Suponiendo frutas = ['manzanas','fresa','banana','naranja]
print(frutas[0:2])   #['manzana','fresa']
print(frutas[:2])     #['manzana','fresa']
print(frutas[1:])     #['manzana','fresa','banana']
#Uso del in
if "Naranja" in frutas:
    print("La Naranja esta dentro de la lista de frutas")
#Agregar,eliminar,ordenar
vehiculos = ["autos","moto","avion"]
#Agregar al final
vehiculos.append("barco")
#Insertar por indice (desplaza lo que sigue)
vehiculos.insert(1,"bicicleta")
#Eliminar por valor
vehiculos.remove("auto")
#Eliminar por indice
vehiculos.pop(1)

#Ordenar alfabeticamente
vehiculos.sort()
# Orden invertido
vehiculos.reverse()
#unir listas + & extend
coleccion1=[1,2,3]
coleccion2 =[4,5,6]
#Concatenar con +
coleccion3 = coleccion1 + coleccion2
print(coleccion3)
#extend
coleccion1.extend(coleccion2)
print(coleccion1)

     


