def to_kelvin(valor):
    # Convertir de Celsius a Kelvin
    converted_Kelvin = valor + 273.15

    return f"{valor}°C = {converted_Kelvin} K"


def to_Fahrenheit(valor):
    # Convertir de Celsius a Fahrenheit
    converted_Fahrenheit = (valor * 9 / 5) + 32
    
    return f"{valor}°C = {converted_Fahrenheit}°F"

