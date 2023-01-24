import os
import pickle

def volver():
    while True:
        try:
            os.chdir('Facturacion')
            break
        except FileNotFoundError: os.chdir('..')

def cargar(clase: str):
    lista = []
    try:
        f = open(f'{clase}.pkl', 'rb')
        while True:
            try:
                x = pickle.load(f)
                lista.append(x)
            except EOFError:
                f.close()
                break
    except FileNotFoundError: pass
    return lista


#def menu_modificar_articulos(indice: int, art: list):
#    while True:
#        print('1. Cambiar descripcion',
#                '\n2. Cambiar conteo',
#                '\n3. Cambiar precio unitario',
#                '\n4. ELIMINAR',
#                '\n0. Volver')
#        opc2 = input('Seleccione opcion: ')
#        if opc2 == '0': return False

#        elif opc2 == '1':
#            art[indice].descripcion = input('Descripcion: ')
#            print('El articulo se ha modificado con exito!')
#            break

#        elif opc2 == '2':
#            art[indice].conteo = input('Conteo: ')
#            print('El articulo se ha modificado con exito!')
#            break

#        elif opc2 == '3':
#            art[indice].precio_unitario = int(input('Precio unitario: $'))
#            print('El articulo se ha modificado con exito!')
#            break
        
#        elif opc2 == '4':
#            print('Seguro que desea eliminar el articulo?')
#            x = input('1.SI - 2.NO: ')
#            if x == '1':
#                del art[indice]
#                print('El articulo se ha eliminado con exito')
#                break

#        else: input('Opcion incorrecta, presione ENTER y vuelva a intentar')

#    with open('articulos.pkl', 'wb') as f:
#        for articulo in art:
#            pickle.dump(articulo, f)
#    return True

#def crear_articulo():
#    try:
#        f = open('articulos.pkl', 'rb')
#        while True:
#            try:
#                x = pickle.load(f)
#            except EOFError:
#                f.close()
#                i = x.ID + 1
#                break
#    except FileNotFoundError: i = int(1)

#    desc = str(input("Descripcion: "))
#    cont = str(input("Conteo: "))
#    p_u = int(input("Precio unitario: $"))
#    articulo = art(i, desc, cont, p_u)

#    with open('articulos.pkl', 'ab') as f:
#        pickle.dump(articulo, f)

#    print('Se ha creado el articulo con exito!')
#    return True

#def modificar_articulo():
#    articulos = []
#    cargar(articulos, 'articulos')
#    if len(articulos) == 0:
#        print('No hay articulos para modificar')
#        return False

#    for articulo in articulos:
#        print(articulo)

#    opc = int(input('Que articulo desea modificar? '))
#    opc -= 1
#    continuar = menu_modificar_articulos(opc, articulos)
#    if continuar == True:
#        return True
#    else:
#        print('Ha ocurrido un error')
#        return False

#def listar_articulos():
#    articulos = []
#    cargar(articulos, 'articulos')
#    if len(articulos) == 0:
#        print('No hay articulos para mostrar')
#        return False

#    for articulo in articulos:
#        print(articulo)
#    return True