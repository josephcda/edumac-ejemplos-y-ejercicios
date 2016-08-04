# -*- coding: utf-8 -*-
total = input ("cuanto ganaste en el año")
totalgastos = []
for i in range (1,12):
    gastos = input("cuanto gastaste en el mes?" + str(i))
    totalgastos.append(gastos)
    total_gastos = sum(list)
operacion = total - total_gastos
if operacion >= 0:
    print "no te queda dinero"
elif operacion < 0:
    print "te quedan" + str(operacion)
