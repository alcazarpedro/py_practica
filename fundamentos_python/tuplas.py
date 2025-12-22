tecnologias = ("Python","Javascript","Go")
print(tecnologias)   #imprime toda la tupla
print(tecnologias[1]) #imprime el valor del indice especificado = "Javascript"
#Duplicados & contar elementos
tecnologias = ("Python","Javascript","Go","Python")
print(tecnologias)
print(len(tecnologias))
#Tipos 
print(type(tecnologias))
fruta = ("manzana")   #Sin coma al final es String
print(type(fruta))
fruta = ("manzana",)  #Con coma al final es una Tupla
print(type(fruta))
#Mezclar tipos 
tupla = ("Verbo",4,True)
print(tupla)
print(type(tupla))
#Desempaquetar Tupla
x,y,z = tupla
print(x,y,z)     # "Verbo", 4 , True
#Concatenar y duplicar 
tupla1= (1,2,3)
tupla2 = (4,5,6)
tupla3 = tupla1 + tupla2
print(tupla3)
print(tupla3 * 2) #duplicar la tupla
#Recorrer y Modificar

for item in tupla3:
    print(item)

tupla_a_modificar = ("Python","Java","Go")
lista_comidin = list(tupla_a_modificar)
lista_comidin.append("React")
tupla_a_modificar = tuple(lista_comidin)
print(tupla_a_modificar)


