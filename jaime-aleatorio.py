from random import randint
aleatorio = randint (0,1000)
usuario = -1
contador = 0
while aleatorio != usuario:
    usuario = input ("escribe un numero del 0 al 1000\n")
    contador = contador + 1
    if type(usuario) == str or usuario >=1001 or usuario <= 0:
        print "eres un animal \nte pedi un numero\nno una letra"
    if aleatorio != usuario:
        print "intenta de nuevo"
if aleatorio == usuario:
   print "Adivinaste, en tan solo %s intentos" % str(contador)
