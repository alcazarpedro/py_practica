
def keys_invertidas(datos):
    dicc_invertido = {k:v[::-1] for k,v in datos.items() }
    return dicc_invertido

palabras ={
    'programacion':'python',
    'libro':'ingles',
    'pink':'white'
}

out = keys_invertidas(palabras)
print(out)