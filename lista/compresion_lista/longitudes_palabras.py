
def longitud_palabra(elementos):
    longitudes=[len(i) for i in elementos]
    return longitudes

elementos = ['palabras','Magdiel','Pedro','Rust','Python','Pandas','Saiden']
output = longitud_palabra(elementos)
print(output)