#!/usr/bin/env python
"""
Copyright 2013 Jorge Campo
Liberado con licencia GPLv3 (General Public License)

Este Script cambia los números de lugar dos a dos de una cadana de números de 20 dígitos y con una "F" en el penúltimo lugar.
"""

ssid = raw_input("Por favor introduzca el ICC:")    # Introduce la cadena de 20 dígitos
j = 0
l = 0
cadena =""
lista=[]
if len(ssid) == 20 and ssid[len(ssid) - 1] == "F" :     # Comprueba que la cadena sea de 20 dígitos y que tenga una F en penúltimo lugar.
    while j < len(ssid)/2:      # Separa la cadena a pares
        lista.append(ssid[l:l+2])
        j += 1
        l += 2
    for elemento in lista:  # Invierte el lugar de los pares de dígitos
        cadena += elemento[1]+elemento[0]   
    print ("El ICC es: ")+cadena  # Imprime el número ya cambiado
else:
    print "El ICC no es correcto." # Imprime mensaje de error
