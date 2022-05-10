"""
    Funcoes de cartas do baralho
    TO DO:
        Funcoes em paralelo em python
       
    @author: claudiorogerio
"""

import pygame
from pygame.locals import *
import time
from pygame import mixer
from gtts import gTTS
import os
from io import BytesIO
from cartas import *
from lista_cartas import *

SHOW = 1 # mostra resulados no bash
DELAY = 1 # ativa delay da visualizacao de cartas

TRANSLATE = 0
def play_google( texto, id ):
    if TRANSLATE:
        try:
            # google audio engine
            print( "On line" )
            eng = gTTS( text = texto, lang='pt', slow=False )
            mp3_file =BytesIO()
            eng.write_to_fp( mp3_file )
            eng.save( 'texto.mp3' )
        except:
            print( "Off line play" )

    mixer.init(18100)
    if id == 1:
        mixer.music.load( 'texto1.mp3' )
    if id == 2:
        mixer.music.load( 'texto2.mp3' )
    if id == 3:
        mixer.music.load( 'texto3.mp3' )

    mixer.music.play()


def image_display( surf, filename, xy ):
    img = pygame.image.load( filename )
    surf.blit( img, xy )

def show_msg( screen, text , size, posx, posy ):
    basicfont = pygame.font.SysFont(None, size)
    text = basicfont.render(text, True, (25, 0, 0))

    textrect = text.get_rect()
    textrect.centerx = posx
    textrect.centery = posy
    text.set_alpha(90)
    screen.blit(text, textrect)

# add textura de fundo
def show_background( screen, texture, x, y, delta ):

    i = 0
    while i <= (x-delta):
        j = 0
        while j <= (y-delta):
            screen.blit( texture, [i,j] )
            j = j+delta
        i = i+delta

def show_buttons( screen ):
    button_1 = pygame.transform.scale( pygame.image.load( "./images/botoes/botao_1.png" ), (70,70) )
    button_2 = pygame.transform.scale( pygame.image.load( "./images/botoes/botao_2.png" ), (70,70) )
    button_3 = pygame.transform.scale( pygame.image.load( "./images/botoes/botao_3.png" ), (70,70) )
    screen.blit( button_1, [270, 660] )
    screen.blit( button_2, [600, 660] )
    screen.blit( button_3, [930, 660] )

# mostra carta unitaria com posicao x y
def show_card( screen, card, x, y ):
    screen.blit( card, [x, y] )

def show_final_card( screen, card ):
    dimx = 110
    dimy = 150
    ang = 90
    dirc = './images/cards/cartasantigas/'
    for n in range(1,11):
        card_fundo = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "C.png" ), ang), (dimx,dimy) )
        show_card( screen, card_fundo, 100+88*n, 250+(n*3) )
        pygame.display.update()
        time.sleep( 0.1 )
        ang +=4
    show_card( screen, card, 120+80*12, 280 )

# mostra uma lista de cartas
def show_list_card( screen, list, dict ):
    initial = 110
    i=initial
    delta_i = 55
    delta_j = 300
    j = 200
    for k in list:
        for x in k:
            for cd in cards:
                if x == cd:
                    show_card( screen, dict[x], j, i )
                    if DELAY:
                        pygame.display.update()
                        time.sleep(0.05)
                    #if SHOW:
                        #print " Lista %s " %(x)
                    i= i + delta_i
                    j = j+5 # arredar as cartas
        i= initial
        j = j+ delta_j


def loop_grafica( list ):
  pygame.init()

  #defi de icone do jogo
  gameIcone = pygame.transform.rotate( pygame.image.load("./images/cards/cartasantigas/AC.png" ), 0)
  pygame.display.set_icon( gameIcone )

  display_width = 1400
  display_height = 900
  gameDisplay = pygame.display.set_mode( (display_width, display_height), RESIZABLE)
  pygame.display.set_caption('----- Dream cards -----')
  clock = pygame.time.Clock()


  white = (25,180,25)
  background_img = pygame.image.load("./images/tapete-v01.png" ).convert()

