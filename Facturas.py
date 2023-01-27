import os
from tkinter import messagebox, ttk
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

        self.clientes = cargar('clientes')
        self.articulos = cargar('articulos')
        self.descripciones = [articulo.descripcion for articulo in self.articulos]

        if len(self.articulos) < 24:
            self.cantidad_maxima = len(self.articulos)
        else:
            self.cantidad_maxima = 24

        self.frame_cliente = Frame(self)
        self.frame_articulos = Frame(self)

        self.filas_ID = [Label(self.frame_articulos, text='ID')]
        self.filas_descripcion = [Label(self.frame_articulos, text='Descripcion')]
        self.filas_conteo = [Label(self.frame_articulos, text='Conteo')]
        self.filas_cantidad = [Label(self.frame_articulos, text='Cantidad')]
        self.filas_p_unitario = [Label(self.frame_articulos, text='Precio unitario')]
        self.filas_total = [Label(self.frame_articulos, text='Subtotal')]

        for i in range(len(self.frame_articulos.winfo_children())):
            self.frame_articulos.columnconfigure(i, pad=100, weight=1)

        for x in range(self.cantidad_maxima):
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

        for n in range(self.cantidad_maxima + 1):
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
                                      text='Crear factura',
                                      command=self.crear_factura)
        self.boton_crear.pack(expand=True)

    def cargar_items(self, event, indice):
        self.filas_ID[indice]['text'] = self.articulos[self.filas_descripcion[indice].current()].ID
        self.filas_conteo[indice]['text'] = self.articulos[self.filas_descripcion[indice].current()].conteo
        self.filas_p_unitario[indice]['text'] = '$' + str(self.articulos[self.filas_descripcion[indice].current()].precio_unitario)

    def calcular_total(self, event, indice):
        if self.filas_cantidad[indice].get() == '' or self.filas_p_unitario[indice]['text'] == '':
            return

        cantidad = float(self.filas_cantidad[indice].get())
        precio = float(self.filas_p_unitario[indice]['text'].replace('$', ''))

        total = cantidad * precio

        self.filas_total[indice]['text'] = '$' + str(total)

    def crear_factura(self):
        self.hoja['G2'] = fecha_actual
        self.hoja['C2'] = self.label_cliente['text']

        #os.chdir('..')
        #os.chdir(f'Optitex\\{clientes[opc].nombre}')
        total = 0
        for i in range(1, self.cantidad_maxima):
            self.hoja[f'B{i+4}'] = self.filas_ID[i]['text']
            self.hoja[f'C{i+4}'] = self.filas_descripcion[i].get()
            self.hoja[f'D{i+4}'] = self.filas_conteo[i]['text']
            self.hoja[f'E{i+4}'] = self.filas_cantidad[i].get()
            self.hoja[f'F{i+4}'] = self.filas_p_unitario[i]['text']
            self.hoja[f'G{i+4}'] = self.filas_total[i]['text']

            if self.filas_total[i]['text'] != '':
                subtotal = self.filas_total[i]['text'].replace('$','')
                total += float(subtotal)

        self.hoja['G29'] = total
        #archivoMRK = seleccionar_mark()

        #hoja['B19'] = str("Observaciones: archivo " + archivoMRK)
        #os.chdir('Facturas')
        #nueva_factura.save(f'{archivoMRK}.xlsx')
        #os.startfile(f'{archivoMRK}.xlsx')
        self.nueva_factura.save('ejemplo.xlsx')

        messagebox.showinfo('Exito',
                            'Factura creada con exito')
        self.master.destroy()
        #volver()

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