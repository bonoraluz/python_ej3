from django.shortcuts import render
from .utils import obtener_metricas_consumo

def vista_panel_sustentabilidad(request):

    registros = [
        {"planta": "Mendoza", "consumo_kwh": 1000},
        {"planta": "San Juan", "consumo_kwh": 2000},
        {"planta": "Cordoba", "consumo_kwh": 1500}
    ]

    metricas = obtener_metricas_consumo(registros)

    contexto = {
        "total_emisiones": metricas["total_emisiones"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "mayor_consumo": metricas["mayor_consumo"]
    }

    return render(request, "sustentabilidad/panel.html", contexto)