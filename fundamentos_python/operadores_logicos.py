#Operadores de comparacion
x = 5
y = 4
z = 5
print(x == y ) # igualdad = False
print(x != y)  # diferencia = True
print(x > y)   # mayor a = True
print(x < y)   # menor a = False
print(x >= z)   # mayor o igual a = True
print(x <= y )   # menor o igual = False
print(x <= z)    # menor o igual = True


#Comparacion And & Or

print((x == y) or (x == z)) # True si se cumple al menos una condicion
print ((x < y) and (x == z)) # True si se cumplen las dos condiciones = False

print((x == y) or ( x > z)) # Ejemplo con mayor para mantener la comprobacion

# Negacion con Not 
estado = True
print(not(estado)) # False

estado = False
print(not(estado)) #True

# Negar una comparacion
print(not(x == y)) # True si x no es igual a y

