#-----------------------FUNCIONES ESPECIFICAS-----------------------#
import pygame
import json
import random
from configuraciones import *

#---------------FUNCIONES PARA PANTALLA PRINCIPAL---------------#

def dibujar_pegar_en_pantalla_principal(pantalla, boton_clickeado: bool, bandera_sonido: bool, texto_nombre: str)-> None:
    
    """La funcion se encarga de dibujar y de pegar en la pantalla principal todos los elementos
    que la misma utiliza

    Args:
        pantalla: Recibe por parametro una pantalla (la cual representa una surface de la libreria Pygame)

        boton_clickeado (bool): Recibe por parametro una bandera de tipo bool que representa si el
        jugador clickeo en el boton de jugar (play)

        bandera_sonido (bool): Recibe por parametro una bandera de tipo bool que representa 
        si el usuario clickeo el boton de sonido para apagarlo o prenderlo

        texto_nombre (str): Recibe por parametro un texto de tipo str el cual representa
        el nombre que el jugador ingresa en el boton de PLAY, el cual es renderizado y bliteado en pantalla

    Returns:
        No retorna nada, solo se encarga de dibujar y pegar en pantalla los elementos fijos
    """

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


def leer_desde_csv(texto_nombre: str):
    """La funcion se encarga de leer lo que se encuentra en el archivo.csv
    y se va guardando en una lista de str, cada una de las partidas, y en caso
    que ya exista una persona con el nombre que escribio, no la va a crear, 
    sino que se guardara el record previo y lo retornara. Caso contrario lo agrega
    a la lista con el nombre elegido por el usuario y record previo en 0.

    Args:
        texto_nombre (str): Recibe por parametro un nombre de tipo str el cual
        representa el nombre que el usuario ingreso por el boton.

    Returns:
        tuple: Retorna una tupla la cual contiene un str (el nombre que ingreso el usuario),
        un int (el cual es el record previo) y una lista de str (que representa la lista con
        las partidas cargadas)
    """
    with open('jugadores.csv', 'r') as archivo:
        lista_lineas_csv = archivo.readlines()
    
    partidas_cargadas = []
    bandera_nueva_partida = True

    for i in range(1, len(lista_lineas_csv)):
        partida = lista_lineas_csv[i]

        if partida != '':
            caracteristicas_partida = partida.split(',')
            nombre_jugador = caracteristicas_partida[0]

            if nombre_jugador == texto_nombre:
                nombre_elegido = texto_nombre
                record_previo = caracteristicas_partida[1]
                record_previo = record_previo.replace('\n', '')
                record_previo = int(record_previo)
                bandera_nueva_partida = False
                partidas_cargadas.append(f'{nombre_elegido},{record_previo}\n')
            
            else:
                partidas_cargadas.append(partida)
    
    if bandera_nueva_partida == True:
        nombre_elegido = texto_nombre
        record_previo = 0
    
    return nombre_elegido, record_previo, partidas_cargadas


def guardar_datos_en_csv(nombre_jugador: str, record_previo: int, partidas_cargadas: list)-> None:
    """La funcion  permite almacenar al jugador nuevo o ya ingresado
    (se usa un for que recorre y verifica cual es el caso) y luego se abre 
    el archivo csv para almacenar la nueva lista de partidas + la cabecera, funciona como
    una especie de actualizacion de los datos en el csv.

    Args:
        nombre_jugador (str): Recibe por parametro el nombre del jugador de la partida (str)

        record_previo (int): Recibe por parametro un numero de tipo int que representa el record 
        de puntaje que llego esa partida

        partidas_cargadas (list): Recibe por parametro una lista de strings, la cual almacena todas
        las partidas que hay en el csv.
    
    Returns:
        No retorna nada, solo se encarga de sobreescribir en el archivo.csv la lista con los jugadores
        cargados de manera ordenada.
    """
    lista_partidas_ordenadas = []
    jugador_ya_existente = False

    for i in range(len(partidas_cargadas)):
        
        partida = partidas_cargadas[i]
        separacion_partida = partida.split(',')

        if nombre_jugador == separacion_partida[0]:
            lista_partidas_ordenadas.append(f'{nombre_jugador},{record_previo}\n')
            jugador_ya_existente = True
        
        else:
            lista_partidas_ordenadas.append(partida)
    
    if jugador_ya_existente == False:
        lista_partidas_ordenadas.append(f'{nombre_jugador},{record_previo}\n')

    with open('jugadores.csv', 'w') as archivo:
        archivo.write('Nombre,Record de monedas\n')

        for partida in lista_partidas_ordenadas:
            archivo.write(partida)        



