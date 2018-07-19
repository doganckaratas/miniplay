#!/usr/bin/python
import curses, sys, signal, time

scr = curses.initscr()
win = curses.newwin(100,60,0,0)
def init(scr):
    curses.noecho()
    curses.cbreak()
    scr.keypad(1)

def kill(scr):
    curses.nocbreak()
    scr.keypad(0)
    curses.echo()
    curses.endwin()

def resize_window(n, frame):
    scr.refresh()

def draw_window(scr):
    #win.box(
    scr.addstr(1,1, "miniplay 1.1 -")
    scr.addstr(1,16, "dogan c. karatas")
    scr.hline(2,1,'-',scr.getmaxyx()[1]-2)
    scr.hline(scr.getmaxyx()[0]-3,1,'-',scr.getmaxyx()[1]-2)
    scr.addstr(scr.getmaxyx()[0]-4,1,"For help, press '?', For exit, press CTRL+C")
    scr.addstr(scr.getmaxyx()[0]-2,1, "Current Channel: ")
    scr.addstr(4,1, "Channel List:")
    scr.border(0)
    scr.refresh()

def main():
   init(scr)
   while 1:
        try:
            signal.signal(signal.SIGWINCH, resize_window)
            draw_window(scr)
        except KeyboardInterrupt:
            kill(scr)
            break

if __name__ == "__main__":
    main()
