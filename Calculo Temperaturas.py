import random

def calcular_promedio_temperaturas(temperaturas, ciudades, semanas, dias_semana):
    """
    Calcula la temperatura promedio de cada ciudad durante el período de tiempo dado.
    :param temperaturas: Lista tridimensional con las temperaturas registradas.
    :param ciudades: Lista con los nombres de las ciudades.
    :param semanas: Número de semanas registradas.
    :param dias_semana: Lista con los días de la semana.
    :return: Diccionario con el promedio de temperaturas por ciudad.
    """
    promedios_ciudades = {}
    for i, ciudad in enumerate(ciudades):
        total_temperaturas = sum(sum(temperaturas[i][semana]) for semana in range(semanas))
        promedio_ciudad = total_temperaturas / (semanas * len(dias_semana))
        promedios_ciudades[ciudad] = round(promedio_ciudad, 2)
    return promedios_ciudades

# Definición de dimensiones de la matriz
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
ciudades = ["Quito", "Guayaquil", "Cuenca"]
semanas = 4  # Ahora usando 4 semanas

# Matriz de temperaturas aleatorias entre 10 y 35 grados Celsius
temperaturas = [[[random.randint(10, 35) for _ in dias_semana] for _ in range(semanas)] for _ in ciudades]

# Calculo de los promedios
promedios = calcular_promedio_temperaturas(temperaturas, ciudades, semanas, dias_semana)
for ciudad, promedio in promedios.items():
    print(f"Temperatura promedio en {ciudad}: {promedio}°C")
