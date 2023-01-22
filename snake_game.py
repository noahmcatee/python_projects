import curses

# setup window
curses.initscr()
win = curses.newwin(20, 80, 0, 0) # y, x
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1) # -1

# snake and food
snake = [(4, 7), (4, 6), (4, 5)]
food = (15, 40)

# game logic
score = 0

ESC = 27
key = curses.KEY_RIGHT

while key != ESC:
    win.addstr(0, 2, 'Score ' + str(score) + ' ')
    win.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120) # increase speed

    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    
    for cord in snake:
        win.addch(cord[0], cord[1], '#')

    win.addch(food[0], food[1], '*')    

curses.endwin()
print(f"Final score = {score}")
