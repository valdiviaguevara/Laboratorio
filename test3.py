import curses
from multiprocessing import Process

p = None
def display(stdscr):
    stdscr.clear()
    stdscr.timeout(500)

    maxy, maxx = stdscr.getmaxyx()
    curses.newwin(2,maxx-1,3,1)
    # invisible cursor
    curses.curs_set(1)

    if (curses.has_colors()):
        # Start colors in curses
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_RED, -1)
    stdscr.refresh()

    curses.init_pair(1, 0, -1)
    curses.init_pair(2, 1, -1)
    curses.init_pair(3, 2, -1)
    curses.init_pair(4, 3, -1)

    bottomBox = curses.newwin(8,maxx-2,maxy-40,1)
    bottomBox.box()
    bottomBox.addstr("BottomBox")
    bottomBox.refresh()
    bottomwindow = curses.newwin(6,maxx-4,maxy-20,2)
    bottomwindow.addstr("{:20s}".format("This is my bottom view"), curses.A_UNDERLINE|curses.color_pair(4))
    bottomwindow.addstr(2, 1, 'Hello ', curses.A_NORMAL | curses.color_pair(4))
    bottomwindow.addstr(2, 10, 'bold', curses.A_BOLD | curses.color_pair(0))
    bottomwindow.addstr(2, 20, ' world', curses.A_NORMAL | curses.color_pair(0))
    bottomwindow.addstr(3, 0, 'See: ', curses.A_NORMAL | curses.color_pair(0))
    bottomwindow.addstr(3, 5, 'www.gnu.org', curses.A_UNDERLINE| curses.color_pair(8))
    bottomwindow.refresh()

    stdscr.addstr("{:20s}".format("Hello world !"), curses.color_pair(4))
    stdscr.refresh()
    while True:
        event = stdscr.getch()
        if event == ord("q"):
            break

def hang():
    while True:
        temp = 1 + 1

if __name__ == '__main__':
    p = Process(target = hang)
    curses.wrapper(display)
    curses.endwin()
