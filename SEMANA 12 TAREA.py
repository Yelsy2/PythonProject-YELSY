import random

# Definir dimensiones de la matriz
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2  # Número de semanas a registrar

# Crear una matriz 3D con temperaturas aleatorias entre 10 y 35 grados Celsius
temperaturas = [[[random.randint(10, 35) for _ in dias] for _ in range(semanas)] for _ in ciudades]

# Calcular y mostrar los promedios semanales por ciudad
for i, ciudad in enumerate(ciudades):
    print(f"Temperaturas promedio para {ciudad}:")
    for semana in range(semanas):
        promedio = sum(temperaturas[i][semana]) / len(dias)
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")
    print()
