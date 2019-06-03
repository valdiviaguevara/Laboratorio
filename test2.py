#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Topmenu and the submenus are based of the example found at this location http://blog.skeltonnetworks.com/2010/03/python-curses-custom-menu/
# The rest of the work was done by Matthew Bennett and he requests you keep these two mentions when you reuse the code :-)
# Basic code refactoring by Andrew Scheller

import curses, os #curses es la interfaz para capturar pulsaciones de teclas en el menú, os lanza los archivos
import time
import sys
import textwrap
from textwrap import fill

MENU = "menu"
COMMAND = "command"

menu_data = {
'title': "Program Launcher", 'type': MENU, 'subtitle': "Please selection an option...",
'options': [
    {
    'title': "Dosbox Games", 'type': MENU, 'subtitle': "Please selection an option...",
    'options':
    [
        { 'title': "Midnight Resuce", 'type': COMMAND, 'command': 'dosbox2 /path/to/EXE -conf /path/to/dosbox.conf -exit' },
        {
        'title': "Treasure Mountain", 'type': MENU, 'subtitle': "BRAD_TESTE",
        'options':
        [
            { 'title': "FORMULARIO_1", 'type': COMMAND, 'command': 'python C:\\Users\\emily\\Documents\\Juan\\FORMULARIOS\\Correios\\Correios_Front_2.py' },
            { 'title': "FORMULARIO_2", 'type': COMMAND, 'command': '' },
        ]
        },
        {
        'title': "More games", 'type': MENU, 'subtitle': "This is a sub-sub menu example!",
        'options':
        [
            { 'title': "Tetris", 'type': COMMAND, 'command': '' },
            { 'title': "Monopoly", 'type': COMMAND, 'command': '' },
            { 'title': "Ridge Racer", 'type': COMMAND, 'command': '' },
            { 'title': "Snake", 'type': COMMAND, 'command': '' },
            { 'title': "Space Invaders", 'type': COMMAND, 'command': '' },
        ]
        },
    ]
    },
    { 'title': "The Ur-Quan Masters", 'type': COMMAND, 'command': 'uqm' },
    { 'title': "Windows 3.1", 'type': COMMAND, 'command': 'dosbox3 /path/to/my/win31/install/WINDOWS/WIN.COM -conf /path/to/my/special/dosbox2.conf -exit' },
]
}
#FUNÇÃO QUE ESCREVE AS LETRAS NO MEDIO DA TELA DIMENSIONADA
def center_wrap(text, cwidth=100, **kw):
    lines = textwrap.wrap(text, **kw)
    return "\n".join(line.center(cwidth) for line in lines)
#FUNÇÃO QUE ACESSA NA PLATAFORMA DE LOGIN
def login(Tela_centro_Login,Tentativas):
    #NOME E SENHA PARA ACCESAR AO PROGRAMA
    username="AA"
    password="XX"
    #Redimencionando a Tela de LOGIN
    os.system('mode con: cols=30 lines=15')
    #Limpando a tela
    clear = lambda: os.system('cls')
    clear()
    #Incrementando o numero de tentativas para o acceso no sistema
    Tentativas=Tentativas+1
    #Disenhando o Formulario de Senha
    print ("\n\n\n")
    print ("        SENHA:".center(15))
    print ("")
    Text_Username="     USUARIO: ".center(10)
    Text_Password="     CONTRASENHA: ".center(10)
    answer1=input(Text_Username)
    answer2=input(Text_Password)
    #Validando o NOME E SENHA para acessar no Sistema
    if answer1==username and answer2==password:
        #Limpando a tela se esta correta o NOME E SENHA para dar Benvida!!!
        clear = lambda: os.system('cls')
        clear()
        #Escrevendo a BEMVINDA para o Acceso no sistema
        print ("\n\n\n")
        Text_benvinda="BENVINDO NO PROGRAMA"
        print ("")
        print(center_wrap(Text_benvinda, cwidth=Tela_centro_Login, width=37))
        #Capturando por dois segundo a Escrita de BENVINDA
        time.sleep(2)
        #Dimensionando a tela de MENU
        os.system('mode con: cols=70 lines=20')
        #Capturando o largo da tela de MENU
        ts = os.get_terminal_size()
        Tela_centro_Menu=ts.columns-1
        sys.exit
        #Chama a Função de Menu
        processmenu(menu_data)
        #menu(Tela_centro_Menu)
    else:
        if (Tentativas<3):
            #Chama na recurrencia da Função para escrever denovo o NOME E SENHA até 3 VEZES
            login(Tela_centro_Login,Tentativas)
        else:
            #Caso as tentativas acabaram
            print ('')
            print (center_wrap("CONTRASENHA INVALIDA!!!", cwidth=Tela_centro_Login, width=37))
