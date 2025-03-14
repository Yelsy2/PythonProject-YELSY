def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad durante un período de tiempo.

    :param temperaturas: Diccionario donde las claves son los nombres de las ciudades y los valores son listas de temperaturas semanales.
    :return: Diccionario con las ciudades y su temperatura promedio.
    """
    promedios = {}
    for ciudad, temps in temperaturas.items():
        promedio = sum(temps) / len(temps)
        promedios[ciudad] = promedio
    return promedios


# Datos de ejemplo: 3 ciudades durante 4 semanas
datos_temperaturas = {
    "Quito": [15, 17, 16, 14],
    "Guayaquil": [28, 30, 29, 27],
    "Cuenca": [13, 14, 12, 15]
}

# Cálculo de temperaturas promedio
resultado = calcular_temperatura_promedio(datos_temperaturas)
print("Temperaturas promedio por ciudad:", resultado)
