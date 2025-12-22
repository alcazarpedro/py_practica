frutas = {"manzanas","naranja","mandarina","naranja"}
print(frutas)       #imprime toda el conjunto
print(type(frutas))  #dame como resultado el tipo de clase que pertence
print(len(frutas))    # imprime la longitud del conjunto
#Orden y mutabilidad
for item in frutas:
    print(item) #Puede salir en cualquier orden

#Mezclar tipos
conjunto = {"Frase",23,True}
print(conjunto)   #Orden no garantizado
print(type(conjunto))

#Verificar pertencia 
print("manzana" in frutas)
print("pera" in frutas)

#Agregacion con add y update
frutas.add("pera") #Agrega de a un elemento
frutas_tropicales = {"Piña","Mango"}
frutas.update(frutas_tropicales) #Agrega varios elementos / tambien funciona como lista o tupla
print(frutas)
#Eliminar
frutas.remove("mango") #Ok si "mango" esta; error si no
frutas.discard("pera")  # Ok este o no este pera

#Pop & Clear
elimidado = frutas.pop()  #elemina y devuelve un elemento aleatorio
print(elimidado)
frutas.clear              #Vacia por completo el conjunto
print(frutas)
#Operaciones entre conjuntos 
A = {"A","B","C"}
B = {"C","D","E"}
C_union = A.union(B)        #Todos los elementos de ambos conjuntos 
I_inter = A.intersection(B)  #Solos elementos en comun
D_diff = A.difference(B)     #Elementos de un conjuto que no esten en el otro

print(C_union)
print(I_inter)
print(D_diff)
