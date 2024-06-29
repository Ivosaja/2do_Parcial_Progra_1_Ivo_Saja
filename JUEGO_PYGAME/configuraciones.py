#-----------------------CONFIGURACIONES-----------------------#
import pygame
import colores

pygame.init()

#DIMENSIONES DE LA PANTALLA
ANCHO_PANTALLA = 1000
ALTO_PANTALLA = 600
DIMENSIONES = (ANCHO_PANTALLA, ALTO_PANTALLA)
FPS = 30



#-----------------------PANTALLA PRINCIPAL-----------------------#
titulo_juego = 'GUESS THE LOGO'
icono = pygame.image.load('Imagenes/logo.png')
imagen_fondo = pygame.image.load('Imagenes/fondo_main.png')
imagen_fondo = pygame.transform.scale(imagen_fondo, DIMENSIONES)

#MUSICA
sonido_inicio_fin = pygame.mixer.Sound('Sonidos/intro_quizz.mp3')

#TITULO
ANCHO_TITULO =  350 
ALTO_TITULO = 300
pos_x_titulo = 331
pos_y_titulo = 30

DIMENSIONES_TITULO = (ANCHO_TITULO, ALTO_TITULO)
titulo_imagen = pygame.image.load('Imagenes/titulo.png')
titulo_imagen = pygame.transform.scale(titulo_imagen, DIMENSIONES_TITULO)

#BOTON JUGAR
ANCHO_BOTON_JUGAR = 130 
ALTO_BOTON_JUGAR = 50
pos_x_boton_jugar = 436
pos_y_boton_jugar = 380

#TEXTO BOTON
pos_x_texto = 464
pos_y_texto = 390
fuente_play = pygame.font.Font('Fuentes/gameplay_1987/GAMEPLAY-1987.ttf', 25)
texto_play = fuente_play.render('PLAY', False, colores.BLANCO)

#BOTON SONIDO
ANCHO_SONIDO = 55
ALTO_SONIDO = 55
imagen_sonido = pygame.image.load('Imagenes/sonido.png')
imagen_sonido = pygame.transform.scale(imagen_sonido, (ANCHO_SONIDO, ALTO_SONIDO))

imagen_sin_sonido = pygame.image.load('Imagenes/no_sonido.png')
imagen_sin_sonido = pygame.transform.scale(imagen_sin_sonido, (ANCHO_SONIDO, ALTO_SONIDO))

pos_x_sonido = 930
pos_y_sonido = 5

#FUENTE NOMBRE DEL JUGADOR
fuente_jugador = pygame.font.SysFont('consolas', 25, True)


#-----------------------PANTALLA JUEGO-----------------------#

#MUSICA
sonido_respuesta_correcta = pygame.mixer.Sound('Sonidos/respuesta_correcta.wav')
sonido_respuesta_incorrecta = pygame.mixer.Sound('Sonidos/respuesta_incorrecta.mp3')


imagen_fondo_juego = pygame.image.load('Imagenes/fondo_game.jpg')
imagen_fondo_juego = pygame.transform.scale(imagen_fondo_juego, (ANCHO_PANTALLA, ALTO_PANTALLA))

#VIDAS
ANCHO_VIDAS = 235
ALTO_VIDAS = 40
pos_x_vidas = 34
pos_y_vidas = 20

vidas_5 = pygame.image.load('Imagenes/Corazones/barra_de_vida_1.png')
vidas_5 = pygame.transform.scale(vidas_5, (ANCHO_VIDAS, ALTO_VIDAS))

vidas_4 = pygame.image.load('Imagenes/Corazones/barra_de_vida_2.png')
vidas_4 = pygame.transform.scale(vidas_4, (ANCHO_VIDAS, ALTO_VIDAS))

vidas_3 = pygame.image.load('Imagenes/Corazones/barra_de_vida_3.png')
vidas_3 = pygame.transform.scale(vidas_3, (ANCHO_VIDAS, ALTO_VIDAS))

vidas_2 = pygame.image.load('Imagenes/Corazones/barra_de_vida_4.png')
vidas_2 = pygame.transform.scale(vidas_2, (ANCHO_VIDAS, ALTO_VIDAS))

vidas_1 = pygame.image.load('Imagenes/Corazones/barra_de_vida_5.png')
vidas_1 = pygame.transform.scale(vidas_1, (ANCHO_VIDAS, ALTO_VIDAS))

