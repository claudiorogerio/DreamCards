"""
    # exec: python jogo_cartas_v01.py
    #
    # python 3
    # sudo apt-get install python-pygame
    #
    # python3
    # sudo apt-get install python3-setuptools
    # sudo easy_install3 pip
    # sudo pip3.5 install pygame
    # install:  python -m pip install pyserial
    #
    @author: claudiorogerio

    TO DO:
        MIDI

"""

from cartas import *	
from sorteio_cartas import *
from lista_cartas import *
from visual import *
#from visual_cards import *

global list_cards

def main():
	#funcao random

	print( "------------------------------------------------------------" )

	quant_part = 52 # nao utilizado
	quant_prem = 21 # total de cartas sorteadas

	print( "\n  Cartas totais:", len( cards ) )

	# sorteio aleatorio das cartas
	premiados = sorteio_cartas( cards, quant_prem )

	print( "\nPremiados: %s \n" %(premiados) )
	print( "------------------------------------------------------------")

	list_cards = criar_lista( premiados )

	for k in list_cards:
		print( " Lista %s " %(k) )

	# inicia a parte visual da lista aleatoria
	loop_grafica( list_cards )

	pygame.quit()

	quit()


if __name__ == '__main__':
	main()
