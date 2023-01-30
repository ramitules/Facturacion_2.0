from tkinter import ttk
from CRUD import interfaz_crud

class crud_articulos(interfaz_crud):
	def __init__(self, master=None):
		super().__init__(master)

	def cargar_widgets(self):
		estilo = ttk.Style(self)
		estilo.configure('Treeview', background=self.fondo)
		self.tabla = ttk.Treeview(self.fr_lista,
								  columns=('descripcion', 'conteo', 'p_u'),
								  style='Treeview')

		self.tabla.column('#0', width=0)
		self.tabla.column('descripcion', width=300)
		self.tabla.column('conteo', width=2)
		self.tabla.column('p_u', width=2)

		self.tabla.heading('#0', text='ID', anchor='center')
		self.tabla.heading('descripcion', text='Descripcion', anchor='center')
		self.tabla.heading('conteo', text='Conteo', anchor='center')
		self.tabla.heading('p_u', text='Precio unitario', anchor='center')

		self.tabla.place(x=0, y=0, relwidth=1, relheight=1)