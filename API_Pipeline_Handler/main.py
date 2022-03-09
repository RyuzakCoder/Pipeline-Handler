from pipeline.pipeline import *

pipe = Data_Pipeline(1,2,[])

pipe.adicionar_nodo_inicio()
pipe.adicionar_nodo_inicio()
pipe.adicionar_nodo_proceso(1,0)
pipe.adicionar_nodo_proceso(1,1)
pipe.adicionar_nodo_proceso(2,0)
pipe.adicionar_nodo_final(3,0)

pipe.get_nodo((0,0)).conectar(pipe,(1,1))
pipe.get_nodo((0,1)).conectar(pipe,(1,0))
pipe.get_nodo((1,0)).conectar(pipe,(2,0))
pipe.get_nodo((1,1)).conectar(pipe,(2,0))
pipe.get_nodo((2,0)).conectar(pipe,(3,0))


pipe.listar_nodos()

