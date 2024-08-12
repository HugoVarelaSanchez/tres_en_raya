from Tablero import Tablero
from Usuario import Usuario
from bases import  Base


def main() :      
   
    
    tab = Tablero()
    A = Base()
    #Juan = Usuario('Juan', True, 'x', 0, 0, 0)
    #Hugo = Usuario('Hugo', False, '0', 0, 0, 0)
    #A.generar_archivo_guardado('Juan')
    #A.generar_archivo_guardado('Hugo')
    A.read_database()
    #print(A.archivo)
    #print(A.lista_nombres)
    #A.register('uno', 'dos')
    #A.register('tres', 'cuatro')
    #A.register('cinco', 'seis')
    #print(A.archivo)
    #print(A.lista_nombres)
    #A.name_in_database('dos')
    #A.name_in_database('uno')    
    A.inicio_sesion('cero', 'pepe', tab)
    A.inicio_sesion('uno', 'pepe', tab)
    a = A.inicio_sesion('uno', 'dos', tab)
    b = A.inicio_sesion('tres', 'cuatro', tab)
    print(tab.usuarios_activos)
    #A.register('uno', 'salmon')
    #A.register('cero', 'password')
    a.win_temp = False
    A.guardado(a, b, tab)


    A.mostrar_partidas(a, tab)

    A.close_sesion(a, tab)
    

main()