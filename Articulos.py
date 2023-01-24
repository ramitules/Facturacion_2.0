import pickle
from funciones import cargar
from tkinter import Button, Entry, Frame, Label, messagebox

class art:
	def __init__(self,
				id: int,
				descripcion: str,
				conteo: str,
				precio_unitario: int):
		self.ID = id
		self.descripcion = descripcion
		self.conteo = conteo
		self.precio_unitario = precio_unitario

	def __getstate__(self):
		return {'ID': self.ID,
				'descripcion': self.descripcion,
				'conteo': self.conteo,
				'precio_unitario': self.precio_unitario}

	def __setstate__(self, state):
		self.ID = state['ID']
		self.descripcion = state['descripcion']
		self.conteo = state['conteo']
		self.precio_unitario = state['precio_unitario']

class caja_cargar_articulo(Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack(expand=True, fill='both')

		self.label_descripcion = Label(self, text='Descripcion: ')
		self.label_conteo = Label(self, text='Conteo: ')
		self.label_precio = Label(self, text='Precio unitario: $')

		self.descripcion = Entry(self, width=40)
		self.conteo = Entry(self, width=40)
		self.precio = Entry(self, width=7)

		self.boton_cargar = Button(self,
							 text='Cargar',
							 command=self.crear_articulo)

		self.cargar_widgets()

	def cargar_widgets(self):
		for i, widget in enumerate(self.winfo_children()):
			if isinstance(widget, Label):
				widget.grid(column=0, row=i, sticky='e', pady=8)
			else:
				widget.grid(column=1, row=i-3, sticky='w')

		self.boton_cargar.place(relx=0.5, rely=0.8, anchor='center')

	def crear_articulo(self):
		articulo = art(id=int(1),
					   descripcion=self.descripcion.get(),
					   conteo=self.conteo.get(),
					   precio_unitario=int(self.precio.get()))

		articulos = cargar('articulos')
		descripciones = [articulo.descripcion for articulo in articulos]

		if self.descripcion.get() in descripciones:
			messagebox.showerror('Error',
								 f'El articulo "{self.descripcion.get()}" ya existe.')
			return

		elif self.descripcion.get() == '':
			messagebox.showerror('Error',
								 'La descripcion es obligatoria')
			return

		try:
			f = open('articulos.pkl', 'rb')
			while True:
				try:
					x = pickle.load(f)
				except EOFError:
					f.close()
					i = x.ID + 1
					articulo.ID = i
					break
		except FileNotFoundError: pass

		with open('articulos.pkl', 'ab') as f:
			pickle.dump(articulo, f)

		messagebox.showinfo('Articulo',
							'El articulo se ha creado con exito')

		self.master.destroy()