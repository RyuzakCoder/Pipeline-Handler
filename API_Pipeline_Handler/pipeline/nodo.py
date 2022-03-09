from abc import ABC, abstractmethod

class Nodo(ABC):
	@abstractmethod
	def conectar():
		pass

class Nodo_inicio(Nodo, object):
	def __init__(self, tipo, direccion, datos, objetivo):
		self.tipo = tipo
		self.direccion = direccion
		self.datos = datos
		self.objetivo = objetivo

	def conectar(self, pipeline, objetivo):
		self.objetivo = objetivo
		pipeline.get_nodo(objetivo).adicionar_entrada(self.direccion)

	def entrada_de_datos():
		pass

	def listar_entradas(self):
		lista = "Nodo inicio"
		return lista


class Nodo_final(Nodo, object):
	def __init__(self, tipo, direccion, funcion):
		self.tipo = tipo
		self.direccion = direccion
		self.funcion = funcion
		self.entrada = []
		self.objetivo = "Nodo Final"

	def conectar():
		pass

	def adicionar_entrada(self, direccion):
		self.entrada.append(direccion)

	def devolver():
		pass

	def listar_entradas(self):
		lista = "["
		for i in self.entrada:
			lista += "(%d, %d), "%(i[0], i[1])
		lista += "fin]"
		return lista


class Nodo_proceso(Nodo, ABC):
	@abstractmethod
	def procesar():
		pass

class Nodo_proceso_X(Nodo_proceso):
	def __init__(self, tipo, direccion, objetivo):
		self.tipo = tipo
		self.direccion = direccion
		self.entrada = []
		self.objetivo = objetivo

	def adicionar_entrada(self, direccion):
		self.entrada.append(direccion)

	def conectar(self, pipeline, objetivo):
		self.objetivo = objetivo
		pipeline.get_nodo(objetivo).adicionar_entrada(self.direccion)

	def procesar():
		pass

	def listar_entradas(self):
		lista = "["
		for i in self.entrada:
			lista += "(%d, %d), "%(i[0], i[1])
		lista += "fin]"
		return lista