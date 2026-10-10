# Libreria estandar
import time

# Libreria de terceros
import numpy as np


def calculador_perdidas(nodos:int, mediciones_scada:list):
    assert nodos>=0

    if nodos=0:
        return 0.0
        
    # Casos base
    costos = np.zeros(nodos+1)
    costos[1] = mediciones_scada[0]

    # LLenar hacia arriba usado iteracion
    for i in range(2,nodos+1):
        valor = mediciones_scada[i-1]
        costos[i] = min(costos[i-1] + valor, costos[i-2] + valor * 0.8)

    return float(costos[nodos])