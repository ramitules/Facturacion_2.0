class art:
	def __init__(self, id: int, descripcion: str, conteo: str, precio_unitario: int):
		self.ID = id
		self.descripcion = descripcion
		self.conteo = conteo
		self.precio_unitario = precio_unitario

	def mostrar(self):
		print(f'ID: {self.ID}, Descripcion: {self.descripcion}, Conteo: {self.conteo}, Precio unitario: {self.precio_unitario}')

	def __setstate__(self, state):
		self.ID = state['ID']
		self.descripcion = state['descripcion']
		self.conteo = state['conteo']
		self.precio_unitario = state['precio_unitario']

	def __str__(self):
		return f'{self.ID}. {self.descripcion}    ${self.precio_unitario}'