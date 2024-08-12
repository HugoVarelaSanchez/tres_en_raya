from Usuario import Usuario
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

            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != '':
                return self.tablero[i][0]  # Ganador en la fila i
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != '':
                return self.tablero[0][i]  # Ganador en la columna i
    
            # Comprobar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != '':
            return self.tablero[0][0]  # Ganador en la diagonal principal
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != '':
            return self.tablero[0][2]  # Ganador en la diagonal secundaria
    
            return None  # No hay ganador aún


    


        
        