import random
import time, os,sys
import curses

###############################################################
# a dead_state function that takes width and height 
# and returns a board of zeros (width x height).

def dead_state(w,h):
    return [[0 for i in range(w)] for j in range(h)] 

# function that randomizes values in dead state to 0 or 1

def random_state(w,h):
    state = dead_state(w, h)
    
    for i in range(h):
        for j in range(w):
            state[i][j] = random.choice([0,1])

    return state

# function to print the board in a comprehensible way 
def render(state):
    w, h = len(state[0]), len(state)
    for i in range(w+2):
        print('-',end='')
    print('',end='\n')
    
    for i in range(h):
        print('|', end='')
        for j in range(w):
            if state[i][j] == 1:
                print('\x1b[6;30;47m' + ' '+ '\x1b[0m',end='')
            else:
                print(' ',end='')
        print('|',end='\n')
        
    for i in range(w+2):
        print('-',end='')
        
    print('',end='\n')

# function to calculate neighbouring cells 

def neighbours(i,j,w,h):
    change = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
    for c in change:
        x,y = c[0]+i,c[1]+j
        
        if (x >= 0 and x < w) and (y >= 0 and y < h):
            yield x,y

# function to calculate the next state of the board

def next_board_state(state):
    init_state = state
    w, h = len(state[0]), len(state)
    next_state = dead_state(w, h)
    
    for i in range(h):
        for j in range(w):
            l = 0
            for n in neighbours(i, j, w, h):
                if init_state[n[0]][n[1]]:
                    l += 1
            
            if init_state[i][j]:
                if l == 0 or l == 1 or l > 3:
                    next_state[i][j] = 0
                elif l == 2 or l == 3:
                    next_state[i][j] = 1
            else:
                if l == 3:
                    next_state[i][j] = 1
            #if l == 0 or l == 1:
            #    state[i][j] = 0
            #elif (l == 2 or l == 3) and init_state[i][j]:
            #    state[i][j] = 1
            #elif l > 3 :
            #    state[i][j] = 0
            #elif l == 3:
            #    state[i][j] = 1
                
            
    return next_state

toad = [[0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,1,1,1,0],
        [0,1,1,1,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]]



def run(board):
    render(board)
    time.sleep(2)
    while True:
        try:
            clear = os.system("cls")
            board = next_board_state(board)
            render(board)
            time.sleep(0.5)
        except KeyboardInterrupt:
            print("it will exit now!")
            sys.exit()
    

run(toad)

def test(exp_state, next_state):
    if exp_state == next_state:
        print("Success")
    else:
        print("Failed")
        print(next_state)






