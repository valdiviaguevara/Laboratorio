#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Topmenu and the submenus are based of the example found at this location http://blog.skeltonnetworks.com/2010/03/python-curses-custom-menu/
# The rest of the work was done by Matthew Bennett and he requests you keep these two mentions when you reuse the code :-)
# Basic code refactoring by Andrew Scheller

import curses, os #curses es la interfaz para capturar pulsaciones de teclas en el menú, os lanza los archivos
screen = curses.initscr() #Inicializa una nueva ventana para capturar pulsaciones de teclas.
curses.noecho() # Desactiva el eco automático de las pulsaciones de teclas (evita que el programa ingrese cada tecla dos veces)
curses.cbreak() # Desactiva el búfer de línea (ejecuta cada tecla a medida que se presiona en lugar de esperar a que se presione la tecla de retorno)
curses.start_color() # Le permite usar colores al resaltar la opción de menú seleccionada
screen.keypad(1) # Entrada de captura desde el teclado

# Cambia esto para usar diferentes colores al resaltar
curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE) # Configura el par de colores # 1, hace texto negro con fondo blanco
h = curses.color_pair(1) #h es el color para una opción de menú resaltada
n = curses.A_NORMAL #n es el color para una opción de menú no resaltada

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
def get_param(prompt_string):
     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, prompt_string)
     screen.refresh()
     input = screen.getstr(10, 10, 60)
     return input

def execute_cmd(cmd_string):
     system("clear")
     a = system(cmd_string)
     print ("")
     if a == 0:
          print ("Command executed correctly")
     else:
          print ("Command terminated with error")
     raw_input("Press enter")
     print ("")
def login(Usuario,Senha,tentativa):
    screen.border(0)
    screen.addstr(1, 2, "LOGIN")
    Text_Usuario = get_param("USUARIO: ")
    Text_Senha = get_param("SENHA: ")
    screen.refresh()
    screen.getch()
    if ((Usuario==Text_Usuario)&(Senha==Text_Senha)):
        return True
    else:
        if tentativa==1:
            return False
        else:
            login(Usuario,Senha,tentativa-1)
def Tela_Benvinda():
    screen.clear()
    screen.addstr(1, 2, "BENVINDO!!!",curses.A_STANDOUT|curses.color_pair(3))
    screen.refresh()
    curses.napms(1000)

# Esta función muestra el menú apropiado y devuelve la opción seleccionada.
def runmenu(menu, parent):

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
  optioncount = len(menu['options'])
  exitmenu = False
  while not exitmenu: #Bucle hasta que el usuario salga del menú.
    getin = runmenu(menu, parent)
    if getin == optioncount:
        exitmenu = True
    elif menu['options'][getin]['type'] == COMMAND:
        os.system(menu['options'][getin]['command']) # ejecuta el comando
    elif menu['options'][getin]['type'] == MENU:
      processmenu(menu['options'][getin], menu) # mostrar el submenú

#Logar
tentativa=3
Usuario=b"AA"
Senha=b"XX"
Avaliar_Senha=login(Usuario,Senha,tentativa)
if (Avaliar_Senha==True):
    #Tela de BENVINDA
    Tela_Benvinda()
    #Entrar no Programa principal
    processmenu(menu_data)
    curses.endwin()
else:
    curses.endwin() #¡VITAL! Esto cierra el sistema de menús y lo regresa al indicador de bash.
