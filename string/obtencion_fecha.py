"""
A partir de una cadena que representa una fecha "2025-01-06 21:45:30", obtén:
Año
Mes
Hora
"""
def obtencion(fecha:str) -> str:
    año = fecha[0:4]
    mes = fecha[5:7]
    dia = fecha[8:10]
    hora = fecha[11:]
    return año,mes,dia,hora

fecha = "2025-01-06 21:45:30"
output = obtencion(fecha)
print(output)
