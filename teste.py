import curses, os #curses es la interfaz para capturar pulsaciones de teclas en el menú, os lanza los archivos
def get_param(prompt_string,X_pos,Y_pos,screenn):
     screenn.addstr(X_pos, Y_pos, prompt_string)
     input = screenn.getstr(X_pos, len(prompt_string)+Y_pos, 60)
     return input

def Tela_Benvinda():
    os.system('mode con: cols=30 lines=5')
    screen = curses.initscr() #Inicializa una nueva ventana para capturar pulsaciones de teclas.
    curses.start_color() # Le permite usar colores al resaltar la opción de menú seleccionada
    screen.keypad(1) # Entrada de captura desde el teclado
    screen.clear()
    screen.border(3)
    screen.addstr(2, 10, "BENVINDO!!!",curses.A_NORMAL|curses.color_pair(0))
    screen.refresh()
    curses.napms(1500)
def login(Usuario,Senha,tentativa):
    os.system('mode con: cols=30 lines=10')
    screenn = curses.initscr() #Inicializa una nueva ventana para capturar pulsaciones de teclas.
    curses.start_color() # Le permite usar colores al resaltar la opción de menú seleccionada
    screenn.keypad(1) # Entrada de captura desde el teclado
    screenn.border(3)
    screenn.addstr(1, 7, "LOGIN",curses.A_NORMAL|curses.color_pair(4))
    X_pos=4
    Y_pos=2
    Text_Usuario = get_param("USUARIO: ",X_pos,Y_pos,screenn)
    curses.noecho()
    Text_Senha = get_param("SENHA: ",X_pos+2,Y_pos,screenn)
    curses.echo()
    screenn.refresh()
    screenn.getch()
    if ((Usuario==Text_Usuario)&(Senha==Text_Senha)):
        return True
    else:
        if tentativa==1:
            return False
        else:
            login(Usuario,Senha,tentativa-1)
#Logar
tentativa=3
Usuario=b"AA"
Senha=b"XX"
#Redimencionando a Tela de LOGIN
Avaliar_Senha=login(Usuario,Senha,tentativa)
if (Avaliar_Senha==True):
    #Tela de BENVINDA
    Tela_Benvinda()
else:
    curses.endwin() #¡VITAL! Esto cierra el sistema de menús y lo regresa al indicador de bash.
