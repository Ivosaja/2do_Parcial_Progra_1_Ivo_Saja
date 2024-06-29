import pygame
import colores
from configuraciones import *
from especificas import * 

lista_jugadores = []

def crear_pantalla_principal(pantalla):

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
                        sonido_inicio_fin.stop()

                        with open('jugadores.csv', 'r') as archivo:
                            lineas_csv = archivo.readlines()

                        record_previo = 0

                        for i in range(1, len(lineas_csv)):
                            datos_previos = lineas_csv[i]
                            separacion = datos_previos.split(',')
                            nombre_jugador = separacion[0]
                
                            if nombre_jugador == texto_nombre:
                                record_previo = separacion[1]
                                record_previo = record_previo.replace('\n', '')
                                record_previo = int(record_previo)
                                break
                        
   
                        return pantalla, texto_nombre, record_previo
                    
                    
        dibujar_pegar_en_pantalla_principal(pantalla, boton_clickeado, bandera_sonido, texto_nombre)
      
        pygame.display.update()
    


#-------------------------------------------------------------------------------------

def crear_pantalla_juego(pantalla, path_archivo_json: str, texto_nombre: str, record_previo: int):


    sonido_respuesta_correcta.set_volume(0.5)
    sonido_respuesta_incorrecta.set_volume(0.5)

    clock = pygame.time.Clock()

    tiempo_total = 30000
    tiempo_inicial = pygame.time.get_ticks()

    cronometro_detener = False
    finalizar = False
    acumulador_puntos = 0
    vidas = 5
    tiempo_de_respuesta = 0


    key_aleatoria = cargar_marcas_random_sin_repetir('logos.json')
    respuestas_correctas = obtener_respuestas_correctas('logos.json')
    print(key_aleatoria)

    with open(path_archivo_json, 'r') as archivo:
        dato = json.load(archivo)
    
    k = 0
    lista = dato.get(key_aleatoria[k])


    ejecutar = True
    while ejecutar:
       
        #PEGAMOS FONDO DE LA PANTALLA JUEGO
        pantalla.blit(imagen_fondo_juego, (0,0))

        #PEGAMOS VIDAS
        pantalla.blit(vidas_5, (pos_x_vidas, pos_y_vidas))
        
        #PEGAMOS CRONOMETRO Y MONEDA
        pantalla.blit(imagen_cronometro, (pos_x_cronometro, pos_y_cronometro))
        pantalla.blit(imagen_moneda, (pos_x_moneda, pos_y_moneda))
        pantalla.blit(personaje, (pos_x_personaje, pos_y_personaje))

        #DIBUJAMOS CUADRADADO QUE CONTIENE LA MARCA A ADIVINAR

        pygame.draw.rect(pantalla, colores.AZUL_OSCURO, (pos_x_cuadrado_marca, pos_y_cuadrado_marca, ANCHO_CUADRADO_MARCA, ALTO_CUADRADO_MARCA))
        pygame.draw.rect(pantalla, colores.BLANCO, (pos_x_cuadrado_marca, pos_y_cuadrado_marca, ANCHO_CUADRADO_MARCA, ALTO_CUADRADO_MARCA), 5)

        marca_renderizada = fuente_jugador.render(key_aleatoria[k], False, colores.BLANCO, colores.AZUL_OSCURO)
        pantalla.blit(marca_renderizada, (pos_x_texto_marca, pos_y_texto_marca))

        #DIBUJAMOS RECORD PREVIO DEL JUGADOR 
        pygame.draw.rect(pantalla, colores.AZUL_OSCURO, (pos_x_cuadrado_record, pos_y_cuadrado_record, ANCHO_CUADRADO_RECORD, ALTO_CUADRADO_RECORD))
        pygame.draw.rect(pantalla, colores.BLANCO, (pos_x_cuadrado_record, pos_y_cuadrado_record, ANCHO_CUADRADO_RECORD, ALTO_CUADRADO_RECORD), 5)

        #record_texto = fuente_jugador.render(key_aleatoria[k], False, colores.BLANCO, colores.AZUL_OSCURO)


        clock.tick(FPS)

        #PEGAMOS IMAGENES EN CADA CUADRANTE
        for i in range(len(matriz_dimensiones_cuadradados)):
            for j in range(len(matriz_dimensiones_cuadradados[i])):
            
                #ACCEDO A LAS TUPLAS DE LA MATRIZ
                variable = matriz_dimensiones_cuadradados[i][j]
                pos_x_cuadrado = variable[0]
                pos_y_cuadrado = variable[1]
                
                path = lista[i]
                imagen_logo = pygame.image.load(path)
                imagen_logo = pygame.transform.scale(imagen_logo, (ANCHO_CUADRADO, ALTO_CUADRADO))
                pantalla.blit(imagen_logo, (pos_x_cuadrado, pos_y_cuadrado))


        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            #print(evento)
            if evento.type == pygame.QUIT:
                ejecutar = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos_x_click = evento.pos[0]
                pos_y_click = evento.pos[1]
                contador_correctas = 0
                click_valido = False

                #RECORREMOS LA MATRIZ NUEVAMENTE Y CHEQUEAMOS SI DIO CLICK EN ALGUNO DE LOS 4
                #CUADRANTES
                for i in range(len(matriz_dimensiones_cuadradados)):
                    for j in range(len(matriz_dimensiones_cuadradados[i])):
                        variable = matriz_dimensiones_cuadradados[i][j]
                        pos_x_cuadrado = variable[0]
                        pos_y_cuadrado = variable[1]
                        
                        if pos_x_click >= pos_x_cuadrado and pos_x_click <= (pos_x_cuadrado + ANCHO_CUADRADO) and pos_y_click >= pos_y_cuadrado and pos_y_click <= (pos_y_cuadrado + ALTO_CUADRADO):
                            
                            click_valido = True
                            if lista[i] in respuestas_correctas:                            
                                contador_correctas += 1

                if click_valido == True:
                    if contador_correctas > 0:
                        sonido_respuesta_correcta.play()
                        acumulador_puntos += 20
                        tiempo_de_respuesta += tiempo_transcurrido
                        print(f'Tardaste {tiempo_transcurrido} segundos')
                        cronometro_detener = True
                        tiempo_transcurrido = 0 #REINICIO EL TIEMPO TRANSCURRIDO
                        pygame.time.delay(1000)
                        k += 1

                        #PARA QUE NO HAYAN ERRORES DE LIST INDEX OUT OF RANGE
                        if k < len(key_aleatoria):
                            lista = dato.get(key_aleatoria[k])
                        tiempo_inicial = pygame.time.get_ticks() #REINICIA EL CRONOMETRO
                        #print(lista)
                        
                    else:
                        vidas -= 1
                        sonido_respuesta_incorrecta.play()
                        acumulador_puntos -= 10
                        tiempo_de_respuesta += tiempo_transcurrido
                        print(f'Tardaste {tiempo_transcurrido} segundos')
                        cronometro_detener = True
                        tiempo_transcurrido = 0 #REINICIO EL TIEMPO TRANSCURRIDO
                        pygame.time.delay(1000)
                        k += 1

                        #PARA QUE NO HAYAN ERRORES DE LIST INDEX OUT OF RANGE
                        if k < len(key_aleatoria):
                            lista = dato.get(key_aleatoria[k])
                        tiempo_inicial = pygame.time.get_ticks() #REINICIA EL CRONOMETRO
                        #print(lista)
                
                #contador_correctas = 0
                #HACE QUE NO ESTE PARADO EL CRONOMETRO DE NUEVO
                cronometro_detener = False
                      
                
        #LOGICA PUNTOS - FUNCION
        
        if acumulador_puntos < 0:
            acumulador_puntos = 0
        
        texto_puntos = fuente_puntos.render(f'{acumulador_puntos}', False, colores.AMARILLO_BRILLANTE)
        pantalla.blit(texto_puntos, (pos_x_puntos, pos_y_puntos))


        #LOGICA CRONOMETRO - FUNCION
    
        if cronometro_detener == False:
            tiempo_actual = pygame.time.get_ticks()
            tiempo_transcurrido = tiempo_actual - tiempo_inicial
            tiempo_final = ((tiempo_total - tiempo_transcurrido)* 0.001)
            
            if tiempo_final < 0:
                tiempo_final = 0
                cronometro_detener = True
                tiempo_inicial = pygame.time.get_ticks()
                vidas -= 1
                k += 1
                #PARA QUE NO HAYAN ERRORES DE LIST INDEX OUT OF RANGE
                if k < len(key_aleatoria):
                    lista = dato.get(key_aleatoria[k])
                #tiempo_inicial = pygame.time.get_ticks()
            
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
                tiempo_de_respuesta = (tiempo_de_respuesta * 0.001)
                promedio_tiempo_respuestas = tiempo_de_respuesta / k
  
  
        pantalla.blit(texto_segundos, (pos_x_segundos, pos_y_segundos))

        if k == len(key_aleatoria):
            finalizar = True
            tiempo_de_respuesta = (tiempo_de_respuesta * 0.001)
            promedio_tiempo_respuestas = tiempo_de_respuesta / k

        if finalizar == True:
            
            jugador = {
                'Nombre': texto_nombre,
                'Record de monedas previo': acumulador_puntos
            }

            record_actual = jugador['Record de monedas previo']


            if record_actual > record_previo:
                jugador['Record de monedas previo'] = record_actual
                lista_jugadores.append(jugador)

            print('Hola mundo')

            #print(lista_jugadores)

            return pantalla, acumulador_puntos, promedio_tiempo_respuestas, lista_jugadores

        pygame.display.update()
    
 
#--------------------------------------------------------------------------------------

def crear_pantalla_resultados(pantalla, puntos_obtenidos: int, promedio_tiempo: int|float):
    

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
        
    