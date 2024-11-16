import random
def pares(elementos):
    numeros_pares =[]
    for i in elementos:
        if i % 2 ==0:
            numeros_pares.append(i)
    return numeros_pares

elementos =[random.randint(1,50) for _ in range(15)]
out= pares(elementos)
print(out)        