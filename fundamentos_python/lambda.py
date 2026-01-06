#Definir la funcion 
# lamba expresion : argumentos
x = lambda b : b + 10

#invocar 
print(x(5))

# Dos argumentos en lambda
y = lambda a,b : a+b

print(y(14,12))

# dentro de una funcion

def mi_funcion(n):
    return lambda a : a * n

# Duplicar y triplicar

duplicador = mi_funcion(2)
triplicador = mi_funcion(3)

print(duplicador(5))
print(triplicador(5)) # el argumento 5 actua como a dentro de la lambda



