from Tablero import Tablero
from Usuario import Usuario
from bases import Base
from exception import number_not_in_menu
from colorama import Fore, Style
from aux_functions import eleccion

import sys
 









'''
╔╗  ╔╗╔═══╗╔╗ ╔╗╔╗╔╗    ╔╗
║║  ║║║╔══╝║╚═╝║║║║║   ╔╝║
║╚╗╔╝║║╚══╗║╔╗ ║║║║║   ╚╗║
║╔╗╔╗║║╔══╝║║╚╗║║║║║    ║║
║║╚╝║║║╚══╗║║ ║║║╚╝║    ║║
╚╝  ╚╝╚═══╝╚╝ ╚╝╚══╝    ╚╝

'''


def menu_inicio(tab:Tablero, base:Base):
    print('''
    (1) Iniciar Sesion
          
    (2) Registrarse
          
    (3) Salir
        
    ''')

    

    opcion = eleccion(3)
    


    if opcion == 1:
        print('\n Iniciando sesion\n')
        print('\nEscribe \'cancelar\' para cancelar\n')

        nombre = input('Nombre de la cuenta: ')
        if nombre.lower() != 'cancelar':
            contraseña = input('Contraseña de la cuenta: ')
            if contraseña.lower() != 'cancelar':
                user = base.inicio_sesion(nombre, contraseña, tab)
                return user
            else:
                print(f'\n{Fore.YELLOW}Abortando inicio de sesion{Style.RESET_ALL}')
        else:
            print(f'\n{Fore.YELLOW}Abortando inicio de sesion{Style.RESET_ALL}')


    elif opcion == 2:
        print('\n Registrando usuario\n')
        print('\nEscribe \'cancelar\' para cancelar\n')

        nombre = input('Nombre de la cuenta: ')
        if nombre.lower() != 'cancelar':
            contraseña = input('Contraseña de la cuenta: ')
            if contraseña.lower() != 'cancelar':
                base.register(nombre, contraseña)
            else:
                print(f'\n{Fore.YELLOW}Abortando nuevo registro{Style.RESET_ALL}')
        else:
            print(f'\n{Fore.YELLOW}Abortando nuevo registro{Style.RESET_ALL}')


    elif opcion == 3:
         sys.exit()



'''
╔╗  ╔╗╔═══╗╔╗ ╔╗╔╗╔╗   ╔══╗
║║  ║║║╔══╝║╚═╝║║║║║   ╚═╗║
║╚╗╔╝║║╚══╗║╔╗ ║║║║║   ╔═╝║
║╔╗╔╗║║╔══╝║║╚╗║║║║║   ║╔═╝
║║╚╝║║║╚══╗║║ ║║║╚╝║   ║╚═╗
╚╝  ╚╝╚═══╝╚╝ ╚╝╚══╝   ╚══╝

'''


def menu_principal(user1:Usuario, tab:Tablero, base:Base):
 
    print('''
    (1) Jugar partida

    (2) Ver Victorias / Empates / Derrotas

    (3) Ver partidas anteriores

    (4) Cerrar sesion
          
    (5) Salir

    ''')

    op = eleccion(5)

    if op == 1:

        return 'juego'
    
    
    elif op == 2:

        print(f'''User {user1.name}
              
Partidas: {user1.plays}

        Victorias: {user1.plays_win}
        Empates: {user1.plays_trowh}
        Derrotas: {user1.plays_lose}

''')
        return None
    
    
    elif op == 3:
    
        base.mostrar_partidas(user1, tab)
        return None

    elif op == 4:
        
        base.close_sesion(user1, tab)
        return False


    elif op == 5:
        base.close_sesion(user1, tab)
        sys.exit()


    



'''
╔╗  ╔╗╔═══╗╔╗ ╔╗╔╗╔╗   ╔══╗
║║  ║║║╔══╝║╚═╝║║║║║   ╚═╗║
║╚╗╔╝║║╚══╗║╔╗ ║║║║║   ╔═╝║
║╔╗╔╗║║╔══╝║║╚╗║║║║║   ╚═╗║
║║╚╝║║║╚══╗║║ ║║║╚╝║   ╔═╝║
╚╝  ╚╝╚═══╝╚╝ ╚╝╚══╝   ╚══╝

'''





def eleccion_segundo_jugador(user_activo:Usuario, tab:Tablero, base:Base):


    print('''
    (1) Iniciar Sesion
          
    (2) Registrarse
          
    (3) Jugar como invitado

    (4) Cancelar
        
    ''')
        
    opcion = eleccion(4)

    if opcion == 1:
        print('\nIniciando sesion \n')
        print('\nEscribe \'cancelar\' para cancelar\n')

        nombre = input('Nombre de la cuenta: ')
        if nombre.lower() != 'cancelar':
            contraseña = input('Contraseña de la cuenta: ')
            if contraseña.lower() != 'cancelar':
                user = base.inicio_sesion(nombre, contraseña, tab)
                return user
            else:
                print(f'\n{Fore.YELLOW}Abortando inicio de sesion{Style.RESET_ALL}')
        else:
            print(f'\n{Fore.YELLOW}Abortando inicio de sesion{Style.RESET_ALL}')

    


    elif opcion == 2:
        print('\nRegistrando jugado\n')
        print('\nEscribe \'cancelar\' para cancelar\n')

        nombre = input('Nombre de la cuenta: ')
        if nombre.lower() != 'cancelar':
            contraseña = input('Contraseña de la cuenta: ')
            if contraseña.lower() != 'cancelar':
                base.register(nombre, contraseña)
            else:
                print(f'\n{Fore.YELLOW}Abortando nuevo registro{Style.RESET_ALL}')
        else:
            print(f'\n{Fore.YELLOW}Abortando nuevo registro{Style.RESET_ALL}')

    
    elif opcion == 3:
        print('\nIniciando sesion como invitado\n')
        return Usuario('Invitado', False, str, 0, 0, 0)
    

    elif opcion == 4:
        return False
    
    
    #elif opcion == 3:

    #    if tab.usuarios_activos < 2:
    #        print('No hay ningun usuario disponible, inicie sesion')
    #    
    #    else:

    #        lista_users = tab.usuarios_activos.clone()
    #        lista_users.remove(user_activo.name)
    




'''
╔╗  ╔╗╔═══╗╔╗ ╔╗╔╗╔╗   ╔╗╔╗
║║  ║║║╔══╝║╚═╝║║║║║   ║║║║
║╚╗╔╝║║╚══╗║╔╗ ║║║║║   ║╚╝║
║╔╗╔╗║║╔══╝║║╚╗║║║║║   ╚═╗║
║║╚╝║║║╚══╗║║ ║║║╚╝║     ║║
╚╝  ╚╝╚═══╝╚╝ ╚╝╚══╝     ╚╝
'''


def menu_final_juego():
    print('''
    (1) Volver a jugar
          
    (2) Volver a jugar contra otra persona
          
    (3) Menu principal
        
    ''')

    opcion = eleccion(3)
    
    if opcion == 1:
        return None
    
    elif opcion == 2:
        return 'new_people'
    
    else:
        return 'principal'