#CUADRADO QUE CONTIENE LA MARCA A ADIVINAR
#(0,90,200,50)
ANCHO_CUADRADO_MARCA = 200 
ALTO_CUADRADO_MARCA = 50

pos_x_cuadrado_marca = 34
pos_y_cuadrado_marca = 90

pos_x_texto_marca = 45
pos_y_texto_marca = 103

#CUADRADO QUE CONTIENE EL RECORD PREVIO DEL JUGADOR
ANCHO_CUADRADO_RECORD = 200 
ALTO_CUADRADO_RECORD = 50

pos_x_cuadrado_record = 34
pos_y_cuadrado_record = 170

pos_x_texto_record = 45
pos_y_texto_record = 103



#CRONOMETRO
fuente_segundos = pygame.font.Font('Fuentes/gameplay_1987/GAMEPLAY-1987.ttf', 25)

ANCHO_CRONOMETRO = 45
ALTO_CRONOMETRO = 55
pos_x_cronometro = 850
pos_y_cronometro = 10

imagen_cronometro = pygame.image.load('Imagenes/cronometro.png')
imagen_cronometro = pygame.transform.scale(imagen_cronometro, (ANCHO_CRONOMETRO, ALTO_CRONOMETRO))

pos_x_segundos = 915
pos_y_segundos = 25

#MONEDA - PUNTOS
fuente_puntos = pygame.font.Font('Fuentes/gameplay_1987/GAMEPLAY-1987.ttf', 25)

ANCHO_MONEDA = 45
ALTO_MONEDA = 45
pos_x_moneda = 850
pos_y_moneda = 70

pos_x_puntos = 915
pos_y_puntos = 75

imagen_moneda = pygame.image.load('Imagenes/moneda.png')
imagen_moneda = pygame.transform.scale(imagen_moneda, (ANCHO_MONEDA, ALTO_MONEDA))


#PERSONAJE JUEGO
ANCHO_PERSONAJE = 100 
ALTO_PERSONAJE = 100
pos_x_personaje = 437
pos_y_personaje = 310

personaje = pygame.image.load('Imagenes/personaje.png')
personaje = pygame.transform.scale(personaje, (ANCHO_PERSONAJE, ALTO_PERSONAJE))


#CUADRADOS DE IMAGENES

matriz_dimensiones_cuadradados = [[(181,448)],
                                  [(350,448)],
                                  [(519,448)],
                                  [(684,448)]
                            ]



ANCHO_CUADRADO = 148
ALTO_CUADRADO = 147

# pos_x_cuadrado_1 = 183 
# pos_y_cuadrado_1 = 451

# pos_x_cuadrado_2 = 352 
# pos_y_cuadrado_2 = 451

# pos_x_cuadrado_3 = 521 
# pos_y_cuadrado_3 = 451

# pos_x_cuadrado_4 = 686 
# pos_y_cuadrado_4 = 451



#-----------------------PANTALLA RESULTADOS-----------------------#

ANCHO_IMAGEN_END = 250
ALTO_IMAGEN_END = 180
pos_x_imagen_end = 380
pos_y_imagen_end = 20

imagen_end = pygame.image.load('Imagenes/end.png')
imagen_end = pygame.transform.scale(imagen_end, (ANCHO_IMAGEN_END, ALTO_IMAGEN_END))

ANCHO_CUADRADO_RESULTADOS = 300
ALTO_CUADRADO_RESULTADOS = 340
pos_x_cuadrado_resultados = 357
pos_y_cuadrado_resultados = 240

mensaje_puntos = 'Puntos obtenidos'
pos_x_mensaje_puntos = 390
pos_y_mensaje_puntos = 278

pos_x_moneda_cuadrado_resultados = 450
pos_y_moneda_cuadrado_resultados = 310

pos_x_puntos_obtenidos = 510
pos_y_puntos_obtenidos = 318

#-----------------------------------------

mensaje_promedio = 'Promedio de tiempo'
pos_x_mensaje_promedio = 375
pos_y_mensaje_promedio = 374

pos_x_cronometro_cuadrado_resultados = 450
pos_y_cronometro_cuadrado_resultados = 415

pos_x_segundos_promedio = 510
pos_y_segundos_promedio = 430


#-----------------------------------------

ANCHO_BOTON_MENU = 274
ALTO_BOTON_MENU = 70

pos_x_boton_menu = 370
pos_y_boton_menu = 500

pos_x_texto_boton_menu = 385
pos_y_texto_boton_menu = 518