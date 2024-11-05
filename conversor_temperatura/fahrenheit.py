def to_kelvin(valor):
    # Convertir de Fahrenheit a Kelvin
    converted_Kelvin = (5 / 9) * (valor - 32) + 273.15
    return f"{valor}°F = {converted_Kelvin} K"

def to_Celsius(valor):
    # Convertir de Fahrenheit a Celsius
    converted_Celsius = (5 / 9) * (valor - 32)
    return f"{valor}°F = {converted_Celsius}°C"

