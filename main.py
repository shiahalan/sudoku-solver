"""
Sudoku Solver by Alan Shiah
Uses backtracking algorithm
Call stack
Return a value so the previous call can complete on completion of
state space tree nodes
Otherwise, stack overflow
"""
from tools.functions import sudoku_solver, display_board, change_board
from time import sleep

print('Loading...')
print('\n')
for i in range(25):
    sleep(0.1)
    bar = '[]' * i
    print(f'\r{bar}' + '-*' * (25 - i), end='')

print()

print('\n-=Loaded=-')
sleep(2)

print("""
███████ ██    ██ ██████   ██████  ██   ██ ██    ██     ███████  ██████  ██      ██    ██ ███████ ██████  
██      ██    ██ ██   ██ ██    ██ ██  ██  ██    ██     ██      ██    ██ ██      ██    ██ ██      ██   ██ 
███████ ██    ██ ██   ██ ██    ██ █████   ██    ██     ███████ ██    ██ ██      ██    ██ █████   ██████  
     ██ ██    ██ ██   ██ ██    ██ ██  ██  ██    ██          ██ ██    ██ ██       ██  ██  ██      ██   ██ 
███████  ██████  ██████   ██████  ██   ██  ██████      ███████  ██████  ███████   ████   ███████ ██   ██ 
""")


while True:
    choice = input('Choose an option:\n[a]Show Board\n[b]Solve Board\n[c]Change board\n[c]Quit!\n>')
    if choice.lower() == 'a':
        display_board()
    elif choice.lower() == 'b':
        print('Solving...')
        if sudoku_solver(0, 0):
            sleep(2)
            display_board()
        else:
            print("Unsolvable Board")
    elif choice.lower() == 'c':
        change_board()
        print('Randomizing..')
        sleep(1)
        display_board()
    elif choice.lower() == 'd':
        print("Goodbye")
        sleep(1)
        quit()
    else:
        print("Invalid option")
        print('-------------------')
        sleep(1)



