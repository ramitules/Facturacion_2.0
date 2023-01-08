import pickle
import os
from funciones import *
from Articulos import art

def crear_articulo():
    try:
        f = open('articulos.pkl', 'rb')
        while True:
            try:
                x = pickle.load(f)
            except EOFError:
                f.close()
                i = x.ID + 1
                break
    except FileNotFoundError: i = int(1)

    desc = str(input("Descripcion: "))
    cont = str(input("Conteo: "))
    p_u = int(input("Precio unitario: $"))
    articulo = art(i, desc, cont, p_u)

    with open('articulos.pkl', 'ab') as f:
        pickle.dump(articulo, f)

    print('Se ha creado el articulo con exito!')
    return True

def modificar_articulo():
    articulos = []
    cargar(articulos, 'articulos')
    if len(articulos) == 0:
        print('No hay articulos para modificar')
        return False

    for articulo in articulos:
        print(articulo)

    opc = int(input('Que articulo desea modificar? '))
    opc -= 1
    continuar = menu_modificar_articulos(opc, articulos)
    if continuar == True:
        return True
    else:
        print('Ha ocurrido un error')
        return False

def listar_articulos():
    articulos = []
    cargar(articulos, 'articulos')
    if len(articulos) == 0:
        print('No hay articulos para mostrar')
        return False

    for articulo in articulos:
        print(articulo)
    return True


def menu_articulos():
    while True:
        os.system("cls")
        print("Elija una opcion")
        print("1. Crear articulo")
        print("2. Modificar articulo")
        print("3. Listar articulos")
        print("0. Volver al menu principal\n")
        opc = input('Opcion: ')

        if opc == '0': break
        elif opc == '1': crear_articulo()
        elif opc == '2': modificar_articulo()
        elif opc == '3': listar_articulos()
        else: input('Opcion incorrecta, presione ENTER y vuelva a intentar')
        input('Presione ENTER para continuar')