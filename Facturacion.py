from tkinter import *
from tkinter.ttk import Combobox
from funciones import *

medidas_principales = {'relx': 0.5, 
                      'rely': 0.5,
                      'relwidth':0.4,
                      'relheight': 0.2,
                      'anchor': 'center'}
colores_principales = {'bg': '#454545',
                       'activebackground': '#353535'}
provincias = ["Buenos Aries",
              "Ciudad Autonoma de Buenos Aires",
              "Catamarca",
              "Chaco",
              "Chubut",
              "Cordoba",
              "Corrientes",
              "Entre Rios",
              "Formosa",
              "Jujuy",
              "La Pampa",
              "La Rioja",
              "Mendoza",
              "Misiones",
              "Neuquen",
              "Rio Negro",
              "Salta",
              "San Juan",
              "San Luis",
              "Santa Cruz",
              "Santa Fe",
              "Santiago del Estero",
              "Tierra del Fuego",
              "Tucuman"]
condicion_fiscal = ["Consumidor final",
                    "Monotributista",
                    "Responsable inscripto"]

dark_mode = True

def comprobar_darkmode():
    if dark_mode == False:
        colores_principales['bg'] = '#909090'
        colores_principales['activebackground'] = '#808080'

    else:
        colores_principales['bg'] = '#454545'
        colores_principales['activebackground'] = '#353535'

def switch_darkmode():
    global dark_mode

    if dark_mode == True:
        dark_mode = False

    else: dark_mode = True
    comprobar_darkmode()

class programa(Tk):
    def __init__(self):
        super().__init__()

        comprobar_darkmode()

        self.wm_title('Facturacion textil')
        self.geometry('1280x720')
        self.iconbitmap(default='.media\\favicon.ico')
        self['bg'] = colores_principales['bg']

        self.img_salir = PhotoImage(file='.media\\salir.png')
        self.salir = Button(self,
                            **colores_principales,
                            border=0,
                            text='Salir',
                            compound=TOP,
                            image=self.img_salir,
                            command=self.destroy)
        self.salir.place(relx=0.01, rely=0.5, anchor='w')

        self.img_darkmode = PhotoImage(file='.media\\oscuro.png')
        self.img_lightmode = PhotoImage(file='.media\\claro.png')

        self.boton_dark = Button(self,
                                 **colores_principales,
                                 border=0,
                                 compound=TOP,
                                 command=switch_darkmode)
        self.boton_dark.place(relx=0.99, rely=0.11, anchor='se')

        if dark_mode == True:
            self.boton_dark.config(text='Modo: oscuro', image=self.img_darkmode)

        else:
            self.boton_dark.config(text='Modo: claro', image=self.img_lightmode)