#  logo = pygame.image.load("./images/secomp-1.png" )
  dict_cards = {}
  dimx = 120 # 140
  dimy = 210 # 190
  dirc = './images/cards/cartasantigas/'
  angle = 0
  dict_cards["AC "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "AC.png" ), angle), (dimx,dimy) )
  dict_cards["2C "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "2C.png" ), angle), (dimx,dimy) )
  dict_cards["3C "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "3C.png" ), angle), (dimx,dimy) )
  dict_cards["4C "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "4C.png" ), angle), (dimx,dimy) )
  dict_cards["5C "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "5C.png" ), angle), (dimx,dimy) )
  dict_cards["6C "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "6C.png" ), angle), (dimx,dimy) )
  dict_cards["7C "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "7C.png" ), angle), (dimx,dimy) )
  dict_cards["8C "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "8C.png" ), angle), (dimx,dimy) )
  dict_cards["9C "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "9C.png" ), angle), (dimx,dimy) )
  dict_cards["10C"] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "10C.png" ), angle), (dimx,dimy) )
  dict_cards["JC "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "JC.png" ), angle), (dimx,dimy) )
  dict_cards["QC "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "QC.png" ), angle), (dimx,dimy) )
  dict_cards["KC "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "KC.png" ), angle), (dimx,dimy) )

  dict_cards["AE "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "AE.png" ), angle), (dimx,dimy) )
  dict_cards["2E "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "2E.png" ), angle), (dimx,dimy) )
  dict_cards["3E "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "3E.png" ), angle), (dimx,dimy) )
  dict_cards["4E "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "4E.png" ), angle), (dimx,dimy) )
  dict_cards["5E "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "5E.png" ), angle), (dimx,dimy) )
  dict_cards["6E "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "6E.png" ), angle), (dimx,dimy) )
  dict_cards["7E "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "7E.png" ), angle), (dimx,dimy) )
  dict_cards["8E "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "8E.png" ), angle), (dimx,dimy) )
  dict_cards["9E "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "9E.png" ), angle), (dimx,dimy) )
  dict_cards["10E"] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "10E.png" ), angle), (dimx,dimy) )
  dict_cards["JE "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "JE.png" ), angle), (dimx,dimy) )
  dict_cards["QE "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "QE.png" ), angle), (dimx,dimy) )
  dict_cards["KE "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "KE.png" ), angle), (dimx,dimy) )

  dict_cards["AO "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "AO.png" ), angle), (dimx,dimy) )
  dict_cards["2O "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "2O.png" ), angle), (dimx,dimy) )
  dict_cards["3O "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "3O.png" ), angle), (dimx,dimy) )
  dict_cards["4O "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "4O.png" ), angle), (dimx,dimy) )
  dict_cards["5O "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "5O.png" ), angle), (dimx,dimy) )
  dict_cards["6O "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "6O.png" ), angle), (dimx,dimy) )
  dict_cards["7O "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "7O.png" ), angle), (dimx,dimy) )
  dict_cards["8O "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "8O.png" ), angle), (dimx,dimy) )
  dict_cards["9O "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "9O.png" ), angle), (dimx,dimy) )
  dict_cards["10O"] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "10O.png" ), angle), (dimx,dimy) )
  dict_cards["JO "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "JO.png" ), angle), (dimx,dimy) )
  dict_cards["QO "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "QO.png" ), angle), (dimx,dimy) )
  dict_cards["KO "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "KO.png" ), angle), (dimx,dimy) )

  dict_cards["AP "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "AP.png" ), angle ), (dimx,dimy) )
  dict_cards["2P "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "2P.png" ), angle ), (dimx,dimy) )
  dict_cards["3P "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "3P.png" ), angle ), (dimx,dimy) )
  dict_cards["4P "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "4P.png" ), angle ), (dimx,dimy) )
  dict_cards["5P "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "5P.png" ), angle ), (dimx,dimy) )
  dict_cards["6P "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "6P.png" ), angle ), (dimx,dimy) )
  dict_cards["7P "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "7P.png" ), angle ), (dimx,dimy) )
  dict_cards["8P "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "8P.png" ), angle ), (dimx,dimy) )
  dict_cards["9P "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "9P.png" ), angle ), (dimx,dimy) )
  dict_cards["10P"] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "10P.png" ), angle ), (dimx,dimy) )
  dict_cards["JP "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "JP.png" ), angle ), (dimx,dimy) )
  dict_cards["QP "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "QP.png" ), angle ), (dimx,dimy) )
  dict_cards["KP "] = pygame.transform.scale( pygame.transform.rotate( pygame.image.load( dirc + "KP.png" ), angle ), (dimx,dimy) )
  #dict_cards["KP "] = pygame.image.load("./images/cards/cartasnova/KP.png" ).convert()

  show_background( gameDisplay, background_img, display_width, display_height, 80 )
  show_msg( gameDisplay, "Ei Vc! Escolha uma carta. Eu vou adivinhar sua carta!  ", 48 , 600, 20 )
  #show_msg( gameDisplay, "Eu vou adivinhar sua carta! ", 48 , 600, 60 )
  time.sleep(1)
  show_list_card( gameDisplay, list, dict_cards )
  show_msg( gameDisplay, "Concentre-se nela e click em qual lista sua carta encontra-se: 1, 2 ou 3? ", 50 , 700, 60 )
  show_buttons( gameDisplay )

  # parametro 1 , texto, parametro 2 arquivo ja captado
  play_google( "Escolha uma carta. E apenas diga em qual lista sua carta se encontra: 1, 2 ou 3",1 )

  fim = False # mudar para o participante queira sair
  count = 0 # contagem de embaralhar as cartas
  UPDATE = 0
  FINAL = 0
  while not fim:

      # evento de acoes do programa
      for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONUP:
              x,y = pygame.mouse.get_pos()
              print( " %s %s " %( x, y ) )

              # eventos de acoes para os botoes de cada lista
              if (x>250 and x<360) and (y>660 and y<890):
                  print (" fila 0")
                  count +=1
                  UPDATE = 1
                  fila = 0

              if (x>570 and x<680) and (y>660 and y<890):
                  print (" fila 1")
                  count +=1
                  UPDATE = 1
                  fila = 1

              if (x>910 and x<990) and (y>660 and y<890):
                  print(" fila 2")
                  count +=1
                  UPDATE = 1
                  fila = 2
              if count == -1:
                  count = 0
                  UPDATE = 1

          if event.type == pygame.KEYDOWN:
              #print "%s" %(event.key)

              if event.key == pygame.K_LEFT or event.key == 49 :
                  fila = 0
                  count += 1
                  UPDATE = 1
                  if SHOW:
                      print( " Lista %s " %(fila+1) )

              if event.key == pygame.K_DOWN or event.key == 50 :
                  fila = 1
                  count +=1
                  UPDATE = 1
                  if SHOW:
                      print( " Lista %s " %(fila+1) )

              if event.key == pygame.K_RIGHT or event.key == 51 :
                  fila = 2
                  count +=1
                  UPDATE = 1
                  if SHOW:
                      print( " Lista %s " %(fila+1) )

               # tecla esc = 27
              if event.key == 27:
                  fim = True

          if count == 3:
              print( " %s count " %(count))
              print(" Sua carta e %s"%( list[1][3] ))
              UPDATE = 0
              FINAL = 1
              count = 0

          if UPDATE :
               list = update_cartas( list , fila )
               show_background( gameDisplay, background_img, display_width, display_height, 100 )
               if count == 0 :
                   show_msg( gameDisplay, "Ei Vc! Escolha uma carta. Eu vou adivinhar sua carta!  ", 48 , 600, 20 )
                   show_msg( gameDisplay, "Concentre-se nela e click em qual lista sua carta encontra-se: 1, 2 ou 3? ", 50 , 700, 60 )
                   play_google( "Escolha uma carta. E apenas diga em qual lista sua carta se encontra: 1, 2 ou 3",1 )

               else:
                   play_google( "Novamente em qual lista 1, 2 ou 3", 2 )
                   show_msg( gameDisplay, "Diga novamente em qual lista sua carta encontra-se: 1, 2 ou 3? ", 50 , 700, 60 )
               show_list_card( gameDisplay, list, dict_cards )
               show_buttons( gameDisplay )


               UPDATE = 0
               if SHOW:
                   for k in list:
                       print( " %s..." %(k) )
                       print( " Lista %s " %(fila+1) )
          if FINAL:
               list = update_cartas( list , fila )
               play_google("Essa foi sua carta. Obrigado!", 3)
               show_background( gameDisplay, background_img, display_width, display_height, 100 )

               show_final_card( gameDisplay, dict_cards[ list[1][3] ] )
               #show_card( screen, dict[x], j, i )
               show_msg( gameDisplay, "Vc escolheu a carta: ", 55 , 700, 100 )
               #show_msg( gameDisplay, list[1][3], 60 , 700, 100 )
#               show_card( gameDisplay, logo, 600, 500 )
               FINAL = 0
               count = -1



          if event.type == pygame.QUIT:
              fim = True
#          if event.key == K_ESCAPE:
#              fim = True


      clock.tick(60)

      pygame.display.update()
