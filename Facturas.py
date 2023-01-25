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
        self.frame_articulos = Frame(self)
        self.frame_IDs = Frame(self.frame_articulos)
        self.frame_descripciones = Frame(self.frame_articulos)
        self.frame_conteos = Frame(self.frame_articulos)
        self.frame_cantidades = Frame(self.frame_articulos)
        self.frame_precios = Frame(self.frame_articulos)
        self.frame_totales = Frame(self.frame_articulos)


        self.label_cliente = Label(self.frame_cliente, text='Seleccione el cliente')
        self.selec_cliente = Combobox(self.frame_cliente,
                                      values=[cliente.nombre for cliente in self.clientes],
                                      state='readonly',
                                      width=30)

        self.enc_ID = Label(self.frame_IDs, text='ID\n')
        self.enc_descripcion = Label(self.frame_descripciones, text='Descripcion')
        self.enc_conteo = Label(self.frame_conteos, text='Conteo\n')
        self.enc_cantidad = Label(self.frame_cantidades, text='Cantidad\n')
        self.enc_p_unitario = Label(self.frame_precios, text='Precio unitario\n')
        self.enc_total = Label(self.frame_totales, text='Total\n')

        self.label_id = Label(self.frame_IDs)
        self.label_conteo = Label(self.frame_conteos)
        self.entry_cantidad = Entry(self.frame_cantidades)
        self.label_precio = Label(self.frame_precios)
        self.total = Label(self.frame_totales)


        self.selec_articulo = Combobox(self.frame_descripciones,
                                        values=[articulo.descripcion for articulo in self.articulos],
                                        state='readonly',
                                        width=20)
        
        self.cargar_widgets()

    def cargar_widgets(self):
        self.frame_cliente.place(anchor='center', relx=0.5, y=30)
        self.frame_articulos.place(anchor='center', relx=0.5, y=100)

        self.label_cliente.pack(anchor='center')
        self.selec_cliente.pack(anchor='center')
        self.selec_cliente.bind('<<ComboboxSelected>>', self.cargar_articulos)
        self.selec_articulo.bind('<<ComboboxSelected>>', self.cargar_items)

        self.frame_articulos.rowconfigure(0, weight=1)

        for i, widget in enumerate(self.frame_articulos.winfo_children()):
            self.frame_articulos.columnconfigure(i, pad=80)
            widget.grid(column=i, row=0)

            for x, subwidget in enumerate(widget.winfo_children()):
                subwidget.pack(side='top', expand=True, fill='x')

    def cargar_articulos(self, event):
        self.label_cliente['text'] = self.selec_cliente.get()
        self.selec_cliente.destroy()
        
    def cargar_items(self, event):
        #for i, widget in enumerate(self.frame_articulos.winfo_children()):
        #    if i != 1:
        #        for x, subwidget in enumerate(widget.winfo_children()):
        #            if x != 0:
        #                subwidget.destroy()

        self.label_id = Label(self.frame_IDs, text=self.articulos[self.selec_articulo.current()].ID)
        self.label_conteo = Label(self.frame_conteos, text=self.articulos[self.selec_articulo.current()].conteo)
        self.entry_cantidad = Entry(self.frame_cantidades)
        self.label_precio = Label(self.frame_precios, text=self.articulos[self.selec_articulo.current()].precio_unitario)
        self.total = Label(self.frame_totales)
        self.selec_articulo = Combobox(self.frame_descripciones,
                                        values=[articulo.descripcion for articulo in self.articulos],
                                        state='readonly',
                                        width=20)
        self.selec_articulo.bind('<<ComboboxSelected>>', self.cargar_items)
        self.selec_articulo.pack(side='top', expand=True, fill='x')
        
        self.label_id.pack(side='top', expand=True, fill='x')
        self.label_conteo.pack(side='top', expand=True, fill='x')
        self.entry_cantidad.bind('<FocusOut>', self.calcular_total)
        self.entry_cantidad.pack(side='top', expand=True, fill='x')
        self.label_precio.pack(side='top', expand=True, fill='x')
        self.total.pack(side='top', expand=True, fill='x')

    def calcular_total(self, event):
        unidades = float(self.entry_cantidad.get())
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