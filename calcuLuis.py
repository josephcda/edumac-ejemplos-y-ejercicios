# -*- coding: utf-8 -*-
import math
pi = math.pi

def circulo (radio):
        resultado = pi*(radio**2)
        return resultado

def circulo_peri (diametro):
        resultado = pi*(diametro)
        return resultado

def triangulo (a,b):
        resultador= b*a/2
        return resultador

def triangulo_peri (lado_a,lado_b,lado_c):
        resultador= lado_a+lado_b+lado_c
        return resultador

def cuadrado (c):
        resultadom= c**2
        return resultadom

def cuadrado_peri (d):
        resultadow = d+d+d+d
        return resultadow

def rectangulo (e,f):
        resultadod= e*f
        return resultadod

def rectangulo_peri (e,f):
        resultadod= 2*e(2*f)
        return resultadod

def pentagono (g,h):
        resultadoz= 5*g*h/2
        return resultadoz

def pentagono_peri(i):
        resultadoz= 5*i
        return resultadoz

def hexagono (j,k):
        resultadoz= 6*j*k/2
        return resultadoz

def hexagono_peri(l):
        resultadoz= 6*l
        return resultadoz

def heptagono (m,n):
        resultadoz= 7*m*n/2
        return resultadoz

def heptgono_peri(o):
        resultadoz= 7*o
        return resultadoz

def octagono (p,q):
        resultadoz= 8*p*q/2
        return resultadoz

def octagono_peri(r):
        resultadoz= 8*r
        return resultadoz

def nonagono (s,t):
        resultadoz= 9*s*t/2
        return resultadoz

def nonagono_peri(u):
        resultadoz= 9*u
        return resultadoz

def decagono (v,x):
        resultadoz= 10*v*x/2
        return resultadoz

def decagono_peri(y):
        resultadoz= 10*y
        return resultadoz

eleccion = input(" Si quieres circulo escoge 1,si quieres triangulo escoge 2,si quieres cuadrado escoge 3,si quieres rectangulo escoge 4,si quiere un pentagono escoge 5,si quiere un hexagono escoge 6,si quiere un hexagono escoge 7,si quiere un hexagono escoge 8,si quiere un hexagono escoge 9,si quiere un hexagono escoge 10 ")
elecciondos = input("Escoge 11 si quieres area ó 12 si quieres perimetro ")

if eleccion == 1:
        if elecciondos == 11:
                radio = input("Agregame tu radio aqui ")
                resultado = circulo(radio)
                print resultado
        elif elecciondos == 12:
                diametro = input ("Agregame tu diametro aqui")
                resultado = circulo(diametro)
                print resultado

elif eleccion == 2:
        if elecciondos == 11:
                a= input("Escribe altura ")
                b= input("Escribe base ")
                resultador = triangulo(a,b)
                print resultador
        elif elecciondos == 12:
                lado_a= input("Escribe lado 1; ")
                lado_b= input("Escribe lado 2; ")
                lado_c= input("Escribe lado 3; ")
                resultador = triangulo(lado_a,lado_b,lado_c)
                print resultador

elif eleccion == 3:
        if elecciondos == 11:
                c= input("Escribe lado ")
                resultadom = cuadrado(c)
                print resultadom
        elif elecciondos == 12:
                d= input("Escribe lado ")
                resultadow = cuadrado_peri(d)
                print resultadow

elif eleccion == 4:
        if elecciondos == 11:
                e= input("Escribe altura ")
                f= input("Escribe base ")
                resultadod = rectangulo (e,f)
                print resultadod
        elif elecciondos == 12:
                e= input("Escribe altura ")
                f= input("Escribe base ")
                resultadod = rectangulo (e,f)
                print resultadod

elif eleccion == 5:
        if elecciondos == 11:
                g= input("Escribe lado ")
                h= input("Escribe radio ")
                resultadoz = pentagono(g,h)
                print resultadoz
        elif elecciondos == 12:
                i= input("Escribe lado ")
                resultadoz = pentagono_peri(i)
                print resultadoz

elif eleccion == 6:
        if elecciondos == 11:
                j= input("Escribe lado ")
                k= input("Escribe radio ")
                resultadoa = hexagono(j,k)
                print resultadoa
        elif elecciondos == 12:
                l= input("Escribe lado ")
                resultadoa = hexagono_peri(l)
                print resultadoa

elif eleccion == 7:
        if elecciondos == 11:
                m= input("Escribe lado ")
                n= input("Escribe radio ")
                resultadob = hexagono(m,n)
                print resultadob
        elif elecciondos == 12:
                o= input("Escribe lado ")
                resultadob = hexagono_peri(o)
                print resultadob

elif eleccion == 8:
        if elecciondos == 11:
                p= input("Escribe lado ")
                q= input("Escribe radio ")
                resultadoc = hexagono(p,q)
                print resultadoc
        elif elecciondos == 12:
                r= input("Escribe lado ")
                resultadoc = hexagono_peri(r)
                print resultadoc

elif eleccion == 9:
        if elecciondos == 11:
                s= input("Escribe lado ")
                t= input("Escribe radio ")
                resultadoe = nonagono(s,t)
                print resultadoe
        elif elecciondos == 12:
                u= input("Escribe lado ")
                resultadoe = nonagono_peri(u)
                print resultadoe

elif eleccion == 10:
        if elecciondos == 11:
                v= input("Escribe lado ")
                x= input("Escribe radio ")
                resultadof = decagono(v,x)
                print resultadof
        elif elecciondos == 12:
                y= input("Escribe lado ")
                resultadof = decagono_peri(y)
                print resultadof
