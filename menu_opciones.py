
import os

seguir = True
flag_saludo = False
flag_brindis = False

while seguir:

    os.system("cls")
    print("   *** Menu de Opciones ***  ")
    print("--------------------------------")
    print("1- Saludar")
    print("2- Brindar")
    print("3- Despedir")
    print("4- Salir")
    opcion = input("Ingrese opcion: ")

    match opcion:
        case "1":
            if flag_saludo:
                print(" Che ya no saludamos :")
            else:
                print("Hola")
                flag_saludo = True
        case "2":
            if flag_saludo:
                print("Chin Chin ")
                flag_brindis = True
            else:
                print("Antes de brindar primero Saluda:")
        case "3":
            if not flag_saludo:
                print(" Antes de despedirnos primero saludemonos ")
            elif  not flag_brindis:
                print(" Antes de despedirnos primero brindemos")
            else:
                print("Chau . Hasta la proxima ")
                flag_brindis = False
                flag_saludo = False
        case "4":

            confirma = input("Confirma Salida? :")
            seguir = not confirma == "s"
            #seguir = False if confirma == "s" else True
            print("Acabas de Salir del Programa :")
        case _:
            print("opcion invalida")


    if seguir:
         os.system("pause")

            