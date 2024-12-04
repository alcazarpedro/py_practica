
def set_len(conjunto:set)-> int:
    numeros_set = len(conjunto)
    return numeros_set

conjunto = {1,2,3,45,6,7}
out= set_len(conjunto)
print(f'cantidad de elementos : {out}')
