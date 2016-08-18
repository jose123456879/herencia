from cuadrado import cuadrado
from triangulo import Triangulo

continuar = False
while continuar == False:
	menu= int(input("1. Crear Figura \n2. Salir \n"))
	if menu == 1:
		figura = int(input("1. Cuadrado \n2. Triangulo\n "))
		if figura == 1:
			lado = int(input("Valor de los lados: "))
			cuadro = cuadrado(lado)
			mini = int(input("1. Calcular el area \n2. Imprimir figura \n "))
			if mini == 1:
				print ("Area: ", cuadro.calcular_area())
			elif mini == 2:
				print ("Figura:" )
				print(cuadro.imprimir())
		if figura == 2:
			base = int(input("Valor de base: "))
			altura = int(input("Valor de altura: "))
			triangulo = Triangulo(base,altura)
			mini = int(input("1. Calcular el area \n2. Imprimir figura \n "))
			if mini == 1:
				print ("Area: ", triangulo.calcular_area())
			elif mini== 2:
				print ("Figura:" )
				print(triangulo.imprimir())
	else:
		continuar = True
print("adios :)")