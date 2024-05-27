from suma import *
from resta import *
from multiplicacion import *
from division import *
from suma_avanzada import *

def menu():
    while True:
        print("")
        print("CALCULADORA")
        print("-------------------------------")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Suma Avanzada")
        print("-------------------------------")

        opcion = int(input("¿Que acción quieres realizar? (Selecciona el número)"))

        if opcion == 1:
            suma()
        elif opcion == 2:
            resta()
        elif opcion == 3:
            multiplicacion()
        elif opcion == 4:
            division()
        elif opcion == 5:
            suma_avanzada()
        else:
            print("¡Adios!")
            break

menu()


