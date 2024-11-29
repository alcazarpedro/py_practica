
def invertir_datos(data):
    invertida={}
    for k,v in data.items():
        invertida[v]=k
    return invertida

data={
    'name': 'Pedro',
    'last_name': 'Alcazar',
    'age': 25,
    'status':'soltero',
    'email':'alcjimepedrol@example.com'
}  

out = invertir_datos(data)
print(out)
