# Θ - Latitud
# alfa - Longitud

import math

R = 3963

def main():

    latitud_a = float(input("Ingresa latitud A\n>"))
    longitud_a = float(input("Ingresa longitud A\n>"))

    latitud_a = (latitud_a / 180.0) * math.pi
    longitud_a = (longitud_a / 180.0) * math.pi


    latitud_b = float(input("Ingresa latitud B\n>"))
    longitud_b = float(input("Ingresa longitud B\n>"))

    latitud_b = (latitud_b / 180.0) * math.pi
    longitud_b = (longitud_b / 180.0) * math.pi

    distance = R * math.acos((math.sin(latitud_a) * math.sin(latitud_b)) + math.cos(latitud_a) * math.cos(latitud_b) * math.cos(longitud_b - longitud_a))

    return distance * 1.609344


print(main())