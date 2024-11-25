from conversor_temperatura import fahrenheit, kelvin, celsius
from conversor_longitud import pies, millas, metros, kilometros

# Listas para almacenar los historiales de temperatura y longitud
historial_temperatura = []
historial_longitud = []

def guardar_historial_temperatura(escala, valor, resultado):
    historial_temperatura.append(f"{escala} {valor} -> {resultado}")

def guardar_historial_longitud(unidad, valor, resultado):
    historial_longitud.append(f"{unidad} {valor} -> {resultado}")

def consultar_historial():
    print("\nHistorial de Temperaturas:")
    if historial_temperatura:
        for item in historial_temperatura:
            print(item)
    else:
        print("No hay historial de temperaturas.")
    
    print("\nHistorial de Longitudes:")
    if historial_longitud:
        for item in historial_longitud:
            print(item)
    else:
        print("No hay historial de longitudes.")

def conv_temp():
    print('Ingresa la escala de Temperatura  :\n')

    escala = input("\n 1- Fahrenheit,\n2- Kelvin,\n3- Celsius: \n")
    valor = float(input("Cual es el  valor de temperatura que vas a convertir: "))

    if escala == '1':
        resultado1 = fahrenheit.to_kelvin(valor)
        resultado2 = fahrenheit.to_Celsius(valor)
        print(resultado1)
        print(resultado2)
        guardar_historial_temperatura('Fahrenheit', valor, f"Kelvin: {resultado1}, Celsius: {resultado2}")

    elif escala == '2':
        resultado1 = kelvin.to_Fahrenheit(valor)
        resultado2 = kelvin.to_Celsius(valor)
        print(resultado1)
        print(resultado2)
        guardar_historial_temperatura('Kelvin', valor, f"Fahrenheit: {resultado1}, Celsius: {resultado2}")

    elif escala == '3':
        resultado1 = celsius.to_kelvin(valor)
        resultado2 = celsius.to_Fahrenheit(valor)
        print(resultado1)
        print(resultado2)
        guardar_historial_temperatura('Celsius', valor, f"Kelvin: {resultado1}, Fahrenheit: {resultado2}")

    else:
        print("Unidad no válida.")
        return conv_temp()

def conv_long():
    print('Ingresa la unidad Medida  :\n')

    unidad = input("1- Pies,\n2- Millas, \n3- Metros,\n4- Kilómetros: \n")

    valor = float(input("Ingrese el valor de longitud a convertir: "))

    if unidad == '1':
        resultado1 = pies.to_metro(valor)
        resultado2 = pies.to_kilometros(valor)
        resultado3 = pies.to_millas(valor)
        print(resultado1)
        print(resultado2)
        print(resultado3)
        guardar_historial_longitud('Pies', valor, f"Metro: {resultado1}, Kilómetros: {resultado2}, Millas: {resultado3}")

    elif unidad == '2':
        resultado1 = millas.to_metro(valor)
        resultado2 = millas.to_kilometros(valor)
        resultado3 = millas.to_pies(valor)
        print(resultado1)
        print(resultado2)
        print(resultado3)
        guardar_historial_longitud('Millas', valor, f"Metro: {resultado1}, Kilómetros: {resultado2}, Pies: {resultado3}")

    elif unidad == '3':
        resultado1 = metros.to_pies(valor)
        resultado2 = metros.to_kilometros(valor)
        resultado3 = metros.to_milla(valor)
        print(resultado1)
        print(resultado2)
        print(resultado3)
        guardar_historial_longitud('Metros', valor, f"Pies: {resultado1}, Kilómetros: {resultado2}, Millas: {resultado3}")

    elif unidad == '4':
        resultado1 = kilometros.to_pies(valor)
        resultado2 = kilometros.to_metro(valor)
        resultado3 = kilometros.to_milla(valor)
        print(resultado1)
        print(resultado2)
        print(resultado3)
        guardar_historial_longitud('Kilómetros', valor, f"Pies: {resultado1}, Metro: {resultado2}, Millas: {resultado3}")

    else:
        print("Unidad no válida.")
        return conv_long()

#---------------|Menu |---------------------------
exit=False
while not exit:
    print('\nHola, Que Deseas Convertir :\n')
    op = input('1.Temperatura\n 2.Longitud\n 3.Consultar Historial\n 4.Salir\n ')
    if op == '1':
        conv_temp()

    elif op == '2':
        conv_long()

    elif op == '3':
        consultar_historial()

    elif op == '4':
        print("Adios")
        exit=True
    else:
        print("Opción no disponible")
