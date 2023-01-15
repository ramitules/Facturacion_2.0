import pickle
import os
from Articulos import art
from Clientes import cli

def volver():
    while True:
        try:
            os.chdir('Facturacion')
            break
        except FileNotFoundError: os.chdir('..')

def cargar(lista: list, clase: str):
    try:
        f = open(f'{clase}.pkl', 'rb')
        while True:
            try:
                x = pickle.load(f)
                lista.append(x)
            except EOFError:
                f.close()
                break
    except FileNotFoundError: return False

def menu_modificar_cliente(indice: int, cl: list):
    while True:
        print('1. Cambiar nombre',
                '\n2. ELIMINAR',
                '\n0. Volver')
        opc2 = input('Seleccione opcion: ')
        if opc2 == '0': return False

        elif opc2 == '1':
            cl[indice].nombre = input('Nombre: ')
            print('El cliente se ha modificado con exito!')
            break

        elif opc2 == '2':
            print('Seguro que desea eliminar el cliente?')
            x = input('1.SI - 2.NO: ')
            if x == '1':
                del cl[indice]
                print('El cliente se ha eliminado con exito')
                break

        else: input('Opcion incorrecta, presione ENTER y vuelva a intentar')

    with open('clientes.pkl', 'wb') as f:
        for cliente in cl:
            pickle.dump(cliente, f)
    return True

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

def menu_modificar_articulos(indice: int, art: list):
    while True:
        print('1. Cambiar descripcion',
                '\n2. Cambiar conteo',
                '\n3. Cambiar precio unitario',
                '\n4. ELIMINAR',
                '\n0. Volver')
        opc2 = input('Seleccione opcion: ')
        if opc2 == '0': return False

        elif opc2 == '1':
            art[indice].descripcion = input('Descripcion: ')
            print('El articulo se ha modificado con exito!')
            break

        elif opc2 == '2':
            art[indice].conteo = input('Conteo: ')
            print('El articulo se ha modificado con exito!')
            break

        elif opc2 == '3':
            art[indice].precio_unitario = int(input('Precio unitario: $'))
            print('El articulo se ha modificado con exito!')
            break
        
        elif opc2 == '4':
            print('Seguro que desea eliminar el articulo?')
            x = input('1.SI - 2.NO: ')
            if x == '1':
                del art[indice]
                print('El articulo se ha eliminado con exito')
                break

        else: input('Opcion incorrecta, presione ENTER y vuelva a intentar')

    with open('articulos.pkl', 'wb') as f:
        for articulo in art:
            pickle.dump(articulo, f)
    return True

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