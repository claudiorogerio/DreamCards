"""
    Funcoes de cartas do baralho
    TO DO:
        Funcoes em paralelo em python

    @author: claudiorogerio
"""
from sorteio_cartas import * # importar variaveis globais

def criar_lista( cartas ):
    list_cards = []
    list_cards.append( [] )
    list_cards.append( [] )
    list_cards.append( [] )
    x=0
    y=0
    for k in cartas:
        list_cards[x].append(k)
    #print " Premiados %s %s %s" %( list_cards[x][y], x ,y )
    #print "Premiados %s" %(list[x][y])
        y=y+1
        if y==7:
          x=x+1
          y=0

    if SHOW:
        print( "Terminou" )
    return list_cards

# altera posicao das lista das cartas
def update_cartas( cartas, controle ):
    # nova lista
    list_upd = []
    list_upd.append( [] )
    list_upd.append( [] )
    list_upd.append( [] )

    list_final = []
    list_final.append( [] )
    list_final.append( [] )
    list_final.append( [] )


    #criar um rand inteiro e mudar o tipo de posicao de carta
    s=random.choice
    rd = s('01') # gera '0' ou '1'

    if rd == '0':
        print( "" )
        print( "Zero")
    else:
        print( "" )
        print( "Um" )

    x = 0
    if controle == 0:
        list_upd[0] = cartas[1]
        list_upd[1] = cartas[0]
        list_upd[2] = cartas[2]
        print( "aqui 1" )

    if controle == 1:
        list_upd = cartas
        print( "aqui 2")

    if controle == 2:
        list_upd[0] = cartas[0]
        list_upd[1] = cartas[2]
        list_upd[2] = cartas[1]
        print( "aqui 3" )

    a = 0
    b = 0
    cont = 0
    #for n in reversed( list_aux ):
    for nn in reversed( list_upd ):
        for nnn in reversed( nn ):
            print(" .. %s  %s     %s %s   " %( cont, nnn, a, b ) )
            list_final[a].append(nnn)
            a += 1

            if a == 3:
                a = 0
                b += 1
                if b == 7:
                    b = 0

            cont +=1

    #print" lista final"
    #for lista1 in list_final:
    #    print"%s....."%(lista1)
            #print"..%s"%(k)

    return list_final
