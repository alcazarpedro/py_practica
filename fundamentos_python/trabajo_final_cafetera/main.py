#importamos la funcion de los otros modulos
from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import ver_historial
#Definimos una funcion

def main():
    while True:
        #mostrar el menu
        mostrar_menu()

        #pedir la opcion al usuario
        opcion = input("Seleccione una opcion : ")

        if opcion == "1":
            #pedir un cafe (logica ampliada mas adelante)
            pedir_cafe()
            
        elif opcion == "2":
            #ver el historial (se implementara leyendo un archivo)
            ver_historial()
            
        elif opcion == "3":
            #Salida
            print("\n Muchas gracias por haber tomado nuestros riquisimos cafes")
            break
        else:
            print("Opcion invalida. indique una de las opciones que se muestre en el menu")

if __name__ == "__main__":
    main()
