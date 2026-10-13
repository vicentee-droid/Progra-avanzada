# Libreria estandar
import time

# Librería de terceros
import numpy as np


def calculador_perdidas(nodos:int, mediciones_scada:list) ->float :
    """ 
    Calcula las perdidas de un alimentador de N nodos
    
    Args: 
        nodos (int): cantidad de nodos
        mediciones_scada (list): lista de mediciones de sensores scada

    Returns:
        float: perdidas del sistema
    """
    assert nodos>=0

    if nodos == 0:
        return 0.0

    try:
        # Se implementa programacion defensiva
        if len(medicones_scada) < nodos:
            raise ValueError("Mediciones insuficientes")

        # Casos base y cracion matriz de tabulación 
        costos = np.zeros(nodos+1)
        costos[1] = mediciones_scada[0]

        # LLenar hacia arriba usado iteracion
        for i in range(2,nodos+1):
            valor = mediciones_scada[i-1]
            
            costos[i] = min(costos[i-1] + valor, costos[i-2] + valor * 0.8)

        return float(costos[nodos])

    except (TypeError, ValueError) as e:
        print(f"Alerta SCADA: Datos corruptos encontrados. {e}")
        return 0.0