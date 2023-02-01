import os
import pickle
from tkinter import END, messagebox, ttk
from variables_globales import provincias, condicion_fiscal
from CRUD import interfaz_crud
from funciones import cargar
from Clientes import cli

class crud_clientes(interfaz_crud):
    def __init__(self, master=None):
        super().__init__(master)

        self.binarios = cargar('clientes')
        self.clientes = []

        for x in self.binarios:
            self.clientes.append([x.ID, x.nombre, x.telefono, x.direccion,
                                  x.ciudad, x.provincia, x.cond_fiscal])

        self.cargar_widgets()

    def cargar_widgets(self):
        self.tabla = ttk.Treeview(self.fr_lista,
                                  columns=('id', 'nombre', 'telefono', 'direccion',
                                           'ciudad', 'provincia', 'cond_fiscal'),
                                  show='headings')

        self.tabla.column('id', width=0, anchor='center')
        self.tabla.column('nombre', width=120, anchor='center')
        self.tabla.column('telefono', width=30, anchor='center')
        self.tabla.column('direccion', width=50, anchor='center')
        self.tabla.column('ciudad', width=50, anchor='center')
        self.tabla.column('provincia', width=50, anchor='center')
        self.tabla.column('cond_fiscal', width=90, anchor='center')

        self.tabla.heading('id', text='ID')
        self.tabla.heading('nombre', text='Nombre')
        self.tabla.heading('telefono', text='Telefono')
        self.tabla.heading('direccion', text='Direccion')
        self.tabla.heading('ciudad', text='Ciudad')
        self.tabla.heading('provincia', text='Provincia')
        self.tabla.heading('cond_fiscal', text='Condicion fiscal')

        for cliente in self.clientes:
            self.tabla.insert('', END, values=cliente)

        self.tabla.place(x=0, y=0, relwidth=1, relheight=1)

    def f_crear(self):
        self.f_cancelar()
        super().f_crear()

        self.l_nombre = ttk.Label(self.fr_atributos, text='Nombre')
        self.l_telefono = ttk.Label(self.fr_atributos, text='Telefono')
        self.l_direccion = ttk.Label(self.fr_atributos, text='Direccion')
        self.l_ciudad = ttk.Label(self.fr_atributos, text='Ciudad')
        self.l_provincia = ttk.Label(self.fr_atributos, text='Provincia')
        self.l_cond_fiscal = ttk.Label(self.fr_atributos, text='Condicion fiscal')

        self.ent_nombre = ttk.Entry(self.fr_atributos)
        self.ent_telefono = ttk.Entry(self.fr_atributos, validate='key',
                                      validatecommand=(self.register(self.decimales), '%S'))
        self.ent_direccion = ttk.Entry(self.fr_atributos)
        self.ent_ciudad = ttk.Entry(self.fr_atributos)

        self.com_provincia = ttk.Combobox(self.fr_atributos, values=provincias)
        self.com_cond_fiscal = ttk.Combobox(self.fr_atributos, values=condicion_fiscal)

        self.l_nombre.place(x=10, y=30)
        self.ent_nombre.place(x=10, y=50)

        self.l_telefono.place(x=10, y=90)
        self.ent_telefono.place(x=10, y=110)
        
        self.l_direccion.place(x=10, y=150)
        self.ent_direccion.place(x=10, y=170)

        self.l_ciudad.place(x=10, y=210)
        self.ent_ciudad.place(x=10, y=230)

        self.l_provincia.place(x=10, y=270)
        self.com_provincia.place(x=10, y=290)

        self.l_cond_fiscal.place(x=10, y=330)
        self.com_cond_fiscal.place(x=10, y=350)

        self.ent_nombre.focus()

    def f_aceptar_crear(self):
        nuevo_cliente = cli(id=int(1),
                            nombre=self.ent_nombre.get(),
                            telefono=self.ent_telefono.get(),
                            direccion=self.ent_direccion.get(),
                            ciudad=self.ent_ciudad.get(),
                            provincia=self.com_provincia.get(),
                            cond_fiscal=self.com_cond_fiscal.get())

        for cliente in self.clientes:
            if cliente[1] == self.ent_nombre.get():
                return messagebox.showwarning('Error',
                                              f'El cliente "{cliente[1]}" ya existe.')

            elif self.ent_nombre.get() == '':
                return messagebox.showwarning('Error',
                                              f'El nombre es obligatorio')

        if len(self.clientes) != 0:
            for elemento in self.clientes:
                nuevo_cliente.ID = elemento[0] + 1

        #self.crear_directorios()

        with open('clientes.pkl', 'ab') as f:
            pickle.dump(cliente, f)

        self.f_cancelar()

        return messagebox.showinfo('Exito',
                                   'El cliente se ha creado con exito')

    def f_modificar(self):
        self.f_cancelar()

        try:
            item = self.tabla.selection()[0]
            valores = self.tabla.item(item, option='values')
        except IndexError:
            return messagebox.showwarning('Error', 'Debe seleccionar un elemento')

        self.f_crear()

        self.ent_nombre.insert(0, valores[1])
        self.ent_telefono.insert(0, valores[2])
        self.ent_direccion.insert(0, valores[3])
        self.ent_ciudad.insert(0, valores[4])
        self.com_provincia.current(provincias.index(valores[5]))
        self.com_cond_fiscal.current(condicion_fiscal.index(valores[6]))

        self.boton_aceptar.configure(command=lambda: self.f_aceptar_modificar(valores))

    def f_aceptar_modificar(self, valores):
        if self.ent_nombre.get() == '':
            return messagebox.showwarning('Error',
                                          'El nombre es obligatorio')

        for cliente in self.binarios:
            if int(valores[0]) == cliente.ID:
                cliente.nombre = self.ent_nombre.get()
                cliente.telefono = self.ent_telefono.get()
                cliente.direccion = self.ent_ciudad.get()
                cliente.ciudad = self.ent_ciudad.get()
                cliente.provincia = self.com_provincia.get()
                cliente.cond_fiscal = self.com_cond_fiscal.get()

        with open('clientes.pkl', 'wb') as f:
            for cliente in self.binarios:
                pickle.dump(cliente, f)

        return messagebox.showinfo('Exito',
                                   'El cliente se ha modificado con exito')

    def f_eliminar(self):
        self.f_cancelar()

        try:
            item = self.tabla.selection()[0]
            valores = self.tabla.item(item, option='values')
        except IndexError:
            return messagebox.showwarning('Error', 'Debe seleccionar un elemento')

        if messagebox.askyesno('Eliminar',
                               'Seguro que desea eliminar el cliente seleccionado?'):
            for i, cliente in enumerate(self.binarios):
                if cliente.ID == int(valores[0]):
                    self.binarios.pop(i)

            self.tabla.delete(item)

            with open('clientes.pkl', 'wb') as f:
                for cliente in self.binarios:
                    pickle.dump(cliente, f)

            return messagebox.showinfo('Exito',
                                       'El cliente se ha eliminado con exito')

        else: return messagebox.showinfo('Error',
                                         'Ha ocurrido un error')

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
