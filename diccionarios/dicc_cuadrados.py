
def dict_cuadrados(dicc):
    cuadrados_dicc = {}
    for k,v in dicc.items():
        cuadrados_dicc[k]= v**2
    return cuadrados_dicc

dicc = {
    1:1,
    2:2,
    3:3,
    4:4,
    5:5
}
output = dict_cuadrados(dicc)
print(output)

