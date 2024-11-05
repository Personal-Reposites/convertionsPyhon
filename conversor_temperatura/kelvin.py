def to_Fahrenheit(valor):

    # Convertir de Kelvin a Fahrenheit
    converted_Fahrenheit = ((valor - 273.15) * 9 / 5) + 32

    return f"{valor} K = {converted_Fahrenheit} °F"

def to_Celsius(valor):
    # Convertir de Kelvin a Celsius
    converted_Celsius = valor - 273.15
    return f"{valor} K = {converted_Celsius} °C"

