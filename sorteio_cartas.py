"""
    Funcoes de cartas do baralho
    TO DO:
        Funcoes em paralelo em python
        
    @author: claudiorogerio
"""

import random
global SHOW
SHOW = 0

def sorteio_cartas( cartas, limite ):

    sorteio=random.choice
    escolhidos=[]
    #selecionado=''
    total = len( cartas )
    print( " Total %s" %( total ) )

    #	for i in range(quant_prem):
    i=0
    while i < limite:
        selecionado = sorteio(cartas)
        #if i == 0 :


        if SHOW:
            print( "id: %s   carta: %s " %(i,escolhidos) )
      # se estiver dentro do vetor de premiados, nao fazer nada
        if selecionado in escolhidos:
            if SHOW:
                print( "  Out: ", selecionado )
    #    i=len(escolhidos)
        else:
            escolhidos.append( selecionado )
            if SHOW:
                print( "  On:  ", selecionado )
            i=i+1

    return escolhidos
