
def interseccion_set(set_x,set_y):
    interseccion= set_x.intersection(set_y)
    return interseccion

set_x = {1,2,3,4,5,6,7}
set_y = {2,4,8,9,10,1,0}
out = interseccion_set(set_x,set_y)
print(f'interseccion : {out}')