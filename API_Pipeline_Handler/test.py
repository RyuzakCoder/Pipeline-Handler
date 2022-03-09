from abc import ABC, abstractmethod
from typing import Type, TypeVar

T = TypeVar('T')

class IConnection(ABC)

    @property
    @abstractmethod
    def source(self):
        pass

    @property
    @abstractmethod
    def target(self):
        pass

class Conection(IConnection):
    def __init__(self, src, trg):
        self._src = src
        self._trg = trg
    
    @property
    def target(self):
        return self._trg

    @property
    def source(self):
        return self._src

class ISocket(ABC):

    @property
    @abstractmethod
    def kind(self)->Type:
        pass
    
    @abstractmethod
    def connect(self, socket):
        pass

class Soket(ISocket, ABC):
    def __init__(self, kind:Type):
        sel._kind = kind

    @property
    def kind(self):
        return self._kind

class Input(Socket):
    def connect(self, socket:ISocket):
        assert isinstance(socket, Output)
        assert socket.kind == self.kind
        return Conection(socket, self)

class Output(Socket):
    def connect(self, socket:ISocket):
        assert isinstance(socket, Input)
        assert socket.kind == self.kind
        return Conection(self, socket)

class LeerNumero:
    num = Output(int)

class NodoSuma:
    a = Input(int)
    b = Input(int)

    def run(self):
        pass


leer1 = LeerNumero()
leer2 = LeerNumero()


coneccion1 = leer1.num.connect(suma.a)
coneccion2 = leer1.num.connect(suma.b)