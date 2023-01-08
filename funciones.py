import pickle
import os

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

def volver():
    while True:
        try:
            os.chdir('Facturacion')
            break
        except FileNotFoundError: os.chdir('..')