import pickle
import os
from variables_globales import *
from funciones import cargar
from tkinter import Button, Entry, Frame, Label, messagebox
from tkinter.ttk import Combobox

class cli:
	def __init__(self,
			  id: int,
			  nombre: str,
			  telefono: str,
			  direccion: str,
			  ciudad: str,
			  provincia: str,
			  cond_fiscal: str):
		self.ID = id
		self.nombre = nombre
		self.telefono = telefono
		self.direccion = direccion
		self.ciudad = ciudad
		self.provincia = provincia
		self.cond_fiscal = cond_fiscal

	def __getstate__(self):
		return {'ID': self.ID,
		  'nombre': self.nombre,
		  'telefono': self.telefono,
		  'direccion': self.direccion,
		  'ciudad': self.ciudad,
		  'provincia': self.provincia,
		  'cond_fiscal': self.cond_fiscal}

	def __setstate__(self, state):
		self.ID = state['ID']
		self.nombre = state['nombre']
		self.telefono = state['telefono']
		self.direccion = state['direccion']
		self.ciudad = state['ciudad']
		self.provincia = state['provincia']
		self.cond_fiscal = state['cond_fiscal']

class caja_cargar_cliente(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(expand=True, fill='both')

        self.label_nombre = Label(self, text='Nombre completo:')
        self.label_telefono = Label(self, text='Telefono:')
        self.label_direccion = Label(self, text='Direccion:')
        self.label_ciudad = Label(self, text='Ciudad:')
        self.label_provincia = Label(self, text='Provincia')
        self.label_cond_fiscal = Label(self, text='Condicion fiscal:')

        self.nombre = Entry(self, width=40)
        self.telefono = Entry(self, width=40)
        self.direccion = Entry(self, width=40)
        self.ciudad = Entry(self, width=40)

        self.desplegable_p = Combobox(self,
                                      values=provincias,
                                      state="readonly",
                                      width=37)
        self.desplegable_c = Combobox(self,
                                      values=condicion_fiscal,
                                      state="readonly",
                                      width=37)

        self.boton_cargar = Button(self,
                                   text='Cargar',
                                   command=self.crear_cliente)

        self.cargar_widgets()

    def cargar_widgets(self):
        cont = 0
        for i, widget in enumerate(self.winfo_children()):
            if isinstance(widget, Label):
                widget.grid(column=0, row=i, sticky='e', pady=8)
                cont += 1
            elif isinstance(widget, Entry):
                widget.grid(column=1, row=i-cont, sticky='w')
            elif isinstance(widget, Combobox):
                widget.current(0)
                widget.grid(column=1, row=i-cont, sticky='w')

        self.boton_cargar.place(relx=0.5, rely=0.8, anchor='center')

    def crear_cliente(self):
        cliente = cli(id=int(1),
                      nombre=self.nombre.get(),
                      telefono=self.telefono.get(),
                      direccion=self.direccion.get(),
                      ciudad=self.ciudad.get(),
                      provincia=self.desplegable_p.get(),
                      cond_fiscal=self.desplegable_c.get())

        clientes = cargar('clientes')
        nombres = [cliente.nombre for cliente in clientes]

        if self.nombre.get() in nombres:
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


class caja_modificar_cliente(caja_cargar_cliente):
    def __init__(self, master=None):
        super().__init__(master)

        self.clientes = cargar('clientes')
        self.nombres = [cliente.nombre for cliente in self.clientes]

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
