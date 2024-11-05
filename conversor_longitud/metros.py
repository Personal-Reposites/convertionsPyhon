def to_pies(valor):
	converted_pies= valor * 3.28084

	return f"{ valor} M =  { converted_pies} pies"


def to_kilometros(valor):
	converted_metros= valor / 1000

	return f"{ valor} M =  { converted_metros}M"

def to_milla(valor):
	converted_milla= valor / 1609.34

	return f"{ valor} M =  { converted_milla} millas"
