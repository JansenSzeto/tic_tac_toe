import os
import random
import sys

grid = [
    ["    ", "    ", "    "],
    ["    ", "    ", "    "],
    ["    ", "    ", "    "]
]
first_pp = ""
second_pp = ""
input_ = ""
turn = 0
people = []
occuipied = []
abc = ["A", "B", "C"]
def show():
    os.system('cls')
    print(occuipied)
    print(f"""{people[turn]}'s turn""")
    print("   0    1    2")
    for x in range(len(grid)):
        print(f"""{abc[x]}{"|".join(grid[x])}""")
        if x != 2:
            print(" --------------")
    try_again()
    
def try_again():
    global grid
    global occuipied
    input_ = list(input())
    if len(input_) == 2 and input_[0].isdigit() and input_[1].upper() in abc and int(input_[0]) in range(0,3):
        if [abc.index(input_[1].upper()), int(input_[0])] in occuipied:
            show()
        else:
            if turn == 0:
                grid[abc.index(input_[1].upper())][int(input_[0])] = "  ○ "
            elif turn == 1:
                grid[abc.index(input_[1].upper())][int(input_[0])] = "  X "
            occuipied.append([abc.index(input_[1].upper()), int(input_[0])])
            check_if_win()
            next_pp()
    else:
        show()
def next_pp():
    global turn
    turn += 1
    if turn == 2:
        turn -= 2
    show()
def win():
    os.system('cls')
    print(f"""{people[turn]} won""")
    input()
    sys.exit(0)
def check_if_win():
    for x in range(0, 3):
        if grid[x][0] == grid[x][1] == grid[x][2] != "    ":
            win()
        elif grid[0][x] == grid[1][x] == grid[2][x] != "    ":
            win()
    if grid[0][0] == grid[1][1] ==grid[2][2] != "    ":
        win()
    elif grid[0][2] == grid[1][1] == grid[2][0] != "    ":
        win()
def start():
    os.system('cls')
    global first_pp
    global second_pp
    global turn
    global people
    first_pp = input("First person's name: ")
    people.append(first_pp)
    second_pp = input("Second person's name: ")
    people.append(second_pp)
    turn = random.randint(0, 1)
    show()

if __name__ == "__main__":
    start()