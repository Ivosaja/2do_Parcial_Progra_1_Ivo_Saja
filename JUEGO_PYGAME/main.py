from pantallas import * 
from especificas import *

pygame.init()

primer_inicio = None  #ESTE NONE HACE REFERENCIA A LA PRIMERA VEZ QUE SE CREA LA PANTALLA PRINCIPAL

listas_marcas_aleatoria = cargar_marcas_random_sin_repetir('logos.json')
datos_main = crear_pantalla_principal(primer_inicio)

if datos_main != None:
    pantalla = datos_main[0]
    nombre_jugador = datos_main[1]
    record_previo = datos_main[2]
    partidas_cargadas = datos_main[3]

    while True:
            
            datos = crear_pantalla_juego(pantalla, 'logos.json', listas_marcas_aleatoria, record_previo)
            
            if datos != None:
                pantalla_resultados = datos[0]
                puntos_obtenidos = datos[1]
                promedio_tiempo = datos[2]

                if record_previo < puntos_obtenidos:
                    record_previo = puntos_obtenidos

                volver_a_jugar = crear_pantalla_resultados(pantalla_resultados, puntos_obtenidos, promedio_tiempo)
                guardar_datos_en_csv(nombre_jugador, record_previo, partidas_cargadas)

                if volver_a_jugar != False:

                    sonido_inicio_fin.stop()        
                    volver_menu = crear_pantalla_principal(volver_a_jugar[1])

                    if volver_menu != None:
                        pantalla = volver_menu[0]
                        nombre_jugador = volver_menu[1]
                        record_previo = volver_menu[2]
                        partidas_cargadas = volver_menu[3]
                        
                        listas_marcas_aleatoria = cargar_marcas_random_sin_repetir('logos.json')

                    else:
                        break

                else:
                    break
            else:
                break

pygame.quit()