#---------------FUNCIONES PARA PANTALLA JUEGO---------------#


def cargar_marcas_random_sin_repetir(path_archivo_json: str)-> list:
    
    """La funcion se encarga de generar una lista de marcas aleatorias leidas del JSON con una funcion
    de la libreria importada Random

    Args:
        path_archivo_json (str): Recibe por parametro una ruta de tipo str donde se encuentra el path
        del archivo JSON el cual va a ser leido para extraer todas las keys del mismo.
    
    Returns:
        list: Retorna una lista de str cargada con marcas aleatorias y desordenadas.
    """

    with open(path_archivo_json, 'r') as archivo:
        marcas = json.load(archivo)

    #set_paths_sin_repetir = set()
    lista_keys_json = list(marcas.keys())
    longitud_lista_keys = len(lista_keys_json)

    lista_marcas_desordenadas = random.sample(lista_keys_json, longitud_lista_keys)

    #El random.sample recibe como 1er parametro una lista (yo le paso la lista de todas las keys del JSON)
    #y como segundo parametro la cantidad de elementos randoms que va a sacar de esa lista (yo le paso el len
    #de mi lista de keys)

    return lista_marcas_desordenadas

    # while True:
    #     numero_random_key = random.randint(0, longitud_lista_keys-1)
    #     key_logo = lista_keys_json[numero_random_key]
    #     set_paths_sin_repetir.add(key_logo)
        
    #     if len(set_paths_sin_repetir) == 15:
    #         lista_sin_repetir = list(set_paths_sin_repetir)
    #         return lista_sin_repetir


def obtener_respuestas_correctas(path_archivo_json: str)-> list:
    
    """La funcion se encarga de generar una lista con todas las imagenes correctas
    que contiene el archivo JSON

    Args:
        path_archivo_json (str): Recibe por parametro una ruta de tipo str donde
        se encuentra guardado el archivo JSON que va a ser leido

    Returns:
        list: Retorna una lista de str con todos los paths de las imagenes correctas
        en mi JSON.
    """

    lista_paths = []
    
    with open(path_archivo_json, 'r') as archivo:
        paths = json.load(archivo)


    for dato in paths:
        for path in paths[dato]:
            #RECORRO LOS PATHS DE CADA KEY
            lista_paths.append(path)
    
    #Creamos unas lista con los paths de las imagenes correctas

    lista_paths_correctas = list(filter(lambda path: '_correcta.png' in path or '_correcta.jpg' in path, lista_paths)) #Verifica si ese fragmento del path esta en cada uno de los paths, pasandole la lista de paths como parametro
    
    return lista_paths_correctas


def realizar_promedio_tiempo_respuesta(tiempo_respuesta_acumulado: int, marcas_adivinadas: int)-> int|float:
    """La funcion se encarga de realizar el calculo para sacar el promedio de tiempo
    en que el usuario adivino todas las marcas (o N cantidad de marcas si es
    que se le acabaron las vidas)

    Args:
        tiempo_respuesta_acumulado (int): Recibe por parametro un numero de tipo int
        que representa el tiempo acumulado en milisegundos en que el usuario adivino
        todas las marcas (o N cantidad de marcas si es que se le acabaron las vidas)

        marcas_adivinadas (int): Recibe por parametro un numero de tipo int que
        representa la cantidad de marcas que el usuario adivino.

    Returns:
        int|float: Retorna un numero de tipo int o float que representa el promedio
        calculado.
    """
    tiempo_respuesta_acumulado = (tiempo_respuesta_acumulado * 0.001)
    promedio = tiempo_respuesta_acumulado / marcas_adivinadas

    return promedio


