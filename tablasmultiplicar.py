# Miguel Ángel Lozano Montero
# Programa que imprime las tablas de multiplicar.

for fila in range (1,11):
	print ("Tabla del " + str (fila))
	print ("-----------")
	for columna in range (1,11):
		print (str(fila) + " por " + str(columna) + " es " + str(fila*columna))

