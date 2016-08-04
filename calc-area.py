circulo = 1
rectangulo = 2
triangulo = 3

eleccion = input ("area del circulo 1\narea del rectangulo 2\narea del triangulo 3\n")
if eleccion == 1:
    radio = input ("cual es el radio del circulo?")
    area1 = (3.14 * (radio ** 2))
    print str (area1)
elif eleccion == 2:
    b = input ("cuanto mide la base de tu cuadrado?")
    c = input ("cuanto mide la altura de tu cuadrado?")
    area2 = b * c
    print str (area2)
elif eleccion == 3:
    d = input ("cual es la base de tu triangulo?")
    e = input ("cual es la altura de tu triangulo?")
    area3 = d * e / 2
    print str (area3)
