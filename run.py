import random
import os
from player import Player


def main():

    play()
    return 1

def play():
    print("Welcome to")
    print("\
 _______  _        _______ _________ _______\n\
(  ____ \( \      (  ___  )\__   __/(  ____ \ \n\
| (    \/| (      | (   ) |   ) (   | (    \/\n\
| (_____ | |      | |   | |   | |   | (_____ \n\
(_____  )| |      | |   | |   | |   (_____  )\n\
      ) || |      | |   | |   | |         ) |\n\
/\____) || (____/\| (___) |   | |   /\____) |\n\
\_______)(_______/(_______)   )_(   \_______) !\n\
                                             ")
    p = Player(checkfl(input("Enter starting amount:")), .05)
    d = Slot(p)
    while True:
        if p.checkplay():
            tmp = input("\'r\' Rules \'p\' Pay Lines \'q\' Quit | \'enter\' to Spin\n-")
            #tmp = input("Spin Again? (\"q\" to exit)")
            if tmp == "p":
                d.print_win_lines()
            if tmp != "q":
                os.system("clear")
                d.draw()
            else:
                break
        else:
            print("Game over!")
            break
    p.endreport()
    print("Thanks For Playing!")
    # randomise()

def menu():
    while True:
        tmp = input(":")


def checkfl(var):
    tmp = var
    while True:
        try:
            tmp = float(var)
            break
        except:
            var = input("Try Again..")
    return tmp


def randomise():
    symbl = ["9", "X", "J", "Q", "K", "A"]  # initial symbols
    # create dict of values
    symbd = {}
    dictc = 0  # dict count
    for s in range(10):  # repeat this 10 times
        count = len(symbl)
        for i in symbl:
            for a in range(count):
                symbd[dictc] = i
                dictc += 1
            count = count - 1
    #print(len(symbd))
    #symb = {}
    valmegalist = []
    vals = [[], [], []]
    for a in range(100):
        for i in range(3):
            for e in range(5):
                vals[i].append(symbd[random.randrange(0, dictc)])
        #  print(vals)
        valmegalist.append(vals)
        vals = [[], [], []]
    #print(valmegalist)

    return valmegalist[random.randrange(0, 100)]


class Slot:
    def __init__(self, player):
        self.player = player

    def winlines(self):
        # 20 winlines
        return [
                ["0:0", "0:1", "0:2", "0:3", "0:4"],  # straight line
                ["1:0", "1:1", "1:2", "1:3", "1:4"],  # straight line
                ["2:0", "2:1", "2:2", "2:3", "2:4"],  # straight line
                ["0:0", "2:1", "0:2", "2:3", "0:4"],  # top zigzag
                ["2:0", "0:1", "2:2", "0:3", "2:4"],  # bottom zigzag
                ["1:0", "0:1", "1:2", "0:3", "1:4"],  # top midzag
                ["1:0", "2:1", "1:2", "2:3", "1:4"],  # bottom midzag
                ["2:0", "0:1", "0:2", "0:3", "2:4"],  # tophat
                ["0:0", "2:1", "2:2", "2:3", "0:4"],  # bowl
                ["0:0", "2:1", "1:2", "2:3", "0:4"],  # W
                ["2:0", "0:1", "1:2", "0:3", "2:4"],  # M
                ["2:0", "1:1", "0:2", "1:3", "2:4"],  # A
                ["0:0", "1:1", "2:2", "1:3", "0:4"],  # V
                ["0:0", "0:1", "1:2", "2:3", "2:4"],  # Z
                ["2:0", "2:1", "1:2", "0:3", "0:4"],  # flipz
                ["1:0", "0:1", "0:2", "0:3", "1:4"],  # small hat
                ["1:0", "2:1", "2:2", "2:3", "1:4"],  # small bowl
                ["0:0", "1:1", "1:2", "1:3", "2:4"],  # top squigle
                ["2:0", "1:1", "1:2", "1:3", "0:4"],  # bottom squigle
                ["0:0", "0:1", "2:2", "0:3", "0:4"]  # side -V-
                ]
        # ["", "", "", "", ""]  # empty

    def print_win_lines(self):
        combs = self.winlines()
        count = 1

        for c in combs:
            tmp = [[" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "]]
            for a in c:
                atmp = a.split(":")
                tmp[int(atmp[0])][int(atmp[1])] = "+"
            print("\n---------------------")
            for i in range(len(tmp)):  # print grid
                print("| {} | {} | {} | {} | {} |".format(tmp[i][0], tmp[i][1],
                                                      tmp[i][2], tmp[i][3], tmp[i][4]))
                print("---------------------")
            input("Win Line {}. (CONTINUE...)".format(count))
            os.system("clear")
            count += 1
        return


    def calcu(self):
        # lines
        won = 0
        winlines = 0
        combs = self.winlines()
        for i in combs:
            c = 0
            first = ""
            for e in i:
                tmp = e.split(":")  # split line
                if c == 0:
                    first = self.vals[int(tmp[0])][int(tmp[1])]

                if self.vals[int(tmp[0])][int(tmp[1])] == first:
                    c = c + 1
                else:
                    break
            if c < 3:
                pass
            elif c == 3:
                won += (self.val(first)) * (self.player.get_spinval() * 100)
                winlines += 1
            elif c == 4:
                won += (self.val(first) * 2) * (self.player.get_spinval() * 100)
                winlines += 1
            elif c == 5:
                won += (self.val(first) * 10) * (self.player.get_spinval() * 100)
                winlines += 1
        self.player.update(won, winlines)
        #print("Won: {}".format(won))
        return

    def val(self, val):
        if val == "9":
            return 0.01
        if val == "X":
            return 0.02
        if val == "J":
            return 0.1
        if val == "Q":
            return 0.5
        if val == "K":
            return 1
        if val == "A":
            return 2
        #if val == "+":
        #    return "Jackpot"

    def draw(self):
        self.vals = randomise()
        #  print(vals)
        print("---------------------")
        for i in range(3):  # print grid
            print("| {} | {} | {} | {} | {} |".format(self.vals[i][0], self.vals[i][1],
                self.vals[i][2], self.vals[i][3], self.vals[i][4]))
            print("---------------------")
        self.calcu()

    def menu(self):
        print("Menu:")


if __name__ == "__main__":
    main()
