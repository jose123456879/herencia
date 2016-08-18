from calcular_area import FiguraGeometrica

class cuadrado(FiguraGeometrica):

	def __init__(self, lado):
		super().__init__(lado, lado)

	def imprimir(self):
		resultado = ""

		for i in range(self.altura):
			resultado += "* " * (self.base) + "\n"
		return resultado