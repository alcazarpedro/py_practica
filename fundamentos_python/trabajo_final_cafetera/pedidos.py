ARCHIVO_PEDIDOS = "pedidos.txt"
def pedir_cafe():

    print("\nElige el cafe de tu agrado: ")
    print("1. Espresso")
    print("2. Latte")
    print("3. Capuccino")
    print("4. Americano")

    opcion = input("Elige una opcion que prefieras:  ")


    cafes = {
        "1" : "Espresso",
        "2" : "Latte",
        "3" : "Capuccino",
        "4" : "Americano"
    }

    if opcion  in cafes: # Valida contra las keys
        cafe_elegido = cafes[opcion]
        print(f"Has pedido un {cafe_elegido}.  estasmos preparando tu cafe")
        #escritura modo append con utf-8
        with open(ARCHIVO_PEDIDOS,"a",encoding="utf-8") as archivo:
            archivo.write(cafe_elegido + "\n")
    else:
        print("Opcion no valida, Por favor intenta de nuevo")
                




    