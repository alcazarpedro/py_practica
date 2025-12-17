#Iterar cadenas de texto
txt = "Python"
for letra in txt:
    print(letra)

#Iterar una lista

frutas = ["Manzana", "Fresa","Piña"]
for fruta in frutas:
    print(fruta)

#Como hacer break, continue,else en el for 

for fruta in frutas:
    if fruta == "Piña":
        break
    print(fruta)

#Continue
for fruta in frutas:
    if fruta == "Fresa":
        continue
    print(fruta)
else:
    print("Hemos terminado el bluce for") #Agregamos el else


#Iterar numeros con raange
print("-+-+-+-+-+-+-++-+++-++---+")

for i in range(10):
    print(i)

#con inicio y fin 
for variable in range(3,5):
    print(variable)

# con salto de numero

for x in range(1,11,2):
    print(x)

# for anidado
verduras = ["Tomate","pimiento","cebolla"]
adjetivos = ["Saludables", "Ricos en vitaminas"]

#Ejercico/ ejemplo
for verdura in verduras:
    for adjetivo in adjetivos:
        print(verdura,adjetivo)


