# Ejercicio 3 - Auditoría con tests unitarios e integración web

from utils import obtener_metricas_consumo

# Punto B
registros = [
    {"planta": "Mendoza", "consumo_kwh": 1000},
    {"planta": "San Juan", "consumo_kwh": 2000},
    {"planta": "Cordoba", "consumo_kwh": 1500}
]

metricas = obtener_metricas_consumo(registros)

print(metricas)