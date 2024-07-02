import pygame
import colores
from configuraciones import *
from especificas import * 


def crear_pantalla_principal(pantalla):
    """La funcion se encarga de crear lo que seria la pantalla principal del juego y mostrarla,
    estableciendo todo lo necesario en la misma como la musica, icono, creacion de ventana,
    etc, y ademas se encarga de manejar los eventos del mouse (para ver si clickeo en el
    boton de PLAY o en el del Sonido) y del teclado (para capturar el nombre que el
    jugador quiera ingresar a la hora de jugar, para borrar algun caracter con la tecla BACKSPACE,
    o para entrar al juego con la tecla RETURN)

    Args:
        pantalla: Recibe por parametro una pantalla (la cual representa una surface de la libreria Pygame)
        que representa que si es igual a None (el None aca funciona como una especie de bandera que sirve para
        hacer que se cree por primera vez la pantalla principal y que si no es igual a None, que no se vuelva a
        establecer la creacion de una ventana con set_mode())

    Returns:
        tuple: Retorna una tupla la cual tiene una surface (la pantalla), un str (el nombre del jugador),
        un int (el record previo del jugador) y por ultimo una lista de str (que representa las partidas
        cargadas)
    """
    sonido_inicio_fin.set_volume(0.1)
    sonido_inicio_fin.play(-1)

    if pantalla == None:
        pantalla = pygame.display.set_mode(DIMENSIONES)
        pygame.display.set_icon(icono)
        pygame.display.set_caption(titulo_juego)
    

    clock = pygame.time.Clock()

    texto_nombre = ''
    bandera_sonido = True
    ejecutar = True
    boton_clickeado = False

    while ejecutar:

        clock.tick(FPS)
            
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                ejecutar = False
    
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos_x_click = evento.pos[0]
                pos_y_click = evento.pos[1]

                if pos_x_click >= pos_x_boton_jugar and pos_x_click <= (pos_x_boton_jugar + ANCHO_BOTON_JUGAR) and pos_y_click >= pos_y_boton_jugar and pos_y_click <= (pos_y_boton_jugar + ALTO_BOTON_JUGAR):
                
                    boton_clickeado = True

                elif pos_x_click >= pos_x_sonido and pos_x_click <= (pos_x_sonido + ANCHO_SONIDO) and pos_y_click >= pos_y_sonido and pos_y_click <= (pos_y_sonido + ALTO_SONIDO):
            
                    if bandera_sonido:
                        bandera_sonido = False
                        sonido_inicio_fin.stop()
                        
                    else:
                        bandera_sonido = True
                        sonido_inicio_fin.play(-1)


            elif evento.type == pygame.TEXTINPUT:
                if boton_clickeado == True:
                    if len(texto_nombre) <= 6:
                        texto_nombre += evento.text

            elif evento.type == pygame.KEYDOWN:
                if boton_clickeado == True:
                    if evento.key == pygame.K_BACKSPACE:
                        longitud_texto = len(texto_nombre)
                        texto_nombre = texto_nombre[0:longitud_texto - 1]

                    elif evento.key == pygame.K_RETURN:

                        if texto_nombre.strip() == '':
                            sonido_respuesta_incorrecta.play()
                        else:
                            sonido_inicio_fin.stop()

                            datos_leidos_csv = leer_desde_csv(texto_nombre)
                            nombre_elegido = datos_leidos_csv[0]
                            record_previo = datos_leidos_csv[1]
                            partidas_cargadas = datos_leidos_csv[2]

                            return pantalla, nombre_elegido, record_previo, partidas_cargadas

                    
        dibujar_pegar_en_pantalla_principal(pantalla, boton_clickeado, bandera_sonido, texto_nombre)
      
        pygame.display.update()
    

#-------------------------------------------------------------------------------------

