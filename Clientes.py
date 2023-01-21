class cli:
	def __init__(self,
			  id: int,
			  nombre: str,
			  telefono: int,
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