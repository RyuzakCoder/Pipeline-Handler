from abc import ABC, abstractmethod

class IConectar(ABC):
    @abstractmethod
    def conectar(self, pipeline, objetivo):
       pass



