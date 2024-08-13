import os
class Usuario:
 
    def __init__(self, name:str, win_temp:bool, ficha:str, plays:int, plays_win:int, plays_lose:int) -> None:
        
        self.name = name                #Nombre de Usuario
        self.ficha = ficha              #Ficha que ha empleado / empleará en la partida
        self.win_temp = win_temp        #Ganador de la ultima partida¿?

        self.plays = plays
        self.plays_win = plays_win
        self.plays_lose = plays_lose

    @property
    def plays_trowh(self)->int:
        return (self.plays - self.plays_win - self.plays_lose)

    '''
    ╔══╗╔══╗╔╗╔╗╔═══╗   ╔══╗ ╔══╗╔════╗╔══╗
    ║╔═╝║╔╗║║║║║║╔══╝   ║╔╗╚╗║╔╗║╚═╗╔═╝║╔╗║
    ║╚═╗║╚╝║║║║║║╚══╗   ║║╚╗║║╚╝║  ║║  ║╚╝║
    ╚═╗║║╔╗║║╚╝║║╔══╝   ║║ ║║║╔╗║  ║║  ║╔╗║
    ╔═╝║║║║║╚╗╔╝║╚══╗   ║╚═╝║║║║║  ║║  ║║║║
    ╚══╝╚╝╚╝ ╚╝ ╚═══╝   ╚═══╝╚╝╚╝  ╚╝  ╚╝╚╝

    '''
    def save_data(self):
        archivo_path = f'../archivos_usuarios/{self.name}/{self.name}_sesion.txt'
        archivo_absoluto = os.path.abspath(os.path.join(os.path.dirname(__file__), archivo_path))

        with open(archivo_absoluto, 'w', encoding='utf-8') as archivo:
            archivo.write(f'{self.name} bool str {self.plays} {self.plays_win} {self.plays_lose}')


  