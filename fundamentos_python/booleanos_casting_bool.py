v = True
f = False
print(v)
print(f)

print(5 > 3)
print(3 > 5)

#casting a bool

print(bool("hello world")) # String con contenido -< True
print(bool(1)) # int con contenido -> True
print(bool([1,2,4])) # True -> lista con valores

print(bool(" ")) #String vacio -> False
print(bool(0)) # Cero es -> False
print(bool([])) # False
print(bool(None)) # False

x = 4
print(isinstance(x, int)) # True -> es entero

y = 1.2
print(isinstance(y,int)) # False -> es flotante

