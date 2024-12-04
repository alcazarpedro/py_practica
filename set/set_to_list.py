
def conversion_to_list(elementos:set) -> list:
    lista_ordenada = list(elementos)
    return lista_ordenada

elementos = {1,2,3,4,5,6,7,8,9,10}
out = conversion_to_list(elementos)

print(f'lista ordenada: {out}')