def crear_pantalla_juego(pantalla, path_archivo_json: str, lista_marcas_aleatorias: list, record_previo: int):
    """La funcion se encarga de crear lo que seria la pantalla del juego y mostrarla, ademas
    de que se encarga de manejar los eventos mas importantes del juego que son el realizar
    click en alguno de los 4 cuadrantes donde se encuentran las imagenes, manejar el tema de las
    vidas si se equivoca, reiniciar el cronometro cada que adivina o se le acaba el tiempo, el
    tema de las monedas que aumenten o resten, el cambio de imagenes, etc.

    Args:
        pantalla: Recibe por parametro una pantalla (la cual representa una surface de la libreria Pygame),
        y en este caso la pantalla pasada por parametro es la pantalla principal, haciendo como la animacion
        de que pasa de la pantalla principal a la del juego sin crear otra ventana con set_mode().

        path_archivo_json (str): Recibe por parametro una ruta de tipo str la cual representa
        la ubicacion donde se encuentra el archivo JSON que contiene los paths de todas la marcas.

        lista_marcas_aleatorias (list): Recibe por parametro una lista de strings con las 15
        marcas del archivo JSON pero de manera random/aleatoria y mezcladas.

        record_previo (int): Recibe por parametro un numero de tipo int que representa el record
        previo del jugador (si es que lo tiene).

    Returns:
        tuple: Retorna una tupla la cual contiene una surface (la pantalla de juego), un int (que
        representa la cantidad de puntos que obtuvo en la partida) y un int/float (que representa
        el promedio de tiempo que tardo en adivinar todas las marcas (o no).) 
    """
    #SONIDOS
    sonido_respuesta_correcta.set_volume(0.5)
    sonido_respuesta_incorrecta.set_volume(0.5)

    #CLOCK PARA FPS
    clock = pygame.time.Clock()

    #INICIALIZACION DE VARIABLES DEL TIEMPO PARA EL CRONOMETRO
    tiempo_total = 30000
    tiempo_inicial = pygame.time.get_ticks() #TIEMPO QUE TARDA EN DARLE AL BOTON PLAY DESDE QUE SE EJECUTA PYGAME.INIT()
    cronometro_detener = False

    #INICIALIZACION DE BANDERA PARA SABER SI FINALIZO EL JUEGO O NO Y DE VIDAS
    vidas = 5
    finalizar = False

    #INICIALIZACION DE ACUMULADORES (para el tiempo promedio y para los puntos obtenidos) 
    acumulador_puntos = 0
    tiempo_de_respuesta = 0
    
    #LLAMAMOS A LA FUNCION QUE OBTIENE LAS RESPUESTAS CORRECTAS DEL JSON Y LAS GUARDA EN UNA LISTA
    respuestas_correctas = obtener_respuestas_correctas('logos.json')


    with open(path_archivo_json, 'r') as archivo:
        dato = json.load(archivo)
    
    k = 0
    lista = dato.get(lista_marcas_aleatorias[k])


    ejecutar = True
    while ejecutar:

        clock.tick(FPS)

        pegar_imagenes_fijas_pantalla_juego(pantalla)

        dibujar_cuadrado_marca_a_adivinar_y_record_previo(pantalla, lista_marcas_aleatorias, k, record_previo)

        pegar_logos_en_cuadrantes(pantalla, lista, matriz_dimensiones_cuadrados)
        
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                ejecutar = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos_x_click = evento.pos[0]
                pos_y_click = evento.pos[1]
               
                validacion = validar_click_en_cuadrantes(matriz_dimensiones_cuadrados, pos_x_click, pos_y_click, lista, respuestas_correctas)

                validacion_click = validacion[0]
                contador_correctas = validacion[1]

                if validacion_click == True:
                    if contador_correctas > 0:
                        sonido_respuesta_correcta.play()
                        acumulador_puntos += 20
                        tiempo_de_respuesta += tiempo_transcurrido
                        cronometro_detener = True
                        tiempo_transcurrido = 0 #REINICIO EL TIEMPO TRANSCURRIDO
                        k += 1

                        #PARA QUE NO HAYAN ERRORES DE LIST INDEX OUT OF RANGE (SE EXCEDE DE RANGO)
                        if k < len(lista_marcas_aleatorias):
                            lista = dato.get(lista_marcas_aleatorias[k])
                        tiempo_inicial = pygame.time.get_ticks()#REINICIA EL CRONOMETRO Y EMPIEZA A CONTAR DE
                                                                #NUEVO A PARTIR DE ESE TIEMPO INICIAL
                        
                    else:
                        vidas -= 1
                        sonido_respuesta_incorrecta.play()
                        acumulador_puntos -= 10
                        tiempo_de_respuesta += tiempo_transcurrido
                        cronometro_detener = True
                        tiempo_transcurrido = 0 #REINICIO EL TIEMPO TRANSCURRIDO
                        k += 1

                        #PARA QUE NO HAYAN ERRORES DE LIST INDEX OUT OF RANGE (SE EXCEDE DE RANGO)
                        if k < len(lista_marcas_aleatorias):
                            lista = dato.get(lista_marcas_aleatorias[k])
                        tiempo_inicial = pygame.time.get_ticks()#REINICIA EL CRONOMETRO Y EMPIEZA A CONTAR DE
                                                                #NUEVO A PARTIR DE ESE TIEMPO INICIAL
                
                    #HACE QUE NO ESTE PARADO EL CRONOMETRO DE NUEVO - VUELVE A INICIARLO
                    cronometro_detener = False
                      
        #LOGICA PUNTOS
        acumulador_puntos = actualizar_puntos(pantalla, acumulador_puntos)

        #LOGICA CRONOMETRO
    
        if cronometro_detener == False:
            tiempo_actual = pygame.time.get_ticks() #EMPIEZA A CONTAR A PARTIR DEL TIEMPO INICIAL
            tiempo_transcurrido = tiempo_actual - tiempo_inicial
            tiempo_final = ((tiempo_total - tiempo_transcurrido)* 0.001)
            
            if tiempo_final < 0:
                tiempo_final = 0
                cronometro_detener = True
                tiempo_inicial = pygame.time.get_ticks()
                vidas -= 1
                k += 1
                sonido_respuesta_incorrecta.play()
            
                #PARA QUE NO HAYAN ERRORES DE LIST INDEX OUT OF RANGE
                if k < len(lista_marcas_aleatorias):
                    lista = dato.get(lista_marcas_aleatorias[k])
            
            cronometro_detener = False

            tiempo_final = (f'{tiempo_final:.00f}')
            texto_segundos = fuente_segundos.render(tiempo_final, False, colores.BLANCO)
            pantalla.blit(texto_segundos, (pos_x_segundos, pos_y_segundos))
       

        match vidas:
            case 4:
                pantalla.blit(vidas_4, (pos_x_vidas, pos_y_vidas))
            case 3:
                pantalla.blit(vidas_3, (pos_x_vidas, pos_y_vidas))
            case 2:
                pantalla.blit(vidas_2, (pos_x_vidas, pos_y_vidas))
            case 1:
                pantalla.blit(vidas_1, (pos_x_vidas, pos_y_vidas))  
            case 0:
                #SE QUEDA SIN VIDAS
                finalizar = True
                
                #SACAMOS PROMEDIO DE TIEMPO DE RESPUESTA DE TODAS LAS PREGUNTAS
                promedio_tiempo_respuestas = realizar_promedio_tiempo_respuesta(tiempo_de_respuesta, k)


        if k == len(lista_marcas_aleatorias):
            finalizar = True
            promedio_tiempo_respuestas = realizar_promedio_tiempo_respuesta(tiempo_de_respuesta, k)

        if finalizar == True:
            return pantalla, acumulador_puntos, promedio_tiempo_respuestas

        pygame.display.update()
    
 
