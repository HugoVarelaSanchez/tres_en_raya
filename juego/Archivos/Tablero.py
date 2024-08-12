from Usuario import Usuario
from colorama import Fore, Style

class Tablero:
 
    def __init__(self, tablero =[[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], aux_columnas = {'a':0, 'b':1, 'c':2}, usuarios_activos = [] ) -> None:
        
        self.tablero = tablero
        self.aux_columnas = aux_columnas
        self.usuarios_activos = usuarios_activos

    def __repr__(self) -> str:
        resultado = '-------------\n'
        for i in self.tablero:
            resultado += f'| {i[0]} | {i[1]} | {i[2]} |\n'
            resultado += '-------------\n'
        return resultado
    




    '''
    ╔══╗╔══╗╔╗  ╔══╗╔══╗╔══╗╔═══╗   ╔══╗╔══╗╔══╗╔╗╔╗╔══╗
    ║╔═╝║╔╗║║║  ║╔╗║║╔═╝║╔╗║║╔═╗║   ║╔═╝╚╗╔╝║╔═╝║║║║║╔╗║
    ║║  ║║║║║║  ║║║║║║  ║╚╝║║╚═╝║   ║╚═╗ ║║ ║║  ║╚╝║║╚╝║
    ║║  ║║║║║║  ║║║║║║  ║╔╗║║╔╗╔╝   ║╔═╝ ║║ ║║  ║╔╗║║╔╗║
    ║╚═╗║╚╝║║╚═╗║╚╝║║╚═╗║║║║║║║║    ║║  ╔╝╚╗║╚═╗║║║║║║║║
    ╚══╝╚══╝╚══╝╚══╝╚══╝╚╝╚╝╚╝╚╝    ╚╝  ╚══╝╚══╝╚╝╚╝╚╝╚╝
    '''
    def colocar_ficha(self, fila, columna, ficha):
        fila = fila-1
        num_columna = self.aux_columnas[columna]

        self.tablero[fila][num_columna] = ficha




    '''
    ╔═══╗╔═══╗╔══╗╔═══╗╔════╗╔═══╗╔══╗╔═══╗   ╔════╗╔══╗╔══╗ 
    ║╔═╗║║╔══╝║╔═╝║╔══╝╚═╗╔═╝║╔══╝║╔╗║║╔═╗║   ╚═╗╔═╝║╔╗║║╔╗║ 
    ║╚═╝║║╚══╗║╚═╗║╚══╗  ║║  ║╚══╗║╚╝║║╚═╝║     ║║  ║╚╝║║╚╝╚╗
    ║╔╗╔╝║╔══╝╚═╗║║╔══╝  ║║  ║╔══╝║╔╗║║╔╗╔╝     ║║  ║╔╗║║╔═╗║
    ║║║║ ║╚══╗╔═╝║║╚══╗  ║║  ║╚══╗║║║║║║║║      ║║  ║║║║║╚═╝║
    ╚╝╚╝ ╚═══╝╚══╝╚═══╝  ╚╝  ╚═══╝╚╝╚╝╚╝╚╝      ╚╝  ╚╝╚╝╚═══╝ 
    '''
    def resetear_tablero(self):
        self.tablero = [['[]', '[]', '[]'], ['[]', '[]', '[]'], ['[]', '[]', '[]']]



    '''
    ╔╗ ╔╗╔═══╗╔╗╔╗╔╗   ╔╗╔╗╔══╗╔═══╗╔═══╗   ╔══╗╔╗ ╔╗╔╗  ╔══╗╔╗ ╔╗╔═══╗
    ║╚═╝║║╔══╝║║║║║║   ║║║║║╔═╝║╔══╝║╔═╗║   ║╔╗║║╚═╝║║║  ╚╗╔╝║╚═╝║║╔══╝
    ║╔╗ ║║╚══╗║║║║║║   ║║║║║╚═╗║╚══╗║╚═╝║   ║║║║║╔╗ ║║║   ║║ ║╔╗ ║║╚══╗
    ║║╚╗║║╔══╝║║║║║║   ║║║║╚═╗║║╔══╝║╔╗╔╝   ║║║║║║╚╗║║║   ║║ ║║╚╗║║╔══╝
    ║║ ║║║╚══╗║╚╝╚╝║   ║╚╝║╔═╝║║╚══╗║║║║    ║╚╝║║║ ║║║╚═╗╔╝╚╗║║ ║║║╚══╗
    ╚╝ ╚╝╚═══╝╚═╝╚═╝   ╚══╝╚══╝╚═══╝╚╝╚╝    ╚══╝╚╝ ╚╝╚══╝╚══╝╚╝ ╚╝╚═══╝
    '''
    def new_user_online(self, name):
        self.usuarios_activos.append(name)

    

    '''
    ╔══╗╔══╗╔╗  ╔╗╔═══╗╔═══╗╔══╗╔══╗ ╔══╗╔═══╗   ╔═══╗╔══╗╔╗ ╔╗╔══╗╔══╗ ╔══╗╔═══╗
    ║╔═╝║╔╗║║║  ║║║╔═╗║║╔═╗║║╔╗║║╔╗║ ║╔╗║║╔═╗║   ║╔══╝║╔╗║║╚═╝║║╔╗║║╔╗╚╗║╔╗║║╔═╗║
    ║║  ║║║║║╚╗╔╝║║╚═╝║║╚═╝║║║║║║╚╝╚╗║╚╝║║╚═╝║   ║║╔═╗║╚╝║║╔╗ ║║╚╝║║║╚╗║║║║║║╚═╝║
    ║║  ║║║║║╔╗╔╗║║╔══╝║╔╗╔╝║║║║║╔═╗║║╔╗║║╔╗╔╝   ║║╚╗║║╔╗║║║╚╗║║╔╗║║║ ║║║║║║║╔╗╔╝
    ║╚═╗║╚╝║║║╚╝║║║║   ║║║║ ║╚╝║║╚═╝║║║║║║║║║    ║╚═╝║║║║║║║ ║║║║║║║╚═╝║║╚╝║║║║║ 
    ╚══╝╚══╝╚╝  ╚╝╚╝   ╚╝╚╝ ╚══╝╚═══╝╚╝╚╝╚╝╚╝    ╚═══╝╚╝╚╝╚╝ ╚╝╚╝╚╝╚═══╝╚══╝╚╝╚╝ 
    '''
    
    def comproba_ganador(self, user1:Usuario, user2:Usuario):
        
        for i in range(3):

            #Filas y Columnas
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != ' ':

            
                if self.tablero[i] == user1.ficha:
                    user1.win_temp = True
                else: 
                    user2.win_temp == False

                self.tablero[i][0] = f"{Fore.RED}{self.tablero[i][0]}{Style.RESET_ALL}"
                self.tablero[i][1] = f"{Fore.RED}{self.tablero[i][1]}{Style.RESET_ALL}"
                self.tablero[i][2] = f"{Fore.RED}{self.tablero[i][2]}{Style.RESET_ALL}" 
                return True
            

            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != ' ':
                if self.tablero[i] == user1.ficha:
                    user1.win_temp = True
                else: 
                    user2.win_temp == False

                self.tablero[0][i] = f"{Fore.RED}{self.tablero[0][i]}{Style.RESET_ALL}"
                self.tablero[1][i] = f"{Fore.RED}{self.tablero[1][i]}{Style.RESET_ALL}"
                self.tablero[2][i] = f"{Fore.RED}{self.tablero[2][i]}{Style.RESET_ALL}"


                return True
            


    

        #Diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != ' ':
            if self.tablero[i] == user1.ficha:
                user1.win_temp = True
            else: 
                    user2.win_temp == False
            

            for i in range(0, 3):
                 self.tablero[i][i] = f"{Fore.RED}{self.tablero[i][i]}{Style.RESET_ALL}"
                
           
            return True  # Ganador en la diagonal principal
        

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != ' ':
            if self.tablero[i] == user1.ficha:
                    user1.win_temp = True
            else: 
                    user2.win_temp == False

                 
            
            self.tablero[0][2] = f"{Fore.RED}{self.tablero[0][2]}{Style.RESET_ALL}"
            self.tablero[1][1] = f"{Fore.RED}{self.tablero[1][1]}{Style.RESET_ALL}"
            self.tablero[2][0] = f"{Fore.RED}{self.tablero[2][0]}{Style.RESET_ALL}"


            return True
        


            
        return False  


    


        
        