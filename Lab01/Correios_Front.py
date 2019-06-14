import curses
screen = curses.initscr()
curses.noecho()
curses.cbreak()
curses.start_color()
screen.keypad( 1 )    # delete this line
curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_CYAN)
highlightText = curses.color_pair( 1 )
normalText = curses.A_NORMAL
screen.border( 0 )
curses.curs_set( 0 )
box = curses.newwin( 22, 64, 1, 1 )
box.keypad( 1 )
box.box()
box.addstr( 5, 3, "YOU HAVE PRESSED: ")

screen.refresh()    # delete this line
box.refresh()

x = box.getch()
letra=''
while  (x>=97 and x<=122) or(x>=48 and x<=57):
    box.erase()
    letra=letra+chr(x)
    box.addstr( 5, 3, "YOU HAVE PRESSED: " + str(x) )
    box.addstr( 6, 4, "YOU HAVE PRESSED: " + str(letra) )
    screen.border( 0 )
    box.border( 0 )
    screen.refresh()  # delete this line
    box.refresh()     # delete this line
    x = box.getch()

curses.endwin()
exit()






import curses
from curses.textpad import Textbox, rectangle
stdscr = curses.initscr()
def main(stdscr,Numero_Linhas):
    stdscr.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)")
    editwin = curses.newwin(Numero_Linhas,30, 2,1)
    rectangle(stdscr, 1,0, 1+Numero_Linhas+1, 1+30+1)
    stdscr.refresh()
    box = Textbox(editwin)
    # Let the user edit until Ctrl-G is struck.
    box.edit([Control-A,Control-B])
    # Get resulting contents
    message = box.gather()
    return message
Numero_Linhas=1
Contenido=main(stdscr,Numero_Linhas)
print (Contenido)
