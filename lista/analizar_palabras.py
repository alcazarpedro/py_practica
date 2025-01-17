def  analizar_palabra(elementos):
    len_elementos=[len(i) for i in elementos]
    palabra_larga = len_elementos[0]
    for i in range(1,len(elementos)):
        if len_elementos[i] > palabra_larga:
            palabra_larga = len_elementos[i]

    palabra_corta = len_elementos[0]
    for i in range(1,len(elementos)):
        if len_elementos[i] < palabra_corta :
            palabra_corta = len_elementos[i]

    letras_unicas = set("".join(elementos))        

    diccionario_palabras = {
        'palabra_larga': palabra_larga,
        'palabra_corta': palabra_corta,
        'letras_unicas': letras_unicas
    } 
    for k,v in diccionario_palabras.items():
        diccionario_palabras[k] = v               
    return diccionario_palabras

elementos = ['constitucion','dolor','politica','amor','anticonstitucionalidad']
salida = analizar_palabra(elementos)
print(salida)   

        