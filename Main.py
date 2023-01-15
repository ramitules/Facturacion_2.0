import os
from funciones import *
from Facturas import menu_facturas

while True:
    os.system("cls")
    print("Bienvenido!\n")
    print("Elija una opcion")
    print("1. Facturas")
    print("2. Clientes")
    print("3. Articulos")
    print("0. Salir")
    print("\nOpcion: ", end = '')
    opc = int(input())

    if opc == 0: break
    elif opc == 1: menu_facturas()
    elif opc == 2: menu_clientes()
    elif opc == 3: menu_articulos()
    else: input('Opcion incorrecta, presione ENTER y vuelva a intentar')

input('Gracias por utilizar este programa! Presione ENTER para salir')