#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script select the minimun cost for the electricity for selected hours
Usage:

"""

# Importo las funciones utilizadas
# import ...


# Importo la configuración del fichero
from config.auth import *

# Seleccionar el intervalo de horas indicado con el precio más bajo
def startStopRoutine(onHours):
# Vacio la lista de precios auxiliar que uso para calcular el mínimo precio en el rango de horas seleccionado
    minPriceList = []

    # Relleno la lista de precios auxiliar que uso para calcular cuando arrancar los equipos
    for i in range(0, len(priceList)+1-onHours):
        minPriceList.append(sum(priceList[i:i+onHours]))

    # Busco el mínimo de esa lista auxiliar para encontrar del rango delimitado por las horas
    startDevice = minPriceList.index(min(minPriceList))
    stopDevice = startDevice + onHours

    # Devuelvo la hora de aranque y de paro del dispositivo
    return startDevice, stopDevice


# Seleccionar el número de horas indicados cuyos precios sean más bajos
def minSelection(onHours, hour):
    if hour == 23:
        enableHours = 0
    minPriceList2 = sorted(priceList)
    priceLimit = minPriceList2[onHours]
    if priceLimit < priceList[hour] and enableHours <= onHours:
        enableHours += 1
        enable = 1
    else:
        enable = 0


# Realizo la elección del minimo valor de la electricidad en el número de horas seleccionadas
def main():
    # Meto por Terminal el número de horas que estará en marcha el dispositivo
    onHours = int(input("¿Cuántas horas estará en marcha el dispositivo? "))

    # Llamo a la función que determina el arranque paro del dispositivo
    startDevice, stopDevice = startStopRoutine(onHours)
    print(startDevice, stopDevice)


if __name__ == "__main__":
	main()