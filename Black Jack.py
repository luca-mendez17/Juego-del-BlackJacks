__author__ = 'TP2 - G323'
import random


# definir carta
def generar_carta():
    valor = ("AS", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K")
    palos = ("Diamantes", "Tréboles", "Picas", "Corazones")
    carta = random.choice(valor)
    palo = random.choice(palos)

    if carta == "J" or carta == "Q" or carta == "K":
        valor_carta = 10
    elif carta == "AS":
        valor_carta = 11
    else:
        valor_carta = carta
    return carta, palo, valor_carta


# comienzo del programa
def principal():
    print("BIENVENIDO AL JUEGO DE BLACKJACK")
    nom = input("Ingrese nombre:")
    pozo = int(input("Ingrese pozo que desea para poder jugar al black jack (debe ser menor a $100000) :"))
    while pozo > 100000 or pozo < 0:
        print("ERROR!!! El pozo elegido no es valido")
        pozo = int(input("Vuelva a cargar el valor del pozo (debe ser menor a $100000) :"))

    pozo_apuesta = 0
    apuesta_jugador = 0
    valor_as = 1
    vict_j = 0
    cant_blackjack_nat = 0
    racha_crupier = 0
    perdida = 0
    max_perdida = 0
    racha_max = 0
    cont_ronda = 0
    max_pozo = 0
    sum_apuestas = 0

    # menu
    menu = "OPCIONES DE JUEGO\n" + \
           "1 ...... Apostar \n" + \
           "2 ...... Jugar mano \n" + \
           "3 ...... Salir \n" + \
           "Ingrese opcion:"

    opcion = int(input(menu))
    while opcion != 3:

        # apostar
        if opcion == 1:
            print("*" * 100)
            if pozo >= 100000:
                print("\n   NO SE PUEDE SUMAR MAS DINERO AL POZO \n")
            else:
                mas_pozo = int(input("Agregar dinero al pozo:"))
                if pozo + mas_pozo < 100000:
                    pozo += mas_pozo
                    print("\n*El nuevo valor del pozo es:", pozo, "\n")
                else:
                    print("\nIngreso un valor que hizo que se exeda el pozo maximo \n")
                print("*" * 100)

        # jugar mano
        elif opcion == 2:
            print("*" * 100)
            print("COMIENZO DE LA RONDA")
            print("su pozo es:", pozo)
            if pozo > max_pozo:
                max_pozo = pozo

            # apuesta
            if pozo > 0:
                monto_a_apostar = int(input("Monto que quiere apostar de su pozo (debe ser multiplo de 5 mayor a 0):"))
                if monto_a_apostar % 5 == 0 and monto_a_apostar <= pozo:
                    apuesta_jugador = monto_a_apostar
                    pozo -= apuesta_jugador
                    sum_apuestas += apuesta_jugador
                else:
                    if monto_a_apostar % 5 != 0 and monto_a_apostar <= pozo:
                        print("Apuesta invalida")
                        apuesta_jugador = 0
                    else:
                        print("El monto apostado es mayor al del pozo")
                        apuesta_jugador = 0
            else:
                print("No hay dinero en el pozo para poder apostar")
                apuesta_jugador = 0

            # cartas y desarrollo de mano
            if apuesta_jugador > 0:
                cont_ronda += 1
                carta_j_1 = generar_carta()
                carta_j_2 = generar_carta()
                carta_c_1 = generar_carta()
                print("\nlas cartas de", nom, "son:")
                print("CARTA 1 JUGADOR =", carta_j_1[0], "de", carta_j_1[1])
                print("CARTA 2 JUGADOR =", carta_j_2[0], "de", carta_j_2[1])
                if carta_j_1[0] == "AS" and carta_j_2[0] == "AS":
                    puntaje_j = carta_j_1[2] + valor_as
                else:
                    puntaje_j = carta_j_1[2] + carta_j_2[2]
                print("El puntaje de", nom, "es", puntaje_j)
                print("\nLa carta del crupier es :")
                print("CARTA 1 CRUPIER = ", carta_c_1[0], "de", carta_c_1[1])
                puntaje_c = carta_c_1[2]
                print("El puntaje del crupier es", puntaje_c)
                pedido = "s"
                cant_cartas_j = 2
                cant_cartas_c = 1

                # Black jack natural del jugador
                if puntaje_j == 21 and cant_cartas_j == 2:
                    print("       BLACK JACK NATURAL DE", nom)
                    print("       ", nom, "HA GANADO LA RONDA ")
                    pozo += apuesta_jugador * 2
                    cant_blackjack_nat += 1
                    vict_j += 1
                    if racha_crupier > racha_max or racha_max is None:
                        racha_max = racha_crupier
                        racha_crupier = 0

                else:
                    # pedir carta
                    while puntaje_j < 21 and (pedido == "s" or pedido == "S"):
                        pedido = input("Desea recibir otra carta? (S/N):")
                        if pedido == "S" or pedido == "s":
                            cant_cartas_j += 1
                            carta_j_extra = generar_carta()
                            print("CARTA ", cant_cartas_j, " JUGADOR =", carta_j_extra[0], "de", carta_j_extra[1])
                            if carta_j_extra[0] == "AS" and puntaje_j + 11 > 21:
                                puntaje_j += valor_as
                            else:
                                puntaje_j += carta_j_extra[2]
                            print("El puntaje actual de", nom, "es:", puntaje_j)
                    else:
                        print("\nTERMINO EL TURNO DE,", nom, "\n")

                    # cartas crupier
                    while puntaje_c < 17:
                        cant_cartas_c += 1
                        carta_c_extra = generar_carta()
                        print("CARTA", cant_cartas_c, "CRUPIER =", carta_c_extra[0], "de", carta_c_extra[1])
                        if carta_c_extra[0] == "AS" and puntaje_c + 11 > 21:
                            puntaje_c += valor_as
                        else:
                            puntaje_c += carta_c_extra[2]
                    print("El puntaje del crupier es", puntaje_c)
                    if puntaje_c == 21 and cant_cartas_c == 2:
                        print("       BLACK JACK NATURAL DEL CRUPIER")
                        print("       EL CRUPIER HA GANADO ")
                        cant_blackjack_nat += 1
                        perdida = apuesta_jugador
                        racha_crupier += 1

                    # comparacion juegos del jugador y del crupier
                    else:
                        if (puntaje_c < puntaje_j <= 21) or (puntaje_c > 21 and puntaje_j <= 21):
                            print("       ", nom, "HA GANADO LA RONDA")
                            pozo += apuesta_jugador * 2
                            vict_j += 1
                            if racha_crupier > racha_max or racha_max == 0:
                                racha_max = racha_crupier
                            racha_crupier = 0
                        else:
                            if (puntaje_j < puntaje_c <= 21) or (puntaje_j > 21 and puntaje_c <= 21):
                                print("EL CRUPIER HA GANADO LA RONDA")
                                perdida = apuesta_jugador
                                racha_crupier += 1
                            else:
                                if (puntaje_j == puntaje_c) and (puntaje_j < 21 and puntaje_c < 21):
                                    print("OCURRIO UN EMPATE, EL JUGADOR RECUPERA SU APUESTA")
                                    pozo += apuesta_jugador
                                else:
                                    if puntaje_c > 21 and puntaje_j > 21:
                                        print("AMBOS PIERDEN \n       GANA EL CRUPIER")
                                        perdida = apuesta_jugador
                                        racha_crupier += 1

                    # declaracion perdida y pozo maximos
                    if perdida > max_perdida:
                        max_perdida = perdida
                    if pozo > max_pozo:
                        max_pozo = pozo

                print("EL MONTO ACTUALIZADO DEL POZO ES", pozo, "\n")
                print("*" * 100)

        # opcion no valida
        else:
            print("Opcion no valida, vuelva a ingresar la opcion.")
        opcion = int(input(menu))

    # seleccion 3(salir)
    else:
        print("*" * 100)
        if cont_ronda > 0:
            porcentaje = ((vict_j * 100) / cont_ronda)
            prom = sum_apuestas / cont_ronda
        else:
            porcentaje = prom = 0
        print("*El porcentaje de victorias del jugador es:", porcentaje, "%")
        print("*La racha mas larga de victorias del crupier es", racha_max)
        print("*Cantidad de manos donde hubo Blackjack natural:", cant_blackjack_nat)
        print("*El monto maximo que llego a tener el jugar en el pozo es", max_pozo)
        print("*El monto promedio que dispuso el jugador para realizar las apuestas es", prom)
        if max_perdida > 0:
            print("*La perdida mas grande que sufrio el jugador es", max_perdida)
        else:
            print("*No hubo perdida por parte del jugador")
        print("       FIN DEL PROGRAMA, GRACIAS POR JUGAR")


principal()
