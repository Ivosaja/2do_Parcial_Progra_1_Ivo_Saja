from pantallas import * 
from especificas import *

pygame.init()

primer_inicio = None
#pantalla = crear_pantalla_principal(primer_inicio) #ESTE NONE HACE REFERENCIA A LA PRIMERA VEZ QUE SE CREA LA PANTALLA MAIN
datos_main = crear_pantalla_principal(primer_inicio)
if datos_main != None:
    pantalla = datos_main[0]
    nombre_player = datos_main[1]
    record_previo = datos_main[2]

while True:

    #if pantalla != None:
        
        datos = crear_pantalla_juego(pantalla, 'logos.json', nombre_player, record_previo)

        if datos != None:
            pantalla_resultados = datos[0]
            puntos_obtenidos = datos[1]
            promedio_tiempo = datos[2]
            lista_jugadores = datos[3]
            print(lista_jugadores)

            if pantalla_resultados != None:
                volver_a_jugar = crear_pantalla_resultados(pantalla_resultados, puntos_obtenidos, promedio_tiempo)

                if volver_a_jugar != False:
                    sonido_inicio_fin.stop()
                    #pantalla = crear_pantalla_principal(volver_a_jugar[1])
                    volver_menu = crear_pantalla_principal(volver_a_jugar[1])
                    pantalla = volver_menu[0]
                    nombre_player = volver_menu[1]
                    record_previo = volver_menu[2]
                    

                        
                else:
                    break
        else:
            break


pygame.quit()