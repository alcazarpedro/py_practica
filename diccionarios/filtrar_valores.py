
def filtrar_values(datos):
    valores = []
    for i in datos:
        valores.append(datos[i])
    return valores

informacion={
    'name': 'Pedro',
    'last_name': 'Alcazar',
    'age': 25,
    'status':'soltero',
    'email':'alcjimepedrol@example.com'
}  
output = filtrar_values(informacion)
print(output)    