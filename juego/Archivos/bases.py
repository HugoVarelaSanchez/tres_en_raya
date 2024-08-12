from Usuario import Usuario
from Tablero import Tablero
import os

class Base:

    def __init__(self, archivo = [], lista_nombres = []) -> None:

        self.lista_nombres = lista_nombres
        self.archivo = archivo
    





    '''
    ╔══╗ ╔══╗╔════╗╔══╗╔══╗ ╔══╗╔══╗╔═══╗  ╔╗  ╔══╗╔══╗╔════╗
    ║╔╗╚╗║╔╗║╚═╗╔═╝║╔╗║║╔╗║ ║╔╗║║╔═╝║╔══╝  ║║  ╚╗╔╝║╔═╝╚═╗╔═╝
    ║║╚╗║║╚╝║  ║║  ║╚╝║║╚╝╚╗║╚╝║║╚═╗║╚══╗  ║║   ║║ ║╚═╗  ║║  
    ║║ ║║║╔╗║  ║║  ║╔╗║║╔═╗║║╔╗║╚═╗║║╔══╝  ║║   ║║ ╚═╗║  ║║  
    ║╚═╝║║║║║  ║║  ║║║║║╚═╝║║║║║╔═╝║║╚══╗  ║╚═╗╔╝╚╗╔═╝║  ║║  
    ╚═══╝╚╝╚╝  ╚╝  ╚╝╚╝╚═══╝╚╝╚╝╚══╝╚═══╝  ╚══╝╚══╝╚══╝  ╚╝  
    '''
    def read_database(self):
        archivo = 'database.txt'
        aux_lista = []


        with open(archivo, 'r') as contenido:
            usuario = contenido.read()

            for line in usuario.split('\n'):
            
                if len(line) != 0:
                    clave_valor = line.split()
                    clave_valor = tuple(clave_valor)
                    aux_lista.append(clave_valor)
            
            self.archivo = aux_lista
            self.obtein_usernames()
            


    '''
    ╔══╗╔══╗ ╔════╗╔═══╗╔╗ ╔╗╔═══╗╔═══╗   ╔╗ ╔╗╔══╗╔╗  ╔╗╔══╗ ╔═══╗╔═══╗╔══╗
    ║╔╗║║╔╗║ ╚═╗╔═╝║╔══╝║╚═╝║║╔══╝║╔═╗║   ║╚═╝║║╔╗║║║  ║║║╔╗║ ║╔═╗║║╔══╝║╔═╝
    ║║║║║╚╝╚╗  ║║  ║╚══╗║╔╗ ║║╚══╗║╚═╝║   ║╔╗ ║║║║║║╚╗╔╝║║╚╝╚╗║╚═╝║║╚══╗║╚═╗
    ║║║║║╔═╗║  ║║  ║╔══╝║║╚╗║║╔══╝║╔╗╔╝   ║║╚╗║║║║║║╔╗╔╗║║╔═╗║║╔╗╔╝║╔══╝╚═╗║
    ║╚╝║║╚═╝║  ║║  ║╚══╗║║ ║║║╚══╗║║║║    ║║ ║║║╚╝║║║╚╝║║║╚═╝║║║║║ ║╚══╗╔═╝║
    ╚══╝╚═══╝  ╚╝  ╚═══╝╚╝ ╚╝╚═══╝╚╝╚╝    ╚╝ ╚╝╚══╝╚╝  ╚╝╚═══╝╚╝╚╝ ╚═══╝╚══╝
    '''
    def obtein_usernames(self):
        self.lista_nombres = []
        for i in self.archivo:
          self.lista_nombres.append(i[0])




    '''
    ╔══╗╔══╗╔╗  ╔╗╔═══╗╔═══╗╔══╗╔══╗ ╔══╗╔═══╗   ╔╗ ╔╗╔══╗╔╗  ╔╗╔══╗ ╔═══╗╔═══╗
    ║╔═╝║╔╗║║║  ║║║╔═╗║║╔═╗║║╔╗║║╔╗║ ║╔╗║║╔═╗║   ║╚═╝║║╔╗║║║  ║║║╔╗║ ║╔═╗║║╔══╝
    ║║  ║║║║║╚╗╔╝║║╚═╝║║╚═╝║║║║║║╚╝╚╗║╚╝║║╚═╝║   ║╔╗ ║║║║║║╚╗╔╝║║╚╝╚╗║╚═╝║║╚══╗
    ║║  ║║║║║╔╗╔╗║║╔══╝║╔╗╔╝║║║║║╔═╗║║╔╗║║╔╗╔╝   ║║╚╗║║║║║║╔╗╔╗║║╔═╗║║╔╗╔╝║╔══╝
    ║╚═╗║╚╝║║║╚╝║║║║   ║║║║ ║╚╝║║╚═╝║║║║║║║║║    ║║ ║║║╚╝║║║╚╝║║║╚═╝║║║║║ ║╚══╗
    ╚══╝╚══╝╚╝  ╚╝╚╝   ╚╝╚╝ ╚══╝╚═══╝╚╝╚╝╚╝╚╝    ╚╝ ╚╝╚══╝╚╝  ╚╝╚═══╝╚╝╚╝ ╚═══╝
    '''
    def name_in_database(self, nombre):
        if nombre in self.lista_nombres:
            return True

        else:
            return False







    '''
    ╔══╗╔╗ ╔╗╔══╗╔══╗╔══╗╔══╗╔═══╗   ╔══╗╔═══╗╔══╗╔══╗╔══╗╔╗ ╔╗
    ╚╗╔╝║╚═╝║╚╗╔╝║╔═╝╚╗╔╝║╔╗║║╔═╗║   ║╔═╝║╔══╝║╔═╝╚╗╔╝║╔╗║║╚═╝║
     ║║ ║╔╗ ║ ║║ ║║   ║║ ║╚╝║║╚═╝║   ║╚═╗║╚══╗║╚═╗ ║║ ║║║║║╔╗ ║
     ║║ ║║╚╗║ ║║ ║║   ║║ ║╔╗║║╔╗╔╝   ╚═╗║║╔══╝╚═╗║ ║║ ║║║║║║╚╗║
    ╔╝╚╗║║ ║║╔╝╚╗║╚═╗╔╝╚╗║║║║║║║║    ╔═╝║║╚══╗╔═╝║╔╝╚╗║╚╝║║║ ║║
    ╚══╝╚╝ ╚╝╚══╝╚══╝╚══╝╚╝╚╝╚╝╚╝    ╚══╝╚═══╝╚══╝╚══╝╚══╝╚╝ ╚╝
    '''
    def inicio_sesion(self, nombre, contraseña, tablero:Tablero):

        if self.name_in_database(nombre):

            for i in self.archivo:
                if i[0] == nombre and i[1] == contraseña:
                    
                    archivo_path = f'../archivos_usuarios/{nombre}/{nombre}_sesion.txt'
                    archivo_absoluto = os.path.abspath(os.path.join(os.path.dirname(__file__), archivo_path))

                    with open(archivo_absoluto, 'r') as contenido:
                        archivo = contenido.read()
                
                        for line in archivo.split('\n'):
                            if len(line) != 0:

                                partes = line.strip().split()
                                user = Usuario(partes[0], partes[1], partes[2], partes[3], partes[4], partes[5])
                                tablero.new_user_online(nombre)
                            

                    print (f'Usuario {nombre} acaba de iniciar sesion')
                    return user
                
                elif i[0] == nombre and i[1] != contraseña:
                    print( 'Contraseña incorrecta' )
        else:
            print(f'El usuario {nombre} no se encuentra registrado en la base de datos')
    '''
    ╔═══╗╔═══╗╔═══╗╔══╗╔══╗╔════╗╔═══╗╔══╗
    ║╔═╗║║╔══╝║╔══╝╚╗╔╝║╔═╝╚═╗╔═╝║╔═╗║║╔╗║
    ║╚═╝║║╚══╗║║╔═╗ ║║ ║╚═╗  ║║  ║╚═╝║║║║║
    ║╔╗╔╝║╔══╝║║╚╗║ ║║ ╚═╗║  ║║  ║╔╗╔╝║║║║
    ║║║║ ║╚══╗║╚═╝║╔╝╚╗╔═╝║  ║║  ║║║║ ║╚╝║
    ╚╝╚╝ ╚═══╝╚═══╝╚══╝╚══╝  ╚╝  ╚╝╚╝ ╚══╝
    '''
    def register(self, nombre, contraseña):

        if self.name_in_database(nombre):
            print('Ese usuario ya esta registrado en la base de datos')
        
        else:

            with open('database.txt', 'a', encoding='utf-8') as archivo:
                archivo.write(f'{nombre} {contraseña}\n')

            self.read_database()
            self.generar_archivo_guardado(nombre)
            
            archivo_path = f'../archivos_usuarios/{nombre}/{nombre}_sesion.txt'
            archivo_absoluto = os.path.abspath(os.path.join(os.path.dirname(__file__), archivo_path))

            with open(archivo_absoluto, 'w', encoding='utf-8') as archivo:
                archivo.write(f'{nombre} bool str 0 0 0')

            print('Usuario registrado con exito')
        
    '''
    ╔══╗╔═══╗╔═══╗╔═══╗╔══╗╔═══╗   ╔══╗╔═══╗╔══╗╔══╗╔══╗╔╗ ╔╗
    ║╔═╝║╔══╝║╔═╗║║╔═╗║║╔╗║║╔═╗║   ║╔═╝║╔══╝║╔═╝╚╗╔╝║╔╗║║╚═╝║
    ║║  ║╚══╗║╚═╝║║╚═╝║║╚╝║║╚═╝║   ║╚═╗║╚══╗║╚═╗ ║║ ║║║║║╔╗ ║
    ║║  ║╔══╝║╔╗╔╝║╔╗╔╝║╔╗║║╔╗╔╝   ╚═╗║║╔══╝╚═╗║ ║║ ║║║║║║╚╗║
    ║╚═╗║╚══╗║║║║ ║║║║ ║║║║║║║║    ╔═╝║║╚══╗╔═╝║╔╝╚╗║╚╝║║║ ║║
    ╚══╝╚═══╝╚╝╚╝ ╚╝╚╝ ╚╝╚╝╚╝╚╝    ╚══╝╚═══╝╚══╝╚══╝╚══╝╚╝ ╚╝
    '''
    def close_sesion(self, Usuario:Usuario, tablero:Tablero):

        tablero.usuarios_activos.remove(Usuario.name)
        # Ruta relativa a la carpeta 'archivos_usuarios' dentro del proyecto

        archivo_path = f'../archivos_usuarios/{Usuario.name}/{Usuario.name}_sesion.txt'
        archivo_absoluto = os.path.abspath(os.path.join(os.path.dirname(__file__), archivo_path))

        with open(archivo_absoluto, 'w', encoding='utf-8') as archivo:
            archivo.write(f'{Usuario.name} bool str {Usuario.plays} {Usuario.plays_win} {Usuario.plays_lose}')

        


    '''
    ╔═══╗╔═══╗╔╗ ╔╗╔═══╗╔═══╗╔══╗╔═══╗   ╔══╗╔═══╗╔══╗╔╗╔╗╔══╗╔╗╔╗╔══╗╔══╗   ╔═══╗╔╗╔╗╔══╗╔═══╗╔══╗ ╔══╗╔══╗ ╔══╗   ╔╗╔╗╔══╗╔═══╗╔═══╗
    ║╔══╝║╔══╝║╚═╝║║╔══╝║╔═╗║║╔╗║║╔═╗║   ║╔╗║║╔═╗║║╔═╝║║║║╚╗╔╝║║║║║╔╗║║╔═╝   ║╔══╝║║║║║╔╗║║╔═╗║║╔╗╚╗║╔╗║║╔╗╚╗║╔╗║   ║║║║║╔═╝║╔══╝║╔═╗║
    ║║╔═╗║╚══╗║╔╗ ║║╚══╗║╚═╝║║╚╝║║╚═╝║   ║╚╝║║╚═╝║║║  ║╚╝║ ║║ ║║║║║║║║║╚═╗   ║║╔═╗║║║║║╚╝║║╚═╝║║║╚╗║║╚╝║║║╚╗║║║║║   ║║║║║╚═╗║╚══╗║╚═╝║
    ║║╚╗║║╔══╝║║╚╗║║╔══╝║╔╗╔╝║╔╗║║╔╗╔╝   ║╔╗║║╔╗╔╝║║  ║╔╗║ ║║ ║╚╝║║║║║╚═╗║   ║║╚╗║║║║║║╔╗║║╔╗╔╝║║ ║║║╔╗║║║ ║║║║║║   ║║║║╚═╗║║╔══╝║╔╗╔╝
    ║╚═╝║║╚══╗║║ ║║║╚══╗║║║║ ║║║║║║║║    ║║║║║║║║ ║╚═╗║║║║╔╝╚╗╚╗╔╝║╚╝║╔═╝║   ║╚═╝║║╚╝║║║║║║║║║ ║╚═╝║║║║║║╚═╝║║╚╝║   ║╚╝║╔═╝║║╚══╗║║║║ 
    ╚═══╝╚═══╝╚╝ ╚╝╚═══╝╚╝╚╝ ╚╝╚╝╚╝╚╝    ╚╝╚╝╚╝╚╝ ╚══╝╚╝╚╝╚══╝ ╚╝ ╚══╝╚══╝   ╚═══╝╚══╝╚╝╚╝╚╝╚╝ ╚═══╝╚╝╚╝╚═══╝╚══╝   ╚══╝╚══╝╚═══╝╚╝╚╝ 
    '''
    def generar_archivo_guardado(self, user):

        #Sacamos la ruta donde nos encontramos y la usamos de directorio base
        directorio_base = os.path.dirname(os.path.abspath(__file__))
        #Ubicacion del nuevo directorio
        directorio = os.path.join(directorio_base, '../archivos_usuarios', user)
        

        os.makedirs(directorio, exist_ok=True)


        for archivo in [f'partidas_{user}.txt', f'resultados_{user}.txt', f'{user}_sesion.txt']:
            ruta_archivo = os.path.join(directorio, archivo)
            open(ruta_archivo, 'w', encoding='utf-8').close()



    '''
    ╔══╗╔══╗╔╗╔╗╔═══╗   ╔═══╗╔╗  ╔══╗╔╗╔╗╔══╗
    ║╔═╝║╔╗║║║║║║╔══╝   ║╔═╗║║║  ║╔╗║║║║║║╔═╝
    ║╚═╗║╚╝║║║║║║╚══╗   ║╚═╝║║║  ║╚╝║║╚╝║║╚═╗
    ╚═╗║║╔╗║║╚╝║║╔══╝   ║╔══╝║║  ║╔╗║╚═╗║╚═╗║
    ╔═╝║║║║║╚╗╔╝║╚══╗   ║║   ║╚═╗║║║║ ╔╝║╔═╝║
    ╚══╝╚╝╚╝ ╚╝ ╚═══╝   ╚╝   ╚══╝╚╝╚╝ ╚═╝╚══╝
    '''
    def guardado(self, user1:Usuario, user2:Usuario, tablero:Tablero):
        
        new_tab = []
        for i in tablero.tablero:
            temp_tab = []
            for u in i:
                if u == ' ':
                    temp_tab.append('n')
                else:
                    temp_tab.append(u)
            new_tab.append(temp_tab)
            



        #---- Empate ----

        if (user1.win_temp and user2.win_temp) == False:

            #User1
            save_user_1 = f'''Partida empatada
{user1.name} {user1.ficha} {user2.name} {user2.ficha}
{new_tab[0][0]} {new_tab[0][1]} {new_tab[0][2]} {new_tab[1][0]} {new_tab[1][1]} {new_tab[1][2]} {new_tab[2][0]} {new_tab[2][1]} {new_tab[2][2]}\n'''

            #User2
            save_user_2 = f'''Partida empatada
{user2.name} {user2.ficha} {user1.name} {user1.ficha}
{new_tab[0][0]} {new_tab[0][1]} {new_tab[0][2]} {new_tab[1][0]} {new_tab[1][1]} {new_tab[1][2]} {new_tab[2][0]} {new_tab[2][1]} {new_tab[2][2]}\n'''





        #---- Gana User 1 ----

        elif user1.win_temp == True:
            
            #User 1
            save_user_1 = f'''Partida ganada
{user1.name} {user1.ficha} {user2.name} {user2.ficha}
{new_tab[0][0]} {new_tab[0][1]} {new_tab[0][2]} {new_tab[1][0]} {new_tab[1][1]} {new_tab[1][2]} {new_tab[2][0]} {new_tab[2][1]} {new_tab[2][2]}\n'''

            #User 2
            save_user_2 = f'''Partida perdida
{user2.name} {user2.ficha} {user1.name} {user1.ficha}
{new_tab[0][0]} {new_tab[0][1]} {new_tab[0][2]} {new_tab[1][0]} {new_tab[1][1]} {new_tab[1][2]} {new_tab[2][0]} {new_tab[2][1]} {new_tab[2][2]}\n'''



        #---- Gana User 2----

        elif user2.win_temp == True:

            #User1
            save_user_1 = f'''Partida perdida
{user1.name} {user1.ficha} {user2.name} {user2.ficha}
{new_tab[0][0]} {new_tab[0][1]} {new_tab[0][2]} {new_tab[1][0]} {new_tab[1][1]} {new_tab[1][2]} {new_tab[2][0]} {new_tab[2][1]} {new_tab[2][2]}\n'''

            #User 2
            save_user_2 = f'''Partida ganada
{user2.name} {user2.ficha} {user1.name} {user1.ficha}
{new_tab[0][0]} {new_tab[0][1]} {new_tab[0][2]} {new_tab[1][0]} {new_tab[1][1]} {new_tab[1][2]} {new_tab[2][0]} {new_tab[2][1]} {new_tab[2][2]}\n'''




        else:
            save = f'''Error Error
Error Error Error Error
{'E'} {'E'} {'E'} {'E'} {'E'} {'E'} {'E'} {'E'} {'E'}\n'''
        
       
        #Guardado User 1
        
        archivo_path = f'../archivos_usuarios/{user1.name}/partidas_{user1.name}.txt'
        archivo_absoluto = os.path.abspath(os.path.join(os.path.dirname(__file__), archivo_path))

        with open(archivo_absoluto, 'a', encoding='utf-8') as archivo:
            archivo.write(save_user_1)

        
        #Guardado User 2

        archivo_path = f'../archivos_usuarios/{user2.name}/partidas_{user2.name}.txt'
        archivo_absoluto = os.path.abspath(os.path.join(os.path.dirname(__file__), archivo_path))

        with open(archivo_absoluto, 'a', encoding='utf-8') as archivo:
            archivo.write(save_user_2)

    '''
    ╔╗  ╔╗╔══╗╔══╗╔════╗╔═══╗╔══╗╔═══╗   ╔═══╗╔══╗╔═══╗╔════╗╔══╗╔══╗─╔══╗╔══╗
    ║║  ║║║╔╗║║╔═╝╚═╗╔═╝║╔═╗║║╔╗║║╔═╗║   ║╔═╗║║╔╗║║╔═╗║╚═╗╔═╝╚╗╔╝║╔╗╚╗║╔╗║║╔═╝
    ║╚╗╔╝║║║║║║╚═╗  ║║  ║╚═╝║║╚╝║║╚═╝║   ║╚═╝║║╚╝║║╚═╝║  ║║   ║║ ║║╚╗║║╚╝║║╚═╗
    ║╔╗╔╗║║║║║╚═╗║  ║║  ║╔╗╔╝║╔╗║║╔╗╔╝   ║╔══╝║╔╗║║╔╗╔╝  ║║   ║║ ║║ ║║║╔╗║╚═╗║
    ║║╚╝║║║╚╝║╔═╝║  ║║  ║║║║ ║║║║║║║║    ║║   ║║║║║║║║   ║║  ╔╝╚╗║╚═╝║║║║║╔═╝║
    ╚╝  ╚╝╚══╝╚══╝  ╚╝  ╚╝╚╝ ╚╝╚╝╚╝╚╝    ╚╝   ╚╝╚╝╚╝╚╝   ╚╝  ╚══╝╚═══╝╚╝╚╝╚══╝
    '''
    def mostrar_partidas(self, user:Usuario, tab:Tablero):


        archivo_path = f'../archivos_usuarios/{user.name}/partidas_{user.name}.txt'
        archivo_absoluto = os.path.abspath(os.path.join(os.path.dirname(__file__), archivo_path))


        with open(archivo_absoluto, 'r') as contenido:
            archivo = contenido.read()
            count = 1
            lista_partidas = []


            for line in archivo.split('\n'):
                if (count % 3 == 1):
                    temp_partida = []
                    estado_partida = ''
                    estado_partida = line
                    temp_partida.append(estado_partida)

                elif (count % 3 == 2):
                    estado_jugadores = ''
                    partes = line.strip().split()
                    jugador_1 = partes[0]
                    jugador_2 = partes [2]

                    ficha_1 = partes[1]
                    ficha_2 = partes[3]

                    estado_jugadores = f'{jugador_1}: {ficha_1} vs {jugador_2}: {ficha_2}'
                    temp_partida.append(estado_jugadores)


                elif (count % 3 == 0):
                    partes = line.strip().split()
                    for i in range(0, 9):
                        if partes[i] == 'n':
                            partes[i] = ' '
                        
                    partida = [[partes[0], partes[1], partes[2]], [partes[3], partes[4], partes[5]], [partes[6], partes[7], partes[8]]]
                    temp_partida.append(partida)
                    lista_partidas.append(temp_partida)

                count += 1

        
        for partida in lista_partidas:
            print(f'''\n{partida[0]}\n{partida[1]}\n{Tablero(partida[2])}\n''')