class caja_principal(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self['bg'] = colores_principales['bg']
        self.boton_1 = Button(self, **colores_principales)
        self.boton_1.place(relwidth=0.3, relheight=1, relx=0.1)

        self.boton_2 = Button(self, **colores_principales)
        self.boton_2.place(relwidth=0.3, relheight=1, relx=0.4)

        self.boton_3 = Button(self, **colores_principales)
        self.boton_3.place(relwidth=0.3, relheight=1, relx=0.7)

        self.cargar_widgets()

    def cambiar(self):
        self.destroy()

        nueva_caja = caja_multiuso(self.master)
        nueva_caja.place(**medidas_principales)

    def cargar_widgets(self):
        self.img_ventas = PhotoImage(file='.media\\venta.png')
        self.boton_1.config(image=self.img_ventas,
                            text='Ventas',
                            compound=TOP,
                            border=0,
                            command=self.cambiar)
        
        self.img_clientes = PhotoImage(file='.media\\cliente.png')
        self.boton_2.config(image=self.img_clientes,
                            text='Clientes',
                            compound=TOP,
                            border=0,
                            command=self.cambiar)
        
        self.img_articulos = PhotoImage(file='.media\\articulo.png')
        self.boton_3.config(image=self.img_articulos,
                            text='Articulos',
                            compound=TOP,
                            border=0,
                            command=self.cambiar)
        

class caja_multiuso(caja_principal):
    def __init__(self, master=None):
        super().__init__(master)

        self.boton_atras = Button(self)
        self.boton_atras.config(**colores_principales,
                                text='Atras',
                                border=0,
                                command=self.cambiar)
        self.boton_atras.place(relx=0)
        
    def cambiar(self):
        self.destroy()

        nueva_caja = caja_principal(self.master)
        nueva_caja.place(**medidas_principales)

    def nueva_ventana(self, boton):
        nueva = Toplevel(self)

        if boton['text'] == 'Cargar':
            nueva.geometry('400x400')
            nueva.wm_title('Cargar cliente')
            caja_cargar_cliente(nueva)
            
        elif boton['text'] == 'Editar':
            nueva.geometry('400x400')
            nueva.wm_title('Modificar cliente')
            caja_modificar_cliente(nueva)

        elif boton['text'] == 'Listar':
            nueva.geometry('1280x400')
            nueva.wm_title('Listar clientes')
            caja_listar_clientes(nueva)

    def cargar_widgets(self):
        self.img_cargar = PhotoImage(file='.media\\cargar.png')
        self.boton_1.config(image=self.img_cargar,
                            text='Cargar',
                            compound=TOP,
                            border=0,
                            command=lambda: self.nueva_ventana(self.boton_1))

        self.img_editar = PhotoImage(file='.media\\editar.png')
        self.boton_2.config(image=self.img_editar,
                            text='Editar',
                            compound=TOP,
                            border=0,
                            command=lambda: self.nueva_ventana(self.boton_2))

        self.img_listar = PhotoImage(file='.media\\listar.png')
        self.boton_3.config(image=self.img_listar,
                            text='Listar',
                            compound=TOP,
                            border=0,
                            command=lambda: self.nueva_ventana(self.boton_3))

class caja_cargar_cliente(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(expand=True, fill='both')

        self.clientes = cargar('clientes')
        self.nombres = [cliente.nombre for cliente in self.clientes]

        self.label_nombre = Label(self, text='Nombre completo:')
        self.label_telefono = Label(self, text='Telefono:')
        self.label_direccion = Label(self, text='Direccion:')
        self.label_ciudad = Label(self, text='Ciudad:')
        self.label_provincia = Label(self, text='Provincia')
        self.label_cond_fiscal = Label(self, text='Condicion fiscal:')

        self.nombre = Entry(self, width=30)
        self.telefono = Entry(self, width=30)
        self.direccion = Entry(self, width=30)
        self.ciudad = Entry(self, width=30)

        self.desplegable_p = Combobox(self,
                                      values=provincias,
                                      state="readonly",
                                      width=27)
        self.desplegable_c = Combobox(self,
                                      values=condicion_fiscal,
                                      state="readonly",
                                      width=27)

        self.boton_cargar = Button(self,
                                   text='Cargar',
                                   command=self.crear_cliente)

        self.cargar_widgets()

    def cargar_widgets(self):
        self.label_nombre.grid(column=0, row=0, sticky='e', pady=8)
        self.label_telefono.grid(column=0, row=1, sticky='e', pady=8)
        self.label_direccion.grid(column=0, row=2, sticky='e', pady=8)
        self.label_ciudad.grid(column=0, row=3, sticky='e', pady=8)
        self.label_provincia.grid(column=0, row=4, sticky='e', pady=8)
        self.label_cond_fiscal.grid(column=0, row=5, sticky='e', pady=8)

        self.nombre.grid(column=1, row=0, sticky='w')
        self.telefono.grid(column=1, row=1, sticky='w')
        self.direccion.grid(column=1, row=2, sticky='w')
        self.ciudad.grid(column=1, row=3, sticky='w')

        self.desplegable_p.current(0)
        self.desplegable_p.grid(column=1, row=4, sticky='w')
        self.desplegable_c.current(0)
        self.desplegable_c.grid(column=1, row=5, sticky='w')

        self.boton_cargar.place(relx=0.5, rely=0.8, anchor='center')

    def crear_cliente(self):
        cliente = cli(id=int(1),
                      nombre=self.nombre.get(),
                      telefono=self.telefono.get(),
                      direccion=self.direccion.get(),
                      ciudad=self.ciudad.get(),
                      provincia=self.desplegable_p.get(),
                      cond_fiscal=self.desplegable_c.get())

        if self.nombre.get() in self.nombres:
            messagebox.showerror('Error',
                                 f'El cliente "{self.nombre.get()}" ya existe.')
            return
        elif self.nombre.get() == '':
            messagebox.showerror('Error',
                                 'El nombre de cliente es obligatorio')
            return

        try:
            f = open('clientes.pkl', 'rb')
            while True:
                try:
                    x = pickle.load(f)
                except EOFError:
                    f.close()
                    i = x.ID + 1
                    cliente.ID = i
                    break
        except FileNotFoundError: pass

        #self.crear_directorios(self.nombre.get())

        with open('clientes.pkl', 'ab') as f:
            pickle.dump(cliente, f)
        
        messagebox.showinfo('Cliente',
                            'El cliente se ha creado con exito')

        self.master.destroy()

    def crear_directorios(self):
        os.chdir('..')
        os.chdir('Optitex')

        try: 
            os.mkdir(f'{self.nombre.get()}')
            os.mkdir(f'{self.nombre.get()}\\Facturas')
            os.mkdir(f'{self.nombre.get()}\\Vista previa')
            os.mkdir(f'{self.nombre.get()}\\Molderias')
            os.mkdir(f'{self.nombre.get()}\\Tizadas')
        except FileExistsError: pass

        os.chdir('..')
        os.chdir('Facturacion')

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


class caja_modificar_cliente(caja_cargar_cliente):
    def __init__(self, master=None):
        super().__init__(master)

    def cargar_widgets(self):
        if len(self.clientes) == 0:
            messagebox.showinfo('Sin clientes',
                                'No hay clientes cargados')
            self.master.destroy()
            return

        self.pregunta = Label(self, text='Que cliente desea modificar?')
        self.pregunta.pack()

        self.desplegable_nombres = Combobox(self, values=self.nombres, state="readonly")
        self.desplegable_nombres.bind("<<ComboboxSelected>>", self.opciones)
        self.desplegable_nombres.pack()

    def opciones(self, event):
        self.indice = self.desplegable_nombres.current()
        indice_prov = provincias.index(self.clientes[self.indice].provincia)
        indice_cond = condicion_fiscal.index(self.clientes[self.indice].cond_fiscal)

        self.caja_secundaria = caja_cargar_cliente(self)

        self.caja_secundaria.label_nombre.destroy()
        self.caja_secundaria.nombre.destroy()

        self.caja_secundaria.telefono.insert(0, self.clientes[self.indice].telefono)
        self.caja_secundaria.direccion.insert(0, self.clientes[self.indice].direccion)
        self.caja_secundaria.ciudad.insert(0, self.clientes[self.indice].ciudad)

        self.caja_secundaria.desplegable_p.current(indice_prov)
        self.caja_secundaria.desplegable_c.current(indice_cond)

        self.caja_secundaria.boton_cargar.config(text='Modificar',
                                                 command=self.modificar)

    def modificar(self):
        self.clientes[self.indice].telefono = self.caja_secundaria.telefono.get()
        self.clientes[self.indice].direccion = self.caja_secundaria.direccion.get()
        self.clientes[self.indice].ciudad = self.caja_secundaria.ciudad.get()
        self.clientes[self.indice].provincia = self.caja_secundaria.desplegable_p.get()
        self.clientes[self.indice].cond_fiscal = self.caja_secundaria.desplegable_c.get()

        with open('clientes.pkl', 'wb') as f:
            for cliente in self.clientes:
                pickle.dump(cliente, f)

        messagebox.showinfo('Exito',
                            'El cliente se ha modificado con exito')
        self.master.destroy()


class caja_listar_clientes(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(expand=True, fill='both')

        self.clientes = cargar('clientes')

        self.label_id = Label(self, text='ID')
        self.label_nombre = Label(self, text='Nombre')
        self.label_telefono = Label(self, text='Telefono')
        self.label_direccion = Label(self, text='Direccion')
        self.label_ciudad = Label(self, text='Ciudad')
        self.label_provincia = Label(self, text='Provincia')
        self.label_cond_fiscal = Label(self, text='Condicion fiscal')

        self.cargar_widgets()

    def cargar_widgets(self):
        for i, widget in enumerate(self.winfo_children()):
            widget.grid(column=i, row=0)
            self.columnconfigure(i, weight=1, pad=100)

        for i, cliente in enumerate(self.clientes, 1):
            label1 = Label(self, text=str(cliente.ID))
            label2 = Label(self, text=cliente.nombre)
            label3 = Label(self, text=cliente.telefono)
            label4 = Label(self, text=cliente.direccion)
            label5 = Label(self, text=cliente.ciudad)
            label6 = Label(self, text=cliente.provincia)
            label7 = Label(self, text=cliente.cond_fiscal)

            label1.grid(column=0, row=i)
            label2.grid(column=1, row=i)
            label3.grid(column=2, row=i)
            label4.grid(column=3, row=i)
            label5.grid(column=4, row=i)
            label6.grid(column=5, row=i)
            label7.grid(column=6, row=i)

            

principal = programa()

caja = caja_principal(principal)
caja.place(**medidas_principales)

principal.mainloop()