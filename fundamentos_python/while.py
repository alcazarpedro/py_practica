#¿ Como contar del 1-9 & 1-10
i = 1
while i < 10:
    print(i)
    i+=1

#Cambiar la condicion para agregar el 10
while i <= 10:
    print(i)
    i+=1

#¿ Como afecta el orden del print e incremento ?
# Imprime del 2 al 11 por el orden de las instrucciones
while i <= 10:
    i+=1
    print(i)

#incrementa del 1 - 10 con incremento antes del print
x = 0
while x < 10 :
    x+=1
    print(x)

#¿ Como controlar el flujo del break y continue

# hace break en el 5 por la igualacion con la sentencia if 

while i <= 10:
    print(i)
    if i == 5:
        break
    i+=1

#Si evalúas la condición antes del print, el 5 no se imprime porque el break ocurre antes del print:
while i <= 10:
    if i == 5:
        break
    print(i)
    i+=1

'''¿Cómo saltar un valor con continue sin romper el bucle?
Caso correcto: incrementa antes de verificar y saltar el 5.'''
while x < 10:
    x+=1
    if x == 5:
        continue
    print(x)

#Caso problemático: usar continue antes de incrementar produce bucle infinito cuando i == 5, porque i nunca cambia.
while i < 10 :
    if i == 5:
        continue # i no incremneta y la condicion nunca cambia
    print(i)
    i+=1

#¿Cómo sumar de a dos y por qué no se llega al 5?
while i < 10 :
    print(i)
    i += 2

#¿Qué rol cumple else en while y qué mensajes muestra?
while x < 10:
    x += 1
    if i == 5:
        continue
    print(x)
else:
    print('i dejó de ser menor a diez')


