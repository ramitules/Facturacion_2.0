import os
from tkinter import ttk
from tkinter.ttk import Combobox
from variables_globales import fecha_actual
from funciones import cargar,volver
from openpyxl import *
from tkinter import Entry, Frame, Label, filedialog

class caja_cargar_factura(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(expand=True, fill='both')

        #self.plantilla = load_workbook('Plantilla.xlsx')
        #self.nueva_factura = self.plantilla
        #self.hoja = self.nueva_factura.active

        self.clientes = cargar('clientes')
        self.articulos = cargar('articulos')
        self.descripciones = [articulo.descripcion for articulo in self.articulos]

        self.frame_cliente = Frame(self)
        self.frame_articulos = Frame(self)

        self.filas_ID = [Label(self.frame_articulos, text='ID')]
        self.filas_descripcion = [Label(self.frame_articulos, text='Descripcion')]
        self.filas_conteo = [Label(self.frame_articulos, text='Conteo')]
        self.filas_cantidad = [Label(self.frame_articulos, text='Cantidad')]
        self.filas_p_unitario = [Label(self.frame_articulos, text='Precio unitario')]
        self.filas_total = [Label(self.frame_articulos, text='Subtotal')]

        for i, widget in enumerate(self.frame_articulos.winfo_children()):
            self.frame_articulos.columnconfigure(i, pad=100, weight=1)

        for x in range(13):
            self.filas_ID.append(Label(self.frame_articulos, text=' '))
            self.filas_descripcion.append(Combobox(self.frame_articulos,
                                                   values=self.descripciones,
                                                   state='readonly'))
            self.filas_conteo.append(Label(self.frame_articulos, text=' '))
            self.filas_cantidad.append(Entry(self.frame_articulos))
            self.filas_p_unitario.append(Label(self.frame_articulos, text=' '))
            self.filas_total.append(Label(self.frame_articulos, text=' '))

            self.filas_cantidad[x+1].bind('<FocusOut>',
                                          lambda y, z=x+1: self.calcular_total(y, z))
            self.filas_descripcion[x+1].bind('<<ComboboxSelected>>',
                                             lambda y, z=x+1: self.cargar_items(y, z))

        self.label_cliente = Label(self.frame_cliente, text='Seleccione el cliente')
        self.selec_cliente = Combobox(self.frame_cliente,
                                      values=[cliente.nombre for cliente in self.clientes],
                                      state='readonly',
                                      width=30)
        
        self.cargar_widgets()

    def cargar_widgets(self):
        self.frame_cliente.pack(expand=True, fill='x')
        self.frame_articulos.pack(expand=True, fill='both')

        self.label_cliente.pack(anchor='center')
        self.selec_cliente.pack(anchor='center')
        self.selec_cliente.bind('<<ComboboxSelected>>', self.fijar_cliente)

        for n in range(14):
            self.frame_articulos.rowconfigure(n, pad=1, weight=1)

            self.filas_ID[n].grid(column=0, row=n)
            self.filas_descripcion[n].grid(column=1, row=n)
            self.filas_conteo[n].grid(column=2, row=n)
            self.filas_cantidad[n].grid(column=3, row=n)
            self.filas_p_unitario[n].grid(column=4, row=n)
            self.filas_total[n].grid(column=5, row=n)

    def fijar_cliente(self, event):
        self.label_cliente['text'] = self.selec_cliente.get()
        self.selec_cliente.destroy()
        
        self.boton_crear = ttk.Button(self,
                                        text='Crear factura')
        self.boton_crear.place(anchor='center', relx=0.15, y=30)

    def cargar_items(self, event, indice):
        self.filas_ID[indice]['text'] = self.articulos[self.filas_descripcion[indice].current()].ID
        self.filas_conteo[indice]['text'] = self.articulos[self.filas_descripcion[indice].current()].conteo
        self.filas_p_unitario[indice]['text'] = self.articulos[self.filas_descripcion[indice].current()].precio_unitario

    def calcular_total(self, event, indice):
        cantidad = float(self.filas_cantidad[indice].get())
        precio = float(self.filas_p_unitario[indice]['text'])

        total = cantidad * precio

        self.filas_total[indice]['text'] = '$' + str(total)

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