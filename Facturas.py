import os
from tkinter.ttk import Combobox
from variables_globales import fecha_actual
from funciones import cargar,volver
from openpyxl import *
from tkinter import Entry, Frame, Label, filedialog

class caja_cargar_factura(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(expand=True, fill='both')

        self.plantilla = load_workbook('Plantilla.xlsx')
        self.nueva_factura = self.plantilla
        self.hoja = self.nueva_factura.active

        self.articulos = cargar('articulos')
        self.clientes = cargar('clientes')

        self.frame_cliente = Frame(self)
        self.frame_encabezados = Frame(self)
        self.frame_articulos = Frame(self)


        self.label_cliente = Label(self.frame_cliente, text='Seleccione el cliente')
        self.selec_cliente = Combobox(self.frame_cliente,
                                      values=[cliente.nombre for cliente in self.clientes],
                                      state='readonly',
                                      width=30)

        self.enc_articulo = Label(self.frame_encabezados, text='ID')
        self.enc_descripcion = Label(self.frame_encabezados, text='Descripcion')
        self.enc_conteo = Label(self.frame_encabezados, text='Conteo')
        self.enc_p_unitario = Label(self.frame_encabezados, text='Precio unitario')
        self.enc_total = Label(self.frame_encabezados, text='Total')
        
        self.cargar_widgets()

    def cargar_widgets(self):
        self.frame_cliente.pack(expand=True, fill='both', pady=20)
        self.frame_encabezados.pack(anchor='s', expand=True, fill='x')
        self.frame_articulos.pack(expand=True, fill='both')

        self.label_cliente.pack(anchor='center')
        self.selec_cliente.pack(anchor='center')
        self.selec_cliente.bind('<<ComboboxSelected>>', self.cargar_articulos)

    def cargar_articulos(self, event):
        for i, widget in enumerate(self.frame_articulos.winfo_children()):
            widget.grid(column=i, row=0)
            self.frame_encabezados.columnconfigure(i, weight=1, pad=100)

        for x in range(6):
            self.frame_articulos.columnconfigure(x, weight=1, pad=100)

        self.frame_articulos.rowconfigure(0, pad=1, weight=1)
        self.selec_articulo = Combobox(self.frame_articulos,
                                        values=[articulo.descripcion for articulo in self.articulos],
                                        state='readonly',
                                        width=20)
        self.selec_articulo.bind('<<ComboboxSelected>>', self.cargar_items)
        self.selec_articulo.grid(column=1, row=0)

    def cargar_items(self, event, indice=0):
        self.label_id = Label(self.frame_articulos, text=self.articulos[self.selec_articulo.current()].ID)
        self.entry_conteo = Entry(self.frame_articulos, width=20)
        self.label_conteo = Label(self.frame_articulos, text=self.articulos[self.selec_articulo.current()].conteo)
        self.label_precio = Label(self.frame_articulos, text=self.articulos[self.selec_articulo.current()].precio_unitario)
        self.total = Label(self.frame_articulos)
        
        self.label_id.grid(column=0, row=indice)
        self.entry_conteo.bind('<FocusOut>', self.calcular_total)
        self.entry_conteo.grid(column=2, row=indice)
        self.label_conteo.grid(column=3, row=indice)
        self.label_precio.grid(column=4, row=indice)
        self.total.grid(column=5, row=indice)

    def calcular_total(self, event):
        unidades = float(self.entry_conteo.get())
        precio = float(self.label_precio['text'])
        total = unidades * precio
        self.total['text'] = total

#    def crear_factura(self):
#        self.hoja['G2'] = fecha_actual
#        self.hoja['C2'] = self.selec_cliente.get()
#        #os.chdir('..')
#        #os.chdir(f'Optitex\\{clientes[opc].nombre}')
#        acumular = float(0)
#        print('\nPrimer articulo')
#        for x in range(13):
#            indice = str(x+5)

#            for articulo in articulos:
#                print(articulo)

#            opc = int(input('Opcion: '))
#            opc -= 1

#            hoja['B'+indice] = articulos[opc].ID
#            hoja['C'+indice] = articulos[opc].descripcion
#            hoja['D'+indice] = articulos[opc].conteo

#            print(articulos[opc].conteo, end = " ")
#            cant = float(input('cantidad: '))

#            hoja['E'+indice] = cant
#            hoja['F'+indice] = articulos[opc].precio_unitario
#            hoja['G'+indice] = cant * articulos[opc].precio_unitario
#            acumular += (cant * articulos[opc].precio_unitario)

#            print("\nAgregar mas articulos?")
#            opc = input("1.SI  2.NO: ")
#            if opc == '2': break

#        hoja['G18'] = acumular
#        archivoMRK = seleccionar_mark()

#        hoja['B19'] = str("Observaciones: archivo " + archivoMRK)
#        os.chdir('Facturas')
#        nueva_factura.save(f'{archivoMRK}.xlsx')
#        os.startfile(f'{archivoMRK}.xlsx')

#        print("Factura creada con exito")
#        volver()

#def seleccionar_mark():
#    os.system("cls")
#    input('A continuacion vas a poder seleccionar el archivo MARK que utilizaste. Presiona ENTER para continuar')

#    archivo = filedialog.askopenfilename(title='Seleccionar archivo de marcada', filetypes=[('Archivo Mark','*.MRK')])
#    archivoMRK1 = os.path.basename(archivo)
#    archivoMRK = archivoMRK1.replace('.MRK','')

#    if len(archivoMRK) == 0:
#        return 'error'
#    else:
#        print(archivoMRK)
#        return archivoMRK

#def listar_facturas(periodo: str, fac: list):
#    acum = float(0)
#    ahora = datetime.now()

#    for factura in fac:
#        try:
#            aux = load_workbook(factura)
#            hoja_aux = aux.active
#            fecha_factura = hoja_aux['G2'].value

#            if periodo == 'semanal':
#                semana = ahora.isocalendar()[1]
#                semana_factura = fecha_factura.isocalendar()[1]

#                if semana_factura == semana:
#                    print(factura, ', $', hoja_aux['G18'].value)
#                    acum += hoja_aux['G18'].value
#                    aux.close()
#            else:
#                mes = ahora.month
#                mes_factura = fecha_factura.month

#                if mes_factura == mes:
#                    print(factura, ', $', hoja_aux['G18'].value)
#                    acum += hoja_aux['G18'].value
#                    aux.close()
#        except: pass
#    return acum

#def resumen_general(periodo: str, clientes: list):
#    acumular = float(0)

#    for cliente in clientes:
#        suma_cliente = float(0)
#        print(f'{cliente.nombre}')

#        os.chdir('..')

#        try: os.chdir(f'Optitex\\{cliente.nombre}\\Facturas')
#        except FileNotFoundError: input(f'El cliente {cliente.nombre} no tiene carpeta de facturas. Presione ENTER para continuar')

#        facturas = os.listdir()
#        suma_cliente += listar_facturas(periodo, facturas)
#        acumular += suma_cliente
#        print('Total:  $', suma_cliente)
#        print('_________________________________')
#        volver()

#    print(f'Total {periodo} acumulado: $', acumular)

#def resumen_por_cliente(periodo: str, clientes: list):
#    acumular = float(0)

#    for cliente in clientes:
#        print(cliente)
#    opc = int(input('Seleccione cliente: '))
#    opc -=1

#    os.chdir('..')
#    os.chdir(f'Optitex\\{clientes[opc].nombre}\\Facturas')
#    facturas = os.listdir()

#    acumular += listar_facturas(periodo, facturas)

#    print(f'Total {periodo} acumulado, cliente {clientes[opc].nombre}: $', acumular)
#    print('_________________________________')
#    volver()

#def resumen(periodo: str):
#    clientes = []
#    cargar(clientes, 'clientes')

#    while True:
#        os.system('cls')
#        print(f'1. Resumen {periodo} general')
#        print(f'2. Resumen {periodo} por cliente')
#        print('0. Volver\n')
#        opc = input('Opcion: ')

#        if opc == '0': return

#        elif opc == '1':
#            resumen_general(periodo, clientes)
#            break

#        elif opc == '2':
#            resumen_por_cliente(periodo, clientes)
#            break

#        else: input('Opcion incorrecta, presione ENTER y vuelva a intentar')