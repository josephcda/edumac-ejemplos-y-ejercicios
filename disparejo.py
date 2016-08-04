from random import randint
a = randint (1,2)
b = randint (1,2)
usuario = input("arriba = 1 \nabajo = 2\n")
usuario = str(usuario)
maquina1 = str(a)
maquina2 = str(b)
if maquina1 == 1 and maquina2 == 1 and usuario == 2:
    print "ganaste"
elif maquina1 == 2 and maquina2 == 2 and usuario == 1:
        print "ganaste"
elif  maquina1 == maquina2 == usuario:
    print "empate"
    print "Maquina1 eligio %s, maquina2 eligio %s tu elegiste %s " %(maquina1 , maquina2 ,usuario)

else:
    print "perdiste"
    print "Maquina1 eligio %s, \nmaquina2 eligio %s \ntu elegiste %s " %(maquina1 , maquina2 ,usuario)
