from Tablero import Tablero
class Usuario:

    def __init__(self, name:str, win_temp:bool, ficha:str, plays:int, plays_win:int, plays_lose:int) -> None:
        
        self.name = name                #Nombre de Usuario
        self.ficha = ficha              #Ficha que ha empleado / empleará en la partida
        self.win_temp = win_temp        #Ganador de la ultima partida¿?

        self.plays = plays
        self.plays_win = plays_win
        self.plays_lose = plays_lose

    @property
    def plays_trowh(self):
        return (self.plays-self.plays_win-self.plays_lose)



 