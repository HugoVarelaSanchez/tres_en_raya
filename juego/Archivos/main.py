from Tablero import Tablero 
from Usuario import Usuario
from bases import  Base
from menu import menu_inicio, menu_principal, eleccion_segundo_jugador, menu_final_juego
from game import game

def main() :      
    base = Base()
    tab = Tablero()

    base.read_database()

    while True:
        
        user = menu_inicio(tab, base)
        if type(user) == Usuario:
            
            print('pasamos al paso 2')

            aux_bool_1 = True
#-------------------------------------------------------------
            while aux_bool_1:

                opcion = menu_principal(user, tab, base)


                if opcion == False:
                    aux_bool_1 = False


                elif opcion == 'juego':

                    print('Pasamos al paso 3')
                    
                    aux_bool_2 = True
#------------------------------------------------------------------------------------
                    while aux_bool_2:

                        print('\nEleccion Jugador 2: \n')

                        opcion = eleccion_segundo_jugador(user, tab, base)

                        if opcion == False:
                            aux_bool_2 = False
                        
                        elif type(opcion) == Usuario:

                            print('Entramos al paso 4')

                            user2 = opcion

                            aux_bool_3 = True
#------------------------------------------------------------------------------------

                            while aux_bool_3:
                                print('\nIniciando partida:\n')


                                game(user, user2, tab)

                                opcion = menu_final_juego()

                                if opcion == 'new_people':
                                    aux_bool_3 = False

                                elif opcion == 'principal':
                                    base.close_sesion(user2, tab)
                                    aux_bool_3 = False
                                    aux_bool_2 = False                          



                            


main() 

