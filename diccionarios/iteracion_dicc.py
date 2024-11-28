

def iteracion(informacion):
    for k,v in informacion.items():
        informacion[k]= v
    return informacion

informacion={
    'name': 'Pedro',
    'last_name': 'Alcazar',
    'age': 25,
    'status':'soltero',
    'email':'alcjimepedrol@example.com'
}  

out = iteracion(informacion)
print(out)
