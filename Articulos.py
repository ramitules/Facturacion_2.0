import pickle
from tkinter.ttk import Combobox
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

		self.articulos = cargar('articulos')
		self.descripciones = [articulo.descripcion for articulo in self.articulos]


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

		if self.descripcion.get() in self.descripciones:
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

class caja_modificar_articulo(caja_cargar_articulo):
	def __init__(self, master=None):
		super().__init__(master)

	def cargar_widgets(self):
		if len(self.articulos) == 0:
			messagebox.showinfo('Sin articulos',
								'No hay articulos cargados')
			self.master.destroy()
			return

		self.pregunta = Label(self, text='Que articulo desea modificar?')
		self.pregunta.pack()

		self.desplegable_descripciones = Combobox(self,
												  values=self.descripciones,
												  state='readonly')
		self.desplegable_descripciones.bind('<<ComboboxSelected>>', self.opciones)
		self.desplegable_descripciones.pack()

	def opciones(self, event):
		self.indice = self.desplegable_descripciones.current()

		self.caja_secundaria = caja_cargar_articulo(self)

		self.caja_secundaria.label_descripcion.destroy()
		self.caja_secundaria.descripcion.destroy()

		self.caja_secundaria.conteo.insert(0, self.articulos[self.indice].conteo)
		self.caja_secundaria.precio.insert(0, self.articulos[self.indice].precio_unitario)

		self.caja_secundaria.boton_cargar.config(text='Modificar',
												 command=self.modificar)

	def modificar(self):
		self.articulos[self.indice].conteo = self.caja_secundaria.conteo.get()
		self.articulos[self.indice].precio_unitario = self.caja_secundaria.precio.get()

		with open('articulos.pkl', 'wb') as f:
			for articulo in self.articulos:
				pickle.dump(articulo, f)

		messagebox.showinfo('Exito',
							'El articulo se ha modificado con exito')

		self.master.destroy()

class caja_listar_articulos(Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack(expand=True, fill='both')

		self.articulos = cargar('articulos')

		self.label_id = Label(self, text='ID')
		self.label_descripcion = Label(self, text='Descripcion')
		self.label_conteo = Label(self, text='Conteo')
		self.label_precio = Label(self, text='Precio unitario')

		self.cargar_widgets()

	def cargar_widgets(self):
		for i, widget in enumerate(self.winfo_children()):
			widget.grid(column=i, row=0)
			self.columnconfigure(i, weight=1, pad=100)

		for i, articulo in enumerate(self.articulos, 1):
			label1 = Label(self, text=str(articulo.ID))
			label2 = Label(self, text=articulo.descripcion)
			label3 = Label(self, text=articulo.conteo)
			label4 = Label(self, text='$' + str(articulo.precio_unitario))

			label1.grid(column=0, row=i)
			label2.grid(column=1, row=i)
			label3.grid(column=2, row=i)
			label4.grid(column=3, row=i)
