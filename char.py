class Charmander(object):
    def __init__(self, tipo, ataque, color):
        self.tipo = tipo
        self.ataque = ataque
        self.color = color
class Charizard(Charmander):
    def __init__(self, tipo, ataque, color, tamanio):
        Charmander.__init__(self,tipo, ataque, color)
        self.tamanio = tamanio

a = Charizard("Dragon", "128", "Naranja", "Un chingo muy grande")
print a.tipo
