from Tablero import Tablero
from Usuario import Usuario
from colorama import Fore, Style
from bases import Base

import random


def game(user1:Usuario, user2:Usuario, tab:Tablero):
    tab.resetear_tablero()

    user1.win_temp = False
    user2.win_temp = False

    user1.plays += 1
    user2.plays += 1
    

    user1.ficha = random.choice(['x', 'o'])

    if user1.ficha == 'x':
        jugador1 = user1
        user2.ficha = 'o'
        jugador2 = user2

    else:
        user2.ficha = 'x'
        jugador1 = user2
        jugador2 = user1




    print(f'\nComienza {Fore.BLUE}{jugador1.name}{Style.RESET_ALL} con {Fore.BLUE}{jugador1.ficha}{Style.RESET_ALL}\nContinua {Fore.BLUE}{jugador2.name}{Style.RESET_ALL} con {Fore.BLUE}{jugador2.ficha}{Style.RESET_ALL}\n')
    print(tab)
    while True:

        
        print(f'Coloca {Fore.BLUE}{jugador1.name}{Style.RESET_ALL}')
        tab.colocar_ficha(jugador1.ficha)

        if tab.comproba_ganador(jugador1, jugador2):
            #print(tab)
            break
        else:
            print(tab)


        print(f'Coloca {Fore.BLUE}{jugador2.name}{Style.RESET_ALL}')
        tab.colocar_ficha(jugador2.ficha)

        if tab.comproba_ganador(jugador1, jugador2):
            #print(tab)
            break
        else:
            print(tab)
    
    

    print(tab)

    if jugador1.ficha == user1.ficha:
        user1 = jugador1
        user2 = jugador2
    else:
        user1 = jugador2
        user2 = jugador1

    user1.save_data()
    if user2.name != 'Invitado':
        user2.save_data()
    
    if user1.win_temp == True:
        print(f'\n{Fore.GREEN}Ganador: {user1.name} ({user1.ficha}){Style.RESET_ALL}\n')
    
    elif user2.win_temp == True:
        print(f'\n{Fore.GREEN}Ganador: {user2.name} ({user2.ficha}){Style.RESET_ALL}\n')
    else:
        print(f'{Fore.RED}EMPATE{Style.RESET_ALL}')
    
    Base().guardado(user1, user2, tab)
    





    


    
    