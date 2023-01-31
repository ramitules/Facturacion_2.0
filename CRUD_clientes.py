import os
import pickle
from tkinter import ttk
from variables_globales import provincias, condicion_fiscal
from CRUD import interfaz_crud

class crud_clientes(interfaz_crud):
    def __init__(self, master=None):
        super().__init__(master)

    def cargar_widgets(self):
        self.tabla = ttk.Treeview(self.fr_lista,
                                  columns=('id', 'nombre', 'telefono', 'direccion',
                                           'ciudad', 'provincia', 'cond_fiscal'))

        self.tabla.column('id', width=0)
        self.tabla.column('nombre', width=150)
        self.tabla.column('telefono', width=10)
        self.tabla.column('direccion', width=10)
        self.tabla.column('ciudad', width=10)
        self.tabla.column('provincia', width=10)
        self.tabla.column('cond_fiscal', width=15)

        self.tabla.heading('id', text='ID', anchor='center')
        self.tabla.heading('nombre', text='Nombre', anchor='center')
        self.tabla.heading('telefono', text='Telefono', anchor='center')
        self.tabla.heading('direccion', text='Direccion', anchor='center')
        self.tabla.heading('ciudad', text='Ciudad', anchor='center')
        self.tabla.heading('provincia', text='Provincia', anchor='center')
        self.tabla.heading('cond_fiscal', text='Condicion fiscal', anchor='center')

        self.tabla.place(x=0, y=0, relwidth=1, relheight=1)

    def f_crear(self):
        self.l_nombre = ttk.Label(self.fr_atributos, text='Nombre')
        self.l_telefono = ttk.Label(self.fr_atributos, text='Telefono')
        self.l_direccion = ttk.Label(self.fr_atributos, text='Direccion')
        self.l_ciudad = ttk.Label(self.fr_atributos, text='Ciudad')
        self.l_provincia = ttk.Label(self.fr_atributos, text='Provincia')
        self.l_cond_fiscal = ttk.Label(self.fr_atributos, text='Condicion fiscal')

        self.ent_nombre = ttk.Entry(self.fr_atributos)
        self.ent_telefono = ttk.Entry(self.fr_atributos)
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

    def f_modificar(self):
        pass

    def f_eliminar(self):
        pass

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
