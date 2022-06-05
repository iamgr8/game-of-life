import sys,os
import curses

def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

     # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

     # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

     # Loop where k is the last character pressed
    while (k != ord('q')):

         # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1

        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        # Declaration of strings
        title = "Curses example"[:width-1]
        subtitle = "Written by Clay McLeod"[:width-1]
        keystr = "Last key pressed: {}".format(k)[:width-1]
        statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(cursor_x, cursor_y)
        if k == 0:
            keystr = "No key press detected..."[:width-1]

         # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        start_y = int((height // 2) - 2)

         # Rendering some text
        whstr = "Width: {}, Height: {}".format(width, height)
        stdscr.addstr(0, 0, whstr, curses.color_pair(1))

         # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

         # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

         # Rendering title
        stdscr.addstr(start_y, start_x_title, title)

         # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

         # Print rest of text
        stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        stdscr.addstr(start_y + 3, (width // 2) - 2, '-' * 4)
        stdscr.addstr(start_y + 5, start_x_keystr, keystr)
        stdscr.move(cursor_y, cursor_x)

         # Refresh the screen
        stdscr.refresh()

         # Wait for next input
        k = stdscr.getch()

def fire():
    #!/usr/bin/python
    import curses, random

    screen  = curses.initscr()
    width   = screen.getmaxyx()[1]
    height  = screen.getmaxyx()[0]
    size    = width*height
    char    = [" ", ".", ":", "^", "*", "x", "s", "S", "#", "$"]
    b       = []

    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1,0,0)
    curses.init_pair(2,1,0)
    curses.init_pair(3,3,0)
    curses.init_pair(4,4,0)
    screen.clear
    for i in range(size+width+1): b.append(0)

    while 1:
            for i in range(int(width/9)): b[int((random.random()*width)+width*(height-1))]=65
            for i in range(size):
                    b[i]=int((b[i]+b[i+1]+b[i+width]+b[i+width+1])/4)
                    color=(4 if b[i]>15 else (3 if b[i]>9 else (2 if b[i]>4 else 1)))
                    if(i<size-1):   screen.addstr(  int(i/width),
                                                    i%width,
                                                    char[(9 if b[i]>9 else b[i])],
                                                    curses.color_pair(color) | curses.A_BOLD )

            screen.refresh()
            screen.timeout(30)
            if (screen.getch()!=-1): break

    curses.endwin()

def main():
    curses.wrapper(draw_menu)

def exp():
    #stdscr = curses.initscr()
    curses.initscr()
    curses.start_color()
    
    stdscr = curses.newwin(25, 25, 12, 12)
    s = stdscr.getch()
    stdscr.clear()
    y,x = stdscr.getmaxyx()
    while s != ord('q'):
        
        stdscr.refresh()

        stdscr.addstr(y//2,x//2, "Hello!",curses.color_pair(1))

        stdscr.refresh()
        
        s = stdscr.getch()

    curses.endwin()

   

if __name__ == "__main__":
    #main()
    #fire()
    exp()
    

