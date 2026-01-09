#Estructura
try:
    print("intentamos algo")
except:    
    print("captura un error")

# Sin manejo
#resultado = 10/0 #Provoca un error ZeroDivision

# Con manejo de error
try: 
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("No se puede divir por cero")

# Sin manejo 
# print(x) # Provoca un error Nameerror

#Con manejo especifico:
'''try:
    print(a)
except NameError:
    print("La variable no esta definida")
#Agregamos finally
finally:
    print("esto siempre se ejecuta")'''


# Sin error
x = 1
try :
    print(x)
except NameError:
    print("Esta variable no esta definoda")
finally:
    print("Esto siempre se ejecuta")