def pegar_logos_en_cuadrantes(pantalla, lista: list, matriz_dimensiones_cuadrados: list)-> None:
    """La funcion se encarga de ir recorriendo la matriz donde estan guardadas
    las posiciones (X,Y) de cada uno de los cuadrados e ir pegandolas a medida que
    va marca por marca de la lista de marcas random que se genero previamente.
     

    Args:
        pantalla: Recibe por parametro una pantalla (la cual representa una surface de la libreria Pygame)

        lista (list): Recibe por parametro una lista de str la cual contiene los paths de las imagenes
        de la marca random que va tomando indice tras indice.

        matriz_dimensiones_cuadrados (list): Recibe por parametro una matriz de tipo list
        (array bidimensional) que contiene todas las posiciones (X,Y) de cada uno de los cuadrados

    Returns:
        No retorna nada, solo va pegando las imagenes en cada cuadrante
    """
    #PEGAMOS IMAGENES EN CADA CUADRANTE
    for i in range(len(matriz_dimensiones_cuadrados)):
        for j in range(len(matriz_dimensiones_cuadrados[i])):
        
            #ACCEDO A LAS TUPLAS DE LA MATRIZ
            tupla_pos_x_y = matriz_dimensiones_cuadrados[i][j]
            pos_x_cuadrado = tupla_pos_x_y[0]
            pos_y_cuadrado = tupla_pos_x_y[1]
            
            path = lista[i] #EN CADA SUB-LISTA SE PEGA UNA IMAGEN DE LA LISTA (POR ESO lista[i])
            imagen_logo = pygame.image.load(path)
            imagen_logo = pygame.transform.scale(imagen_logo, (ANCHO_CUADRADO, ALTO_CUADRADO))
            pantalla.blit(imagen_logo, (pos_x_cuadrado, pos_y_cuadrado))


def validar_click_en_cuadrantes(matriz_dimensiones_cuadrados: list, pos_x_click: int, pos_y_click: int, lista: list, lista_respuestas_correctas: list):
    """La funcion se encarga de validar si el usuario hizo click o no dentro
    de alguno de los 4 cuadrantes donde se encuentran las imagenes parecidas
    recorriendo l

    Args:
        matriz_dimensiones_cuadrados (list): Recibe por parametro una matriz de tipo list
        (array bidimensional) que contiene todas las posiciones (X,Y) de cada uno de los cuadrados

        pos_x_click (int): Recibe por parametro un numero de tipo int que representa la posicion
        en X donde el usuario hizo click

        pos_y_click (int): Recibe por parametro un numero de tipo int que representa la posicion
        en Y donde el usuario hizo click

        lista (list): Recibe por parametro una lista de str la cual contiene los paths de las imagenes
        de la marca random que va tomando indice tras indice.

        lista_respuestas_correctas (list): Recibe por parametro una lista de str con los paths
        de todas las imagenes correctas.

    Returns:
        tuple: Retorna una tupla, la cual contiene una bandera (bool) y contador de correctas (int)
    """
    contador_correctas = 0
    click_valido = False

    #RECORREMOS LA MATRIZ NUEVAMENTE Y CHEQUEAMOS SI DIO CLICK EN ALGUNO DE LOS 4
    #CUADRANTES
    for i in range(len(matriz_dimensiones_cuadrados)):
        for j in range(len(matriz_dimensiones_cuadrados[i])):
            variable = matriz_dimensiones_cuadrados[i][j]
            pos_x_cuadrado = variable[0]
            pos_y_cuadrado = variable[1]
            
            if pos_x_click >= pos_x_cuadrado and pos_x_click <= (pos_x_cuadrado + ANCHO_CUADRADO) and pos_y_click >= pos_y_cuadrado and pos_y_click <= (pos_y_cuadrado + ALTO_CUADRADO):
                
                click_valido = True
                if lista[i] in lista_respuestas_correctas:                            
                    contador_correctas += 1
    
    return click_valido, contador_correctas


def pegar_imagenes_fijas_pantalla_juego(pantalla)-> None:
    """La funcion se encarga unicamente de pegar en la pantalla de juego
    los elementos fijos que no cambian (como el la imagen del fondo, la de la moneda,
    la del cronometro, etc).

    Args:
        pantalla: Recibe por parametro una pantalla (la cual representa una surface de la libreria Pygame)
    
    Returs:
        No retorna nada, solo pega en la pantalla de juego las imagenes estaticas/fijas.
    """
    #PEGAMOS FONDO DE LA PANTALLA JUEGO
    pantalla.blit(imagen_fondo_juego, (0,0))

    #PEGAMOS VIDAS
    pantalla.blit(vidas_5, (pos_x_vidas, pos_y_vidas))
    
    #PEGAMOS CRONOMETRO, MONEDA Y SPRITE DEL PERSONAJE
    pantalla.blit(imagen_cronometro, (pos_x_cronometro, pos_y_cronometro))
    pantalla.blit(imagen_moneda, (pos_x_moneda, pos_y_moneda))
    pantalla.blit(personaje, (pos_x_personaje, pos_y_personaje))


