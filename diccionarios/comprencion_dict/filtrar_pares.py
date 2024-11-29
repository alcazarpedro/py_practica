
def filtrar_valores_pares(data):
    dicc_pares={k:v for k,v in data.items() if v % 2 ==0}
    return dicc_pares

ticekt_compra = {
    'pan': 18,
    'detergentes': 101,
    'verduras': 98,
    'soda':24,
    'postres':440,
    'higiene':122
}

out = filtrar_valores_pares(ticekt_compra)
print(out)
