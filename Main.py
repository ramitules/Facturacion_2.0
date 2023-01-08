import os
from tkinter import *
from MenuClientes import menu_clientes
from MenuFacturas import menu_facturas
from MenuArticulos import menu_articulos

ventana = Tk()
ventana.wm_title('Facturacion textil')


ventana.mainloop()

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