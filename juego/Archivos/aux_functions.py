from colorama import Fore, Style
from exception import number_not_in_menu


'''
╔═══╗╔═══╗╔═══╗╔══╗╔═══╗   ╔══╗╔╗╔╗╔══╗╔═══╗
║╔══╝║╔═╗║║╔═╗║║╔╗║║╔═╗║   ║╔═╝║║║║╚╗╔╝║╔═╗║
║╚══╗║╚═╝║║╚═╝║║║║║║╚═╝║   ║║  ║╚╝║ ║║ ║╚═╝║
║╔══╝║╔╗╔╝║╔╗╔╝║║║║║╔╗╔╝   ║║  ║╔╗║ ║║ ║╔══╝
║╚══╗║║║║ ║║║║ ║╚╝║║║║║    ║╚═╗║║║║╔╝╚╗║║   
╚═══╝╚╝╚╝ ╚╝╚╝ ╚══╝╚╝╚╝    ╚══╝╚╝╚╝╚══╝╚╝   
'''

def obtener_fila():
    while True:

            try:
                fila = int(input('Fila: '))

                if fila < 1 or fila > 3:
                    raise number_not_in_menu
                break

            except ValueError:
                print(f'\n{Fore.YELLOW}Las filas se denominan con numeros del {Fore.RED}1 {Fore.YELLOW}al {Fore.RED}3 {Fore.YELLOW}de arriba a abajo{Style.RESET_ALL}\n')
            except number_not_in_menu:
                print(f'\n{Fore.RED}Debes introducir el numero de una fila{Style.RESET_ALL}\n')
    return fila



def obtener_columna():
    while True:

            try:
                columna = input('Columna: ')

                if columna not in ['a', 'b', 'c']:
                    raise number_not_in_menu
                break

           
            except number_not_in_menu:
                print(f'\n{Fore.YELLOW}Las columnas se denominan con letras del la {Fore.RED}a {Fore.YELLOW}a la {Fore.RED}c {Fore.YELLOW}de {Fore.RED}izquierda {Fore.YELLOW}a {Fore.RED}derecha{Style.RESET_ALL}\n')
    
    return columna




'''
╔═══╗╔╗  ╔═══╗╔══╗╔══╗╔══╗╔══╗╔╗ ╔╗╔═══╗╔══╗
║╔══╝║║  ║╔══╝║╔═╝║╔═╝╚╗╔╝║╔╗║║╚═╝║║╔══╝║╔═╝
║╚══╗║║  ║╚══╗║║  ║║   ║║ ║║║║║╔╗ ║║╚══╗║╚═╗
║╔══╝║║  ║╔══╝║║  ║║   ║║ ║║║║║║╚╗║║╔══╝╚═╗║
║╚══╗║╚═╗║╚══╗║╚═╗║╚═╗╔╝╚╗║╚╝║║║ ║║║╚══╗╔═╝║
╚═══╝╚══╝╚═══╝╚══╝╚══╝╚══╝╚══╝╚╝ ╚╝╚═══╝╚══╝
'''

def eleccion(num_opciones:int):
    while True:
            try:
                opcion= int(input(f'Opcion: '))

                if opcion < 1 or opcion > num_opciones:
                    raise number_not_in_menu
                break

            except ValueError:
                print(f'\n{Fore.RED}Debes introducir un numero{Style.RESET_ALL}\n')
            except number_not_in_menu:
                print(f'\n{Fore.RED}Debes introducir un numero que aparezca en las opciones{Style.RESET_ALL}\n')
    
    return opcion