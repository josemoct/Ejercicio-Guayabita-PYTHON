# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from random import randint, uniform,random
import random

def minimo_apuesta():
	return random.randrange(10,200,10)
def bolsillo():
	return random.randrange(200,1000,10)
def lanzar_dados():
    return randint(1,6)
#MANTENIENDO AL JUGADOR JUGANDO
def mantener_en_el_juego(dadoAnterior,dadoActual,dineroP1,dineroP2,dineroMesa,apuestaMinima,inicio,jugador):
	print "Dinero P1: "+str(dineroP1)
	print "Dinero P2: "+str(dineroP2)
	if inicio:
		dineroMesa = apuestaMinima*2
		print "Case: "+str(apuestaMinima)
		print "Ambos jugadores apuestan el minimo"
		dineroP1-=apuestaMinima
		dineroP2-=apuestaMinima
		print "Dinero de mesa: "+str(dineroMesa)
	else:
		print "Dinero de mesa: "+str(dineroMesa)	
	#print "P1 apuesta: "+str(hacer_apuesta2(dineroP1,apuestaMinima))
	if(dineroP1 <= apuestaMinima):
		print "P1 ha perdido por falta de dinero, gana P2"
		return 
	elif(dineroP2 <= apuestaMinima):
		print "P2 ha perdido por falta de dinero, gana P1"
		return
	if(jugador==1):
		print "P1 Sacó: "+str(dadoAnterior)
		if(dadoAnterior==1 or dadoAnterior==6):
			print "P1 ha perdido el turno"
			mantener_en_el_juego(lanzar_dados(),lanzar_dados(),dineroP1,dineroP2,dineroMesa,apuestaMinima,False,2)
		elif(dadoAnterior==dadoActual or dadoAnterior>dadoActual):
			print "P1 Saca ahora: "+str(dadoActual)			
			print "El jugador 1 pierde el Case: "+str(apuestaMinima)
			dineroP1-=apuestaMinima
			dineroMesa+=apuestaMinima
			mantener_en_el_juego(lanzar_dados(),lanzar_dados(),dineroP1,dineroP2,dineroMesa,apuestaMinima,False,2)
		elif(dadoActual>dadoAnterior):
			print "P1 Saca ahora: "+str(dadoActual)			
			print "Jugador 1 ha gando dinero de la mesa: "+str(dineroMesa)
			dineroP1+=dineroMesa
			dineroMesa=0
			print "todos vuelven a dar el Case"
			dineroP1-=apuestaMinima
			dineroP2-=apuestaMinima
			dineroMesa=apuestaMinima*2
			mantener_en_el_juego(lanzar_dados(),lanzar_dados(),dineroP1,dineroP2,dineroMesa,apuestaMinima,False,2)
	elif(jugador==2):
 		print "P2 Sacó: "+str(dadoAnterior)
 		if(dadoAnterior==1 or dadoAnterior==6):
 			print "Jugador 2 ha perdido turno"
 			mantener_en_el_juego(lanzar_dados(),lanzar_dados(),dineroP1,dineroP2,dineroMesa,apuestaMinima,False,1)
 		elif(dadoAnterior==dadoActual or dadoAnterior>dadoActual):
 			print "P2 Saca ahora: "+str(dadoActual)			
 			print "El jugador 2 pierde el Case: "+str(apuestaMinima)
 			dineroP2-=apuestaMinima
 			dineroMesa+=apuestaMinima
 			mantener_en_el_juego(lanzar_dados(),lanzar_dados(),dineroP1,dineroP2,dineroMesa,apuestaMinima,False,1)
 		elif(dadoActual>dadoAnterior):
 			print "P2 Saca ahora: "+str(dadoActual)			
 			print "Jugador 2 ha gando dinero de la mesa: "+str(dineroMesa)
 			dineroP2+=dineroMesa
 			dineroMesa=0
 			print "todos vuelven a dar el Case"
 			dineroP1-=apuestaMinima
 			dineroP2-=apuestaMinima
 			dineroMesa=apuestaMinima*2
 			mantener_en_el_juego(lanzar_dados(),lanzar_dados(),dineroP1,dineroP2,dineroMesa,apuestaMinima,False,1)

mantener_en_el_juego(lanzar_dados(),lanzar_dados(),bolsillo(),bolsillo(),0,minimo_apuesta(),True,1)
