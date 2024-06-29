#-----------------------FUNCIONES ESPECIFICAS-----------------------#
import pygame
import json
import random
from configuraciones import *


def dibujar_pegar_en_pantalla_principal(pantalla, boton_clickeado: bool, bandera_sonido: bool, texto_nombre: str)-> None:
    
    #PEGAMOS FONDO DE PANTALLA PRINCIPAL Y TITULO - FUNCION
    pantalla.blit(imagen_fondo, (0,0))
    pantalla.blit(titulo_imagen, (pos_x_titulo, pos_y_titulo))

    #DIBUJAMOS BOTONES DE JUGAR Y DE SONIDO
    pygame.draw.rect(pantalla, colores.CELESTE, (pos_x_boton_jugar, pos_y_boton_jugar, ANCHO_BOTON_JUGAR, ALTO_BOTON_JUGAR), 0, 10)

    pygame.draw.rect(pantalla, colores.AZUL_OSCURO, (pos_x_boton_jugar, pos_y_boton_jugar, ANCHO_BOTON_JUGAR, ALTO_BOTON_JUGAR), 5, 10)
    
    #PEGAMOS TEXTO 'PLAY' DEL BOTON JUGAR
    pantalla.blit(texto_play, (pos_x_texto, pos_y_texto))

    if boton_clickeado == True:
        
        #DIBUJAMOS RECTANGULO BLANCO SOBRE EL CUAL SE ESCRIBE EL NOMBRE DE USUARIO
        pygame.draw.rect(pantalla, colores.BLANCO, (pos_x_boton_jugar, pos_y_boton_jugar, ANCHO_BOTON_JUGAR, ALTO_BOTON_JUGAR), 0, 10)

        #DIBUJAMOS RECTANGULO CON BORDE Y SE PONE ENCIMA DEL BLANCO
        pygame.draw.rect(pantalla, colores.AZUL_OSCURO, (pos_x_boton_jugar, pos_y_boton_jugar, ANCHO_BOTON_JUGAR, ALTO_BOTON_JUGAR), 5, 10)

        texto = fuente_jugador.render(texto_nombre, False, colores.NEGRO, colores.BLANCO)
        pantalla.blit(texto, (pos_x_boton_jugar + 9, pos_y_boton_jugar + 10))
    
    if bandera_sonido == True:
        #PEGAMOS IMAGEN DEL SONIDO
        pantalla.blit(imagen_sonido, (pos_x_sonido, pos_y_sonido))
    
    else:
        #PEGAMOS IMAGEN DEL SONIDO
        pantalla.blit(imagen_sin_sonido, (pos_x_sonido, pos_y_sonido))


