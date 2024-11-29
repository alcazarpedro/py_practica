
def delete_dicc(datos):
    return datos.pop('status')

datos={
    'name': 'Pedro',
    'last_name': 'Alcazar',
    'age': 25,
    'status':'soltero',
    'email':'alcjimepedrol@example.com'
} 


print(delete_dicc(datos))
    
