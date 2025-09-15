# Función para convertir Fahrenheit a Celsius
from semana12.RegistrodeTemperaturasDiarias import temperaturas


def fahrenheit_a_celsius(f):
    return (f - 32) * 5 / 9


# Función para calcular el promedio de temperatura de cada ciudad
def promedio_por_ciudad(temperaturas, ciudades):
    promedios_ciudades = {}

    for ciudad_idx, ciudad in enumerate(temperaturas):  # Recorre ciudades
        suma_total = 0
        conteo_dias = 0

        for semana in ciudad:  # Recorre semanas
            for dia in semana:  # Recorre días
                suma_total += fahrenheit_a_celsius(dia["temp"])
                conteo_dias += 1

        promedio_ciudad = suma_total / conteo_dias
        promedios_ciudades[ciudades[ciudad_idx]] = promedio_ciudad

    return promedios_ciudades


# ---- Ejemplo de uso ----
ciudades = ["Ciudad 1 Cuenca", "Ciudad 2 Loja", "Ciudad 3 Ambato"]

resultado = promedio_por_ciudad(temperaturas, ciudades)

# Mostrar resultados
for ciudad, promedio in resultado.items():
    print(f"{ciudad}: {promedio:.2f} °C")


