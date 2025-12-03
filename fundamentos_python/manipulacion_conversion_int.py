x = 5
y = 5.5
z = 5j
# tipo de dato
print(type(x))
print(type(y))
print(type(z))

#casceo de entero a float

xf = float(x)
print(type(xf))
print(xf)

#casceo de flotante a entero

xe = int(y)
print(type(xe))
print(xe)

#casceo de entero y flotante a complejo
entero = 5
flotante = 5.5

enteroComplejo = complex(entero)
print(type(enteroComplejo))
print(enteroComplejo)
flotanteComplejo = complex(flotante)
print(type(flotanteComplejo))
print(flotanteComplejo)

#Aleatrios
import random
print(random.randrange(1,11)) # output : numero aletorio entre 1 y 10 