def main():
    #Dimencionando a Tela de LOGIN
    os.system('mode con: cols=30 lines=15')
    #Capturando o largo da tela de Login
    ts = os.get_terminal_size()
    Tela_centro_Login=ts.columns-1
    #Teste para ver o tamanho do largo da tela de login
    print (Tela_centro_Login)
    time.sleep(1)
    #Iniciando o numero de tentativas para o Password
    Tentativas=0
    #Chama na função de Login
    login(Tela_centro_Login,Tentativas)
# Esta función muestra el menú apropiado y devuelve la opción seleccionada.
def runmenu(menu,screen, curses,parent):
    h = curses.color_pair(1) #h es el color para una opción de menú resaltada
    n = curses.A_NORMAL #n es el color para una opción de menú no resaltada
    # averiguar qué texto mostrar como la última opción del menú
    if parent is None:
        lastoption = "Exit"
    else:
        lastoption = "Return to %s menu" % parent['title']

    optioncount = len(menu['options']) # cuantas opciones en este menu
    pos=0 #pos es el índice basado en cero de la opción de menú resaltada. Cada vez que se llama a runmenu, la posición vuelve a 0, cuando finaliza runmenu, se devuelve la posición y le dice al programa qué opción ha sido seleccionada
    oldpos=None # Se utiliza para evitar que la pantalla se vuelva a dibujar cada vez.
    x = None #control para bucle while, le permite desplazarse por las opciones hasta que se presione la tecla de retorno y luego regrese pos al programa

    # Bucle hasta que se pulse la tecla de retorno
    while x !=ord('\n'):
        if pos != oldpos:
                oldpos = pos

        screen.clear() #borra la pantalla anterior al presionar una tecla y actualiza la pantalla basada en pos
        screen.border(0)
        screen.addstr(2,2, menu['title'], curses.A_STANDOUT) # Título para este menú
        screen.addstr(4,2, menu['subtitle'], curses.A_BOLD) #Subtítulo para este menú

        # Muestra todos los elementos del menú, mostrando el elemento 'pos' resaltado
        for index in range(optioncount):
            textstyle = n
            if pos==index:
                textstyle = h
            screen.addstr(5+index,4, "%d - %s" % (index+1, menu['options'][index]['title']), textstyle)
        # Ahora muestra Exit / Return en la parte inferior del menú
        textstyle = n
        if pos==optioncount:
            textstyle = h
        screen.addstr(5+optioncount,4, "%d - %s" % (optioncount+1, lastoption), textstyle)
        screen.refresh()
        # pantalla de actualización terminada

        x = screen.getch() # Obtiene la entrada del usuario

        # ¿Qué es la entrada del usuario?
        if x >= ord('1') and x <= ord(str(optioncount+1)):
            pos = x - ord('0') - 1 # convertir la pulsación de tecla nuevamente en un número, luego restar 1 para obtener el índice
        elif x == 258: # flecha hacia abajo
            if pos < optioncount:
                pos += 1
            else: pos = 0
        elif x == 259: # flecha hacia arriba
            if pos > 0:
                pos += -1
            else: pos = optioncount
        elif x != ord('\n'):
            curses.flash()

    # índice de retorno del artículo seleccionado
    return pos

# Esta función llama a showmenu y luego actúa sobre el elemento seleccionado.
def processmenu(menu, parent=None):
    screen = curses.initscr() #Inicializa una nueva ventana para capturar pulsaciones de teclas.
    curses.noecho() # Desactiva el eco automático de las pulsaciones de teclas (evita que el programa ingrese cada tecla dos veces)
    curses.cbreak() # Desactiva el búfer de línea (ejecuta cada tecla a medida que se presiona en lugar de esperar a que se presione la tecla de retorno)
    curses.start_color() # Le permite usar colores al resaltar la opción de menú seleccionada
    screen.keypad(1) # Entrada de captura desde el teclado
    # Cambia esto para usar diferentes colores al resaltar
    curses.init_pair(1,curses.COLOR_WHITE, curses.COLOR_BLACK) # Configura el par de colores # 1, hace texto negro con fondo blanco
    optioncount = len(menu['options'])
    exitmenu = False
    while not exitmenu: #Bucle hasta que el usuario salga del menú.
        getin = runmenu(menu,screen,curses, parent)
        if getin == optioncount:
            exitmenu = True
        elif menu['options'][getin]['type'] == COMMAND:
            os.system(menu['options'][getin]['command']) # ejecuta el comando
        elif menu['options'][getin]['type'] == MENU:
            processmenu(menu['options'][getin], menu) # mostrar el submenú

# Programa principal
#Dimencionando a Tela de LOGIN
#processmenu(menu_data)
main()
curses.endwin() #¡VITAL! Esto cierra el sistema de menús y lo regresa al indicador de bash.
