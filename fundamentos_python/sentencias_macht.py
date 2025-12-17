# Python 3.10

dia = 1

match dia :
    case 1:
        print("Hoy es Lunes")
    case 2:
        print("Hoy es Martes")    
    case 3:
        print("Hoy es Miercoles")
    case _ : 
        print("No coincide con los valores establecidos") #Atrapa cualquier caso que no este referenciado


# Ejercicio

txt = input("Escribe un dia de la semana de Lunes - Viernes: __ ").capitalize()

match txt :
    case "Lunes":
        print("Ir al gym de 8.00am")
    case "Martes":
        print("bruch con la gerencia a las 9.30 am")
    case "Miercoles":
        print("coferencia de plan 2026 a las 7:30 am ")
    case "Jueves":
        print("dia normal")
    case "Viernes":
        print("horario normal")
    case _ :
        print("Descanso...")



