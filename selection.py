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


# Realizo la elección del minimo valor de la electricidad en el número de horas seleccionadas
def main():

    """
    Las cojo al final del fichero auth
    selectHours = 2
    electricityPriceList = [0.240, 0.205, 0.011, 0.103, 0.034, 0.045, 0.203, 0.554, 0.231, 0.210, 0.615, 0.271, 0.362,
    0.40, 0.232, 0.121, 0.131, 0.324, 0.745, 0.253, 0.554, 0.121, 0.871, 0.695]
    minPriceList = [999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 999.0,
    999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 999.0]
    """
    # Vacio la lista de precios auxiliar que uso para calcular el mínimo precio en el rango de horas seleccionado
    minPriceList = []

    for i in range(0, len(electricityPriceList)+1-selectHours):
        minPriceList.append(sum(electricityPriceList[i:i+selectHours]))

    # Busco el mínimo de esa lista y el índice
#    minPrice = min(minPriceList)
    print(minPriceList)
    startEquip = minPriceList.index(min(minPriceList))
    stopEquip = startEquip + selectHours

    print(startEquip)
    print(stopEquip)


if __name__ == "__main__":
	main()