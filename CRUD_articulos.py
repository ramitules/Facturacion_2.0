from tkinter import ttk
from CRUD import interfaz_crud

class crud_articulos(interfaz_crud):
	def __init__(self, master=None):
		super().__init__(master)

	def cargar_widgets(self):
		self.tabla = ttk.Treeview(self.fr_lista,
								  columns=('descripcion', 'conteo', 'p_u'))

		self.tabla.column('#0', width=1)
		self.tabla.column('descripcion', width=200)
		self.tabla.column('conteo', width=10)
		self.tabla.column('p_u', width=10)

		self.tabla.heading('#0', text='ID', anchor='center')
		self.tabla.heading('descripcion', text='Descripcion', anchor='center')
		self.tabla.heading('conteo', text='Conteo', anchor='center')
		self.tabla.heading('p_u', text='Precio unitario', anchor='center')

		self.tabla.place(x=0, y=0, relwidth=1, relheight=1)

	def f_crear(self):
		self.l_descripcion = ttk.Label(self.fr_atributos, text='Descripcion')
		self.l_conteo = ttk.Label(self.fr_atributos, text='Conteo')
		self.l_p_u = ttk.Label(self.fr_atributos, text='Precio unitario')

		self.ent_descripcion = ttk.Entry(self.fr_atributos)
		self.ent_conteo = ttk.Entry(self.fr_atributos)
		self.ent_precio = ttk.Entry(self.fr_atributos)

		self.l_descripcion.place(x=10, y=50)
		self.ent_descripcion.place(x=10, y=70)

		self.l_conteo.place(x=10, y=110)
		self.ent_conteo.place(x=10, y=130)
		
		self.l_p_u.place(x=10, y=170)
		self.ent_precio.place(x=10, y=190)

	def f_modificar(self):
		pass

	def f_eliminar(self):
		pass