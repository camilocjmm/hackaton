def get_class(texto):
    if "comida" in texto.lower():
        return "Receta"
    elif "ejercicio" in texto.lower():
        return "Ejercicio"
    elif "clima" in texto.lower():
        return "Clima"
    else:
        return "Otro"
