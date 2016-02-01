#!/usr/bin/env python
# -*-coding:utf-8-*-
#Juego de piedra papel y tijera con funciones aleatorias
import time
from  time import sleep
import random

sus = "-" * 35
depo = ["piedra", "papel", "tijera"]

#Ciclo continuo
while True:
    x = raw_input("Que elijes? piedra, papel o tijera: ")
    if x not in depo:
        print("No hagas Trampa!!! :P\n")
        continue #programa salta al siguiente Ciclo

    pc = random.choice(depo) #eleccion aleatoria
    sleep(0.5) #Espera de la computadora
    print(("computadora elijio {}.").format(pc)) #primer par de paretesis python 3
    #equivalente a
    #print "Computadora elijio %s." % pc
    if x == pc :
        print "\nEmpate."
    elif x == "piedra" and pc == "tijera" :
        print "\nGanaste!! :D"
    elif x == "papel" and pc == "piedra" :
        print "\nGanaste!! :D"
    elif x == "tijera" and pc == "papel" :
        print "\nGanaste!! :D"
    else :
        print "Perdiste. XD :P :| \n{} gana {} \n".format(pc, x)
    print sus
