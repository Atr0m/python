#!/usr/bin/env python

ssid = raw_input("Por favor introduzca el ICC:")
j = 0
l = 0
cadena =""
lista=[]
if len(ssid) == 20 and ssid[len(ssid) - 1] == "F" :
    while j < len(ssid)/2:
        lista.append(ssid[l:l+2])
        j += 1
        l += 2
    for elemento in lista:
        cadena += elemento[1]+elemento[0]   
    print ("El ICC es: ")+cadena
else:
    print "El ICC no es correcto."
