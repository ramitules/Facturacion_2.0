import os
from Facturas import crear_factura, resumen

def menu_facturas():
    while True:
        os.system("cls")
        print("Elija una opcion")
        print("1. Crear factura")
        print("2. Resumen semanal")
        print("3. Resumen mensual")
        print("0. Volver al menu principal\n")
        opc = input('Opcion: ')

        if opc == '0': break
        elif opc == '1': crear_factura()
        elif opc == '2': resumen('semanal')
        elif opc == '3': resumen('mensual')
        else: input('Opcion incorrecta, presione ENTER y vuelva a intentar')
        input('Presione ENTER para continuar')