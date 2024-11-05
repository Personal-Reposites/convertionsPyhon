def to_pies(valor):
	converted_pies= valor * 3280.84

	return f"{ valor} KM =  { converted_pies} pies"


def to_metro(valor):
	converted_metros= valor * 1000

	return f"{ valor} KM =  { converted_metros}M"

def to_milla(valor):
	converted_milla= valor * 0.621371

	return f"{ valor} KM =  { converted_milla} millas"
