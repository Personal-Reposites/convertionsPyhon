def to_kilometros(valor):
	converted_kilometros= valor *0.0003048

	return f"{ valor} pies =  { converted_kilometros} KM"

def to_metro(valor):
	converted_metros= valor * 0.3048

	return f"{ valor} pies =  { converted_metros} M"

def to_millas(valor):
	converted_millas= valor / 5280

	return f"{ valor} pies =  { converted_millas} millas"