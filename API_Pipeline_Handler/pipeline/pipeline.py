#Imports
from abc import ABC, abstractmethod
from . import nodo
#Imports

class Pipeline(nodo.Nodo_proceso, ABC):
	@abstractmethod
	def adicionar_nodo_inicio():
		pass
	@abstractmethod
	def adicionar_nodo_proceso():
		pass
	@abstractmethod
	def adicionar_nodo_final():
		pass
	@abstractmethod
	def devolver():
		pass
	@abstractmethod
	def procesar():
		pass

class Data_Pipeline(Pipeline):
	nodos_inicio = 0

	def __init__(self, direccion, objetivo, lista):
		self.direccion = direccion
		self.objetivo = objetivo
		self.lista_nodos = lista

	def get_nodo(self, x:tuple):
		nodo = 0
		for i in self.lista_nodos:
			if i.direccion == x:
				nodo = i
				break
		return nodo

	def conectar():
		pass

	def procesar():
		pass
	
	def adicionar_nodo_inicio(self):
		nodo_inicio = nodo.Nodo_inicio("Inicio", (0,self.nodos_inicio), "Datos", 0)
		self.lista_nodos.append(nodo_inicio)
		self.nodos_inicio += 1

	def adicionar_nodo_proceso(self, x, y):
		nodo_proceso = nodo.Nodo_proceso_X("Proceso",(x, y), 0)
		self.lista_nodos.append(nodo_proceso)

	def adicionar_nodo_pipeline():
		pass

	def adicionar_nodo_final(self, x,y):
		nodo_final = nodo.Nodo_final("Final",(x, y), "funcion")
		self.lista_nodos.append(nodo_final)

	def devolver():
		pass

	def listar_nodos(self):
		for i in self.lista_nodos:
			print("Nodo %s Tipo %s Conecciones: %s Se conecta a: %s" %(i.direccion, i.tipo, i.listar_entradas(), i.objetivo))