#--------------------------------------------------------------------------------------

def crear_pantalla_resultados(pantalla, puntos_obtenidos: int, promedio_tiempo: int|float):
    """La funcion se encarga de crear lo que seria la pantalla de resultados y mostrarla,
    ademas de que se encarga de manejar los eventos del mouse para detectar si el jugador
    le dio click en el boton de "Volver al menu" o si le dio click al sonido para detenerlo
    o encenderlo nuevamente.

    Args:
        pantalla: Recibe por parametro una pantalla (la cual representa una surface de la libreria Pygame),
        y en este caso la pantalla pasada por parametro es la pantalla del juego, haciendo como la animacion
        de que pasa de la pantalla del juego a la final donde se muestran los datos finales de la partida,
        como la cantidad de puntos, promedio de tiempo de respuesta de todas las marcas, etc, 
        sin crear otra ventana con set_mode().

        puntos_obtenidos (int): Recibe por parametro un numero de tipo int que representa la cantidad
        de puntos obtenidos que obtuvo el jugador en una partida.

        promedio_tiempo (int | float): Recibe por parametro un numero de tipo int|float que representa
        el promedio de tiempo en que adivino todas (o no) las marcas.

    Returns:
        tuple: Retorna una tupla la cual contiene una bandera (que puede ser True or False, dependiendo si
        el usuario le da click o no en el boton de "Volver al menu") y una surface (que representa la pantalla
        de resultados/final)
    """
    sonido_inicio_fin.set_volume(0.1)
    sonido_inicio_fin.play(-1)

    clock = pygame.time.Clock()
    volver_a_jugar = False
    bandera_sonido = True
    retorno = ''

    ejecutar = True
    while ejecutar:

        clock.tick(FPS)

        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                ejecutar = False
            
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos_x = evento.pos[0]
                pos_y = evento.pos[1]

                if pos_x >= pos_x_boton_menu and pos_x <= (ANCHO_BOTON_MENU + pos_x_boton_menu)\
                and pos_y > pos_y_boton_menu and pos_y <= (ALTO_BOTON_MENU + pos_y_boton_menu):
                    volver_a_jugar = True
                    ejecutar = False #Cambio la bandera ejecutar a FALSE para salir del bucle WHILE
                    retorno = volver_a_jugar, pantalla
                    break #Rompo y salgo de bucle FOR que recorre los eventos
                
                elif pos_x >= pos_x_sonido and pos_x <= (pos_x_sonido + ANCHO_SONIDO) and pos_y >= pos_y_sonido and pos_y <= (pos_y_sonido + ALTO_SONIDO):
            
                    if bandera_sonido:
                        bandera_sonido = False
                        sonido_inicio_fin.stop()
                        
                    else:
                        bandera_sonido = True
                        sonido_inicio_fin.play(-1)
        

        dibujar_pegar_en_pantalla_final(pantalla, bandera_sonido, puntos_obtenidos, promedio_tiempo)
    
        pygame.display.update()

    
    if volver_a_jugar == False:
        retorno = volver_a_jugar
        
    return retorno
        
    