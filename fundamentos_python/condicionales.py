#¿Que pasa si las condicion es True o False?
if 5 > 3 :
    print("5 es mayor que 3") # True

#False : no imprime
if 2 > 3 :
    print("2 es mayor que 3")

#¿Como usar variables al mismo nivel en el if ?

x = 6
y = 4

if x > y :
    print('x es mayor que y ') # Se ejecuta

if x < y :
    print('x es menor que y ') # No se ejecuta

#¿Cuando aplicar es para la alternativa?

a = 5
b = 5

if a > b :
    print("a es mayor que b ")
else: 
    if a == b:
        print("a es igual a b")
    else : 
        print("No se cumplio ninguna de las anteriores")

#¿Como combinar condiciones con and & or ?
x = 6
y = 4
z = 1

# And
if x > y and x > z :
    print('x es mayor que y  & x mayor que z') # Ambas son verdadares 
else:
    print("No se cumplio ninguna de las anteriores")    

# or 
f = 10
if x > y or x > f:
    print('x es mayor que y o x mayor que f') # al menos se cumple una
else:
    print("No se cumple ninguna ")

#¿Como comprar texto con if y anidar?

d = 'Python'
c = 'Javascript'
e = 'Python'

# igualdad y diferencia 

if a == b :
    print("a es igual a b")
else : 
    print('a no es igual a b')

#comparacion con anidacion
if a == c :
    if a != b :
        print("a es igual a c , pero, difernte a b ")
    else:
        print("Estoy saliendo por el if interno")
else:
    print("a no es igual a c")

#¿Para que sirve el statement pass en un if vacio?

e = 10
f = 10

if e == f :
    pass # placeholder temporal para no romper la ejecucion
