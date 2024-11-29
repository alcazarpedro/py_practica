
def longitudes_listas(listas):
    dicc_longitudes = {c:len(v) for c,v in listas.items()}
    return dicc_longitudes

listas ={
    'calificaciones_mate': [7,6,9,10,8],
    'calificaciones_historia':[9,9,8,8,10,7],
    'taller_calificacion':[9,9,9,8,6,7,7,7]
}

output = longitudes_listas(listas)
print(output)
    


                           