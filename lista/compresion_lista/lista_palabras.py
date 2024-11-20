


def letter_list(cadena):
    new_list =[i[0] for i in cadena]
    return new_list
cadena = ['lista','objeto','palabra']
out=letter_list(cadena)
print(out)
