def to_metro(valor):
	converted_metros= valor * 1609.34

	return f"{ valor} millas =  { converted_metros}M"

def to_kilometros(valor):
	converted_kilometros= valor *1.60934

	return f"{ valor} pies =  { converted_kilometros} KM"

def to_pies(valor):
	converted_pies= valor * 5280

	return f"{ valor} KM =  { converted_pies} pies"
