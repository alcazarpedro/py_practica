#importamos la funcion operaciones
'''import operaciones

print(operaciones.suma(12,56))
print(operaciones.resta(1200,345))
print(operaciones.multiplicacion(12,7))
print(operaciones.division(124,8))'''

#Otra forma de hacerlo es la siguiente usando from 

from operaciones import suma,resta,multiplicacion,division

print(suma(98,34))
print(resta(123,98))
print(multiplicacion(23,6))
print(division(12,4))
