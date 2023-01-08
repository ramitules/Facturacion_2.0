import os
from funciones import cargar,volver
from openpyxl import *
from tkinter import filedialog
from datetime import datetime, date

def seleccionar_mark():
    os.system("cls")
    input('A continuacion vas a poder seleccionar el archivo MARK que utilizaste. Presiona ENTER para continuar')

    archivo = filedialog.askopenfilename(title='Seleccionar archivo de marcada', filetypes=[('Archivo Mark','*.MRK')])
    archivoMRK1 = os.path.basename(archivo)
    archivoMRK = archivoMRK1.replace('.MRK','')

    if len(archivoMRK) == 0:
        return 'error'
    else:
        print(archivoMRK)
        return archivoMRK

def crear_factura():
    plantilla = load_workbook('Plantilla.xlsx')
    nueva_factura = plantilla
    hoja = nueva_factura.active

    fecha = date.today()
    hoja['G2'] = fecha

    articulos = []
    cargar(articulos, 'articulos')

    if len(articulos) == 0:
        print('No hay articulos cargados')
        return

    clientes = []
    cargar(clientes, 'clientes')

    if len(clientes) == 0:
        print('No hay clientes cargados')
        return

    print('Seleccionar cliente')
    for cliente in clientes:
        print(cliente)

    opc = int(input('Opcion: '))
    opc -= 1
    hoja['C2'] = clientes[opc].nombre

    os.chdir('..')
    os.chdir(f'Optitex\\{clientes[opc].nombre}')

    acumular = float(0)

    print('\nPrimer articulo')
    
    for x in range(13):
        indice = str(x+5)

        for articulo in articulos:
            print(articulo)

        opc = int(input('Opcion: '))
        opc -= 1

        hoja['B'+indice] = articulos[opc].ID
        hoja['C'+indice] = articulos[opc].descripcion
        hoja['D'+indice] = articulos[opc].conteo

        print(articulos[opc].conteo, end = " ")
        cant = float(input('cantidad: '))

        hoja['E'+indice] = cant
        hoja['F'+indice] = articulos[opc].precio_unitario
        hoja['G'+indice] = cant * articulos[opc].precio_unitario
        acumular += (cant * articulos[opc].precio_unitario)

        print("\nAgregar mas articulos?")
        opc = input("1.SI  2.NO: ")
        if opc == '2': break

    hoja['G18'] = acumular
    archivoMRK = seleccionar_mark()

    hoja['B19'] = str("Observaciones: archivo " + archivoMRK)
    os.chdir('Facturas')
    nueva_factura.save(f'{archivoMRK}.xlsx')
    os.startfile(f'{archivoMRK}.xlsx')

    print("Factura creada con exito")
    volver()

def listar_facturas(periodo: str, fac: list):
    acum = float(0)
    ahora = datetime.now()

    for factura in fac:
        try:
            aux = load_workbook(factura)
            hoja_aux = aux.active
            fecha_factura = hoja_aux['G2'].value

            if periodo == 'semanal':
                semana = ahora.isocalendar()[1]
                semana_factura = fecha_factura.isocalendar()[1]

                if semana_factura == semana:
                    print(factura, ', $', hoja_aux['G18'].value)
                    acum += hoja_aux['G18'].value
                    aux.close()
            else:
                mes = ahora.month
                mes_factura = fecha_factura.month

                if mes_factura == mes:
                    print(factura, ', $', hoja_aux['G18'].value)
                    acum += hoja_aux['G18'].value
                    aux.close()
        except: pass
    return acum

def resumen_general(periodo: str, clientes: list):
    acumular = float(0)

    for cliente in clientes:
        suma_cliente = float(0)
        print(f'{cliente.nombre}')

        os.chdir('..')

        try: os.chdir(f'Optitex\\{cliente.nombre}\\Facturas')
        except FileNotFoundError: input(f'El cliente {cliente.nombre} no tiene carpeta de facturas. Presione ENTER para continuar')

        facturas = os.listdir()
        suma_cliente += listar_facturas(periodo, facturas)
        acumular += suma_cliente
        print('Total:  $', suma_cliente)
        print('_________________________________')
        volver()

    print(f'Total {periodo} acumulado: $', acumular)

def resumen_por_cliente(periodo: str, clientes: list):
    acumular = float(0)

    for cliente in clientes:
        print(cliente)
    opc = int(input('Seleccione cliente: '))
    opc -=1

    os.chdir('..')
    os.chdir(f'Optitex\\{clientes[opc].nombre}\\Facturas')
    facturas = os.listdir()

    acumular += listar_facturas(periodo, facturas)

    print(f'Total {periodo} acumulado, cliente {clientes[opc].nombre}: $', acumular)
    print('_________________________________')
    volver()

def resumen(periodo: str):
    clientes = []
    cargar(clientes, 'clientes')

    while True:
        os.system('cls')
        print(f'1. Resumen {periodo} general')
        print(f'2. Resumen {periodo} por cliente')
        print('0. Volver\n')
        opc = input('Opcion: ')

        if opc == '0': return

        elif opc == '1':
            resumen_general(periodo, clientes)
            break

        elif opc == '2':
            resumen_por_cliente(periodo, clientes)
            break

        else: input('Opcion incorrecta, presione ENTER y vuelva a intentar')