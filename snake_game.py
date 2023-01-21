import curses

# setup window
curses.initscr()
win = curses.newwin(20, 60, 0, 0) # y, x
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1) # -1

# snake and food
snake = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)

# game logic
score = 0

while True:
    event = win.getch()
    
    for cord in snake:
        win.addch(cord[0], cord[1], '#')

    win.addch(food[0], food[1], '*')    

curses.endwin()
print(f"Final score = {score}")
