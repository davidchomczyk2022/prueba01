
#A) Para ello se cargarán los siguientes datos hasta que el usuario lo decida:
#* Nombre
#* Monto en pesos de la operación (no menor a $10000)
#* Cantidad de instrumentos
#* Tipo (CEDEAR, BONOS, MEP)

#B) Luego del ingreso mostrar en pantalla todos los datos.

#C) Realizar los siguientes informes:
#1. Tipo de instrumento que más se operó.
#2. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron
#más de $50000.
#3. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP,
#que menos dinero invirtió. Puede ser más de uno.
#4. Nombre de los usuarios que invirtieron en CEDEAR, cuya inversión supere el
#monto promedio
#5. Porcentaje de usuarios que no invirtieron en MEP, siempre y cuando el monto
#no supere los $50000.

#PUNTO  A)
#seguir = 'si'
indice = 0
import os
nombres = ["juan","lucia","carlos","analia","mario"]
monto_pesos = [10000,13000,15000,21000,14000]
cantidad_instrumentos = [5,12,45,23,32]
tipos = ["cedear","cedear","mep","bono","mep"]
flag = 0

# while True:
    # nombre = input("Ingrese su Nombre :")
    # nombres.append(nombre)
    # try :
    #     monto_pesos = int(input("Ingrese un Valor no menos a 10000 :"))
    #     break
    # except:
    #     print("eso no es un numero ")
    # if monto_pesos >= 10000 :
    #     break
    # else:
    #     print("Monto Invalido")
    # cantidad_instrumento = int(input("Ingrese Cantidad de Instrumentos :"))
    # tipo = input("Seleccione tipo : 'CEDAR','BONOS','MEP' :")
    # while tipo !='CEDAR' and  tipo!='BONOS' and tipo!='MEP':
    #     tipo = input("ERROR Seleccione tipo : 'CEDAR','BONOS','MEP' :")
    # seguir = input("desea continuar? s / n :").lower()
    
    # if seguir !="s":
    #     break


# INFORMES C)
os.system("cls")

for numero in monto_pesos:
    if flag == 0:
            mayor = numero
            indice_mayor = indice
    else:
        if numero > mayor:
            mayor = numero
            indice_mayor = indice
    indice +=1
print(mayor,indice_mayor)


print("     *****Listas de Inverciones *****")
print("  Nombres     Monto     Cantidades      Tipos  ")

for i in range(5):
    print(f"  {nombres[i]:<10}  {monto_pesos[i]}        {cantidad_instrumentos[i]:02d}          {tipos[i]:>5}")

# for indice in range(len(nombres))
#     print(nombres[indice])


# for elemento in nombres:

#     print(elemento)



# print(nombres)
# print(monto_pesos)
# print(cantidad_instrumentos)
# print(tipos)
