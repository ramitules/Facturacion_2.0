import pickle
import os
from Clientes import cli
from funciones import *

def crear_directorios(nombre: str):
    os.chdir('..')
    os.chdir('Optitex')
    try: 
        os.mkdir(f'{nombre}')
        os.mkdir(f'{nombre}\\Facturas')
        os.mkdir(f'{nombre}\\Vista previa')
        os.mkdir(f'{nombre}\\Molderias')
        os.mkdir(f'{nombre}\\Tizadas')
    except FileExistsError: pass
    os.chdir('..')
    os.chdir('Facturacion')

def crear_cliente():
    try:
        f = open('clientes.pkl', 'rb')
        while True:
            try:
                x = pickle.load(f)
            except EOFError:
                f.close()
                i = x.ID + 1
                break
    except FileNotFoundError: i = int(1)

    nombre = str(input("Nombre: "))
    cliente = cli(i, nombre)

    crear_directorios(nombre)

    with open('clientes.pkl', 'ab') as f:
        pickle.dump(cliente, f)

    print('Se ha creado el cliente con exito!')
    return True

def modificar_cliente():
    clientes = []
    cargar(clientes, 'clientes')
    if len(clientes) == 0:
        print('No hay clientes para modificar')
        return False

    for cliente in clientes:
        print(cliente)

    opc = int(input('Que cliente desea modificar? '))
    opc -= 1
    continuar = menu_modificar_cliente(opc, clientes)
    if continuar == True:
        return True
    else:
        print('Ha ocurrido un error')
        return False

def listar_clientes():
    clientes = []
    cargar(clientes, 'clientes')
    if len(clientes) == 0:
        print('No hay clientes para mostrar')
        return False

    for cliente in clientes:
        print(cliente)
    return True


def menu_clientes():
    while True:
        os.system("cls")
        print("Elija una opcion")
        print("1. Crear cliente")
        print("2. Modificar cliente")
        print("3. Listar clientes")
        print("0. Volver al menu principal\n")
        opc = input('Opcion: ')

        if opc == '0': break
        elif opc == '1': crear_cliente()
        elif opc == '2': modificar_cliente()
        elif opc == '3': listar_clientes()
        else: input('Opcion incorrecta, presione ENTER y vuelva a intentar')
        input('Presione ENTER para continuar')