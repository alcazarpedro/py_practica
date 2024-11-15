from functools import reduce

def suma_list(elementos):
    out = reduce(lambda a,b: a+b,elementos)
    return out
elementos = list(range(1,11))
print(f'suma de todos los elementos es = {suma_list(elementos)}')