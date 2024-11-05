from conversor_temperatura import fahrenheit, kelvin, celsius
from conversor_longitud import pies, millas, metros, kilometros

def conv_temp():
	print('Ingresa la escala de Temperatura  :\n')

	escala = input("\n 1- Fahrenheit,\n2- Kelvin,\n3- Celsius: \n")
	valor = float(input("Cual es el  valor de temperatura que vas a convertir: "))

	if escala == '1':
		print(fahrenheit.to_kelvin(valor))
		print(fahrenheit.to_Celsius(valor))

	elif escala == '2':
		print(kelvin.to_Fahrenheit(valor))
		print(kelvin.to_Celsius(valor))

	elif escala == '3':
		print(celsius.to_kelvin(valor))
		print(celsius.to_kelvin(valor))

	else:
		print("Unidad no válida.")
		return conv_temp()

def conv_long():
	print('Ingresa la unidad Medida  :\n')

	unidad = input("1- Pies,\n2- Millas, \n3- Metros,\n4- Kilómetros: \n")

	valor = float(input("Ingrese el valor de longitud a convertir: "))

	if unidad == '1':
		print(pies.to_metro(valor))
		print(pies.to_kilometros(valor))
		print(pies.to_millas(valor))

	elif unidad == '2':
		print(millas.to_metro(valor))
		print(millas.to_kilometros(valor))
		print(millas.to_pies(valor))

	elif unidad == '3':
		print(metros.to_pies(valor))
		print(metros.to_kilometros(valor))
		print(metros.to_milla(valor))
	elif unidad == '4':
		print(kilometros.to_pies(valor))
		print(kilometros.to_metro(valor))
		print(kilometros.to_milla(valor))

	else:
		print("Unidad no válida.")
		return conv_long()


#---------------|Menu |---------------------------
exit=False
while not exit:
	print('\nHola, Que Deseas Convertir :\n')
	op = input('1.Temperatura\n 2.Longitud\n 3.Salir\n ')
	if op == '1':
		conv_temp()

	elif op == '2':
		conv_long()

	elif op == '3':
		print("Adios")
		exit=True
	else:
		print("No disponible")
    

