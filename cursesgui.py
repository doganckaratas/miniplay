#!/usr/bin/python
import curses, sys, signal, time

scr = curses.initscr()
win = curses.newwin(scr.getmaxyx()[0]-6,scr.getmaxyx()[1]-1,3,0)
title = curses.newwin(3,scr.getmaxyx()[1]-1,0,0)
status = curses.newwin(3,scr.getmaxyx()[1]-1,scr.getmaxyx()[0]-3,0)
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

def draw_title(scr):
    scr.addstr(1,1, "miniplay 1.2 -")
    scr.addstr(1,16, "dogan c. karatas")
    scr.border(0)
    scr.refresh()

def draw_status(scr):
    scr.addstr(1,1, "Current Channel: ")
    scr.border(0)
    scr.refresh()

def draw_content(scr):
    scr.addstr(1,1, "Channel List:")
    scr.addstr(scr.getmaxyx()[0]-2,1,"For help, press '?', For exit, press CTRL+C")
    scr.border(0)
    scr.refresh()

def main():
    signal.signal(signal.SIGWINCH, resize_window)
    draw_title(title)
    draw_status(status)
    draw_content(win)

if __name__ == "__main__":
   init(scr)
   while 1:
        try:
            main()
        except KeyboardInterrupt:
            kill(scr)
            break

