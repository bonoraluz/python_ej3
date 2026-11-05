def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo")

    return consumo_kwh * factor_emision


def obtener_metricas_consumo(registros):

    total_emisiones = 0
    mayor_consumo = 0
    planta_mayor_consumo = ""

    for registro in registros:

        planta = registro["planta"]
        consumo = registro["consumo_kwh"]

        emisiones = calcular_emisiones_carbono(consumo)

        total_emisiones += emisiones

        if consumo > mayor_consumo:
            mayor_consumo = consumo
            planta_mayor_consumo = planta

    return {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo,
        "mayor_consumo": mayor_consumo
    }



