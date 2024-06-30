from pantallas import * 
from especificas import *


pygame.init()

primer_inicio = None  #ESTE NONE HACE REFERENCIA A LA PRIMERA VEZ QUE SE CREA LA PANTALLA MAIN
#pantalla = crear_pantalla_principal(primer_inicio) 


listas_marcas_aleatoria = cargar_marcas_random_sin_repetir('logos.json')
datos_main = crear_pantalla_principal(primer_inicio)

if datos_main != None:
    pantalla = datos_main[0]
    nombre_jugador = datos_main[1]

    while True:
            
            print(listas_marcas_aleatoria)
        
            datos = crear_pantalla_juego(pantalla, 'logos.json', listas_marcas_aleatoria, nombre_jugador)
            
            if datos != None:
                pantalla_resultados = datos[0]
                puntos_obtenidos = datos[1]
                promedio_tiempo = datos[2]

                volver_a_jugar = crear_pantalla_resultados(pantalla_resultados, puntos_obtenidos, promedio_tiempo)
                

                if volver_a_jugar != False:
                    sonido_inicio_fin.stop()

                    #pantalla = crear_pantalla_principal(volver_a_jugar[1])
                    
                    volver_menu = crear_pantalla_principal(volver_a_jugar[1])

                    if volver_menu != None:
                        pantalla = volver_menu[0]
                        nombre_player = volver_menu[1] 
                          
                        listas_marcas_aleatoria = cargar_marcas_random_sin_repetir('logos.json')


                    else:
                        break

                else:
                    break
            else:
                break

pygame.quit()