def dibujar_cuadrado_marca_a_adivinar_y_record_previo(pantalla, lista_marcas_aleatorias: list, k: int, record_previo: int)-> None:
    """La funcion se encarga de dibujar en la pantalla el cuadrado
    que contiene la marca a adivinar (la cual va cambiando ronda tras ronda)
    y de dibujar la burbuja que contiene el record previo del jugador que ingreso
    unicamente si es diferente de 0.

    Args:
        pantalla: Recibe por parametro una pantalla (la cual representa una surface de la libreria Pygame)

        lista_marcas_aleatorias (list): Recibe por parametro una lista de str la cual contiene
        las marcas (keys) del archivo JSON de manera aleatoria y desordenada.

        k (int): Recibe por parametro un numero de tipo int el cual representa los indices
        (que van aumentando a medida que el usuario adivina o no la marca) de la lista de str que contiene
        las marcas generadas de manera random.

        record_previo (int): Recibe por parametro un numero de tipo int que representa
        el record previo del jugador.

    Returns:
        No retorna nada, solo se encarga de dibujar en pantalla.
    """
    #DIBUJAMOS CUADRADADO QUE CONTIENE LA MARCA A ADIVINAR
    pygame.draw.rect(pantalla, colores.AZUL_OSCURO, (pos_x_cuadrado_marca, pos_y_cuadrado_marca, ANCHO_CUADRADO_MARCA, ALTO_CUADRADO_MARCA))
    pygame.draw.rect(pantalla, colores.BLANCO, (pos_x_cuadrado_marca, pos_y_cuadrado_marca, ANCHO_CUADRADO_MARCA, ALTO_CUADRADO_MARCA), 5)

    #RENDERIZAMOS EL TEXTO DE LA MARCA A ADIVINAR Y LO PEGAMOS EN LA PANTALLA
    #(Este mismo va cambiando a medida que cambia el valor de k)
    marca_renderizada = fuente_jugador.render(lista_marcas_aleatorias[k], False, colores.BLANCO, colores.AZUL_OSCURO)
    pantalla.blit(marca_renderizada, (pos_x_texto_marca, pos_y_texto_marca))

    #DIBUJAMOS RECORD PREVIO DEL JUGADOR
    if record_previo != 0:
        texto_puntaje_record = fuente_jugador.render(f'Record: {record_previo}', False, colores.NEGRO)

        pantalla.blit(imagen_burbuja_dialogo_record, (pos_x_imagen_burbuja_dialogo_record, pos_y_imagen_burbuja_dialogo_record))

        pantalla.blit(texto_puntaje_record, (pos_x_texto_record, pos_y_texto_record))


def actualizar_puntos(pantalla, acumulador_puntos: int)-> int: 
    """La funcion se encarga de mostrar el puntaje actual en la pantalla del juego.
    Si el puntaje es negativo, se ajusta a 0 antes de mostrarlo. Esto hace que el 
    puntaje nunca aparezca negativo en la pantalla.

    Args:
        pantalla: Recibe por parametro una pantalla (la cual representa una surface de la libreria Pygame)
        donde se va pegando el puntaje del jugador a medida que avanza de pregunta

        acumulador_puntos (int): Recibe por parametro un numero de tipo int que representa 
        la cantidad de puntos que obtuvo. 

    Returns:
        int: Retorna un numero de tipo int que representa el puntaje actualizado
    """
    if acumulador_puntos < 0:
        acumulador_puntos = 0

    texto_puntos = fuente_puntos.render(f'{acumulador_puntos}', False, colores.AMARILLO_BRILLANTE)
    pantalla.blit(texto_puntos, (pos_x_puntos, pos_y_puntos))
    return acumulador_puntos


#---------------FUNCIONES PARA PANTALLA FINAL/RESULTADOS---------------#

def dibujar_pegar_en_pantalla_final(pantalla, bandera_sonido: bool, puntos_obtenidos: int, promedio_tiempo: int)-> None:
    """La funcion se encarga de pegar en la pantalla final del juego, la cual muestra
    los resultados del jugador al finalizar la partida, todos los elementos necesarios que
    la misma utiliza, como el fondo, la imagen del sonido, el cuadro con los resultados, etc.

    Args:
        pantalla: Recibe por parametro una pantalla (la cual representa una surface de la libreria Pygame)
        
        bandera_sonido (bool): Recibe por parametro una bandera de tipo bool que es utilizada
        para ver si el jugador clickeo en el boton de sonido para apagarlo o no.

        puntos_obtenidos (int): Recibe por parametro un numero de tipo int que representa la
        cantidad de monedas/puntos que el jugador gano en la partid.

        promedio_tiempo (int): Recibe por parametro un numero de tipo int que representa el
        promedio de tiempo que tardo en adivinar todas (o no) las marcas del juego.
    
    Returns:
        No retorna nada, solo se encarga de pegar todo los elementos necesarios en la pantalla
        de resultados/final.
    """
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

