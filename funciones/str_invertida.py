def cadena_invertida(texto):
    texto = texto[::-1]
    return texto

texto = 'python'
output=cadena_invertida(texto)
print(f'txt original >> {texto} --> txt invertido <<< {output}')