def dibujar_pegar_en_pantalla_final(pantalla, bandera_sonido: bool, puntos_obtenidos: int, promedio_tiempo: int)-> None:
    
    #PEGAMOS FONDO DE LA PANTALLA DE RESULTADOS
    pantalla.blit(imagen_fondo, (0,0))

    pantalla.blit(imagen_end, (pos_x_imagen_end, pos_y_imagen_end))
    
    #DIBUJAMOS CUADRADO DE RESULTADOS DE LA PARTIDA
    pygame.draw.rect(pantalla, colores.AZUL_OSCURO, (pos_x_cuadrado_resultados, pos_y_cuadrado_resultados, ANCHO_CUADRADO_RESULTADOS, ALTO_CUADRADO_RESULTADOS), 0, 10)
    
    #DIBUJAMOS CUADRADO DE RESULTADOS DE LA PARTIDA
    pygame.draw.rect(pantalla, colores.BLANCO, (pos_x_cuadrado_resultados, pos_y_cuadrado_resultados, ANCHO_CUADRADO_RESULTADOS, ALTO_CUADRADO_RESULTADOS), 5, 10)

    #PEGAMOS MONEDA Y CRONOMETRO
    pantalla.blit(imagen_moneda, (pos_x_moneda_cuadrado_resultados, pos_y_moneda_cuadrado_resultados))
    texto_puntos = fuente_play.render(f'{puntos_obtenidos}', False, colores.BLANCO)
    pantalla.blit(texto_puntos, (pos_x_puntos_obtenidos, pos_y_puntos_obtenidos))

    pantalla.blit(imagen_cronometro, (pos_x_cronometro_cuadrado_resultados, pos_y_cronometro_cuadrado_resultados))
    texto_tiempo_promedio = fuente_play.render(f'{promedio_tiempo:.2f}', False, colores.BLANCO)
    pantalla.blit(texto_tiempo_promedio, (pos_x_segundos_promedio, pos_y_segundos_promedio))

    #PEGAMOS TEXTOS
    texto_puntos_obtenidos_mensaje = fuente_jugador.render(mensaje_puntos, False, colores.BLANCO, colores.AZUL_OSCURO)
    pantalla.blit(texto_puntos_obtenidos_mensaje, (pos_x_mensaje_puntos, pos_y_mensaje_puntos))
    
    texto_promedio_tiempo_mensaje = fuente_jugador.render(mensaje_promedio, False, colores.BLANCO, colores.AZUL_OSCURO)
    pantalla.blit(texto_promedio_tiempo_mensaje, (pos_x_mensaje_promedio, pos_y_mensaje_promedio))

    #BOTON VOLVER AL MENU
    pygame.draw.rect(pantalla, colores.CELESTE, (pos_x_boton_menu, pos_y_boton_menu, ANCHO_BOTON_MENU, ALTO_BOTON_MENU), 0, 10)
    pygame.draw.rect(pantalla, colores.AZUL_OSCURO, (pos_x_boton_menu, pos_y_boton_menu, ANCHO_BOTON_MENU, ALTO_BOTON_MENU), 5, 10)

    texto_volver_al_menu = fuente_play.render('VOLVER AL MENU', False, colores.BLANCO)
    pantalla.blit(texto_volver_al_menu, (pos_x_texto_boton_menu, pos_y_texto_boton_menu))



    if bandera_sonido == True:
        #PEGAMOS IMAGEN DEL SONIDO
        pantalla.blit(imagen_sonido, (pos_x_sonido, pos_y_sonido))
    
    else:
        #PEGAMOS IMAGEN DEL SONIDO
        pantalla.blit(imagen_sin_sonido, (pos_x_sonido, pos_y_sonido))




def pegar_logos_en_cuadrantes_pantalla_juego():
    pass



def validar_ingreso_nombre_jugador(nombre_jugador: str)-> str:
    pass
#     #validar que no ingrese un nombre que ya existe en el csv
#     #validar que no sea un nombre vacio ('')
#     sonido_respuesta_incorrecta.set_volume(0.4)
#     while nombre_jugador == '' or len(nombre_jugador) >= 6:
#         sonido_respuesta_incorrecta.play()
    
#     return nombre_jugador



def cargar_jugadores_csv(path_jugadores_csv: str):
    
    lista_jugadores = []

    with open(path_jugadores_csv, 'r') as archivo:
        lineas = archivo.read()
    
    for i in range(1, len(lineas)):
        datos = lineas[i]

        nombre_jugador = datos






def cargar_marcas_random_sin_repetir(path_archivo_json: str)-> list:
    with open(path_archivo_json, 'r') as archivo:
        marcas = json.load(archivo)

    set_paths_sin_repetir = set()

    lista_keys_json = list(marcas.keys())
    longitud_lista_keys = len(lista_keys_json)
    
    while True:
        numero_random_key = random.randint(0, longitud_lista_keys-1)
        key_logo = lista_keys_json[numero_random_key]
        set_paths_sin_repetir.add(key_logo)
        
        if len(set_paths_sin_repetir) == 15:
            return list(set_paths_sin_repetir)


def obtener_respuestas_correctas(path_archivo_json: str)-> list:
    
    lista_paths = []
    lista = []
    
    with open(path_archivo_json, 'r') as archivo:
        paths = json.load(archivo)

    lista.append(paths)

    for dato in paths:
        for path in paths[dato]:
            #RECORRO LOS PATHS DE CADA KEY
            lista_paths.append(path)
    
    
    #Creamos unas lista con los paths de las imagenes correctas

    lista_paths_correctas = list(filter(lambda path: '_correcta.png' in path or '_correcta.jpg' in path, lista_paths)) #Verifica si ese fragmento del path esta en cada uno de los paths
    
    return lista_paths_correctas

