#encoding: UTF-8
#Autor: Astrid M. Villegas Berdejo
#Tarea 3 melodia

from Myro import *

fa = 698.456
sol = 783.991
la = 880
re = 587.33
mi = 659.255
do = 523.251

def reproducirCompasUno (duracion):
    beep (duracion, fa)
    beep (duracion, fa)
    beep (duracion, sol)
    beep (duracion, la)
    
def reproducirCompasDos (duracion):
    beep (duracion, la)
    beep (duracion, sol)
    beep (duracion, fa)
    beep (duracion, mi)
    
def reproducirCompasTres (duracion):
    beep (duracion, re)
    beep (duracion, re)
    beep (duracion, mi)
    beep (duracion, fa)
    
def reproducirCompasCuatro (duracion):
    beep (duracion/2, fa)
    beep (duracion/2, 0)
    beep (duracion/2, mi)
    beep (2*duracion, mi)   
    
def reproducirCompasNueve (duracion):
    beep (duracion, mi)
    beep (duracion, mi)
    beep (duracion, fa)
    beep (duracion, re)
    
def reproducirCompasDiez (duracion):
    beep (duracion, mi)
    beep (duracion, fa)
    beep (duracion/2, mi)
    beep (duracion/2, sol)
    beep (duracion, mi)
    beep (duracion, re)
    
def reproducirCompasOnce (duracion):
    beep (duracion, mi)
    beep (duracion, fa)
    beep (duracion/2, mi)
    beep (duracion/2, sol)
    beep (duracion, mi)
    beep (duracion, mi)
    
def reproducirCompasDoce (duracion):
    beep (duracion, re)
    beep (duracion, mi)
    beep (duracion, la)
    beep (duracion, fa)
    
    
tiempo = .25

reproducirCompasUno (tiempo)
reproducirCompasDos (tiempo)
reproducirCompasTres (tiempo)
reproducirCompasCuatro (tiempo)
reproducirCompasUno (tiempo)
reproducirCompasDos (tiempo)
reproducirCompasTres (tiempo)
reproducirCompasCuatro (tiempo)
reproducirCompasNueve (tiempo)
reproducirCompasDiez (tiempo)
reproducirCompasOnce (tiempo)
reproducirCompasDoce (tiempo)
reproducirCompasUno (tiempo)
reproducirCompasDos (tiempo)
reproducirCompasTres (tiempo)
reproducirCompasCuatro (tiempo)