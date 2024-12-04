
def difference_set(set_a:set,set_b:set) -> set:
    diferencia = set_a.difference(set_b)
    return diferencia

set_a = {3,2,1,4,5,6,7}
set_b = {1,2,3,56,67,12,4}
output = difference_set(set_a,set_b)

print(f'diferencia : {output}')
