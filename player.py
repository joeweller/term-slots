import os

class Player:
    def __init__(self, startfunds, spinval):
        self.account = startfunds
        self.spinval = spinval
        self.lines = 20
        self.spinc = 0  # spin count
        self.totalwon = 0  # total won
        self.totalbet = 0  # total bet
        self.highbank = startfunds  # highest bank point
        self.highwin = 0

    def checkplay(self):
        tmp = self.spinval * self.lines
        if self.account >= tmp:
            return 1
        else:
            return 0

    def get_spinval(self):
        return self.spinval

    def drawplayer(self):
        print("Bank: {0:.2f}".format(self.account))

    def update(self, won, winlines):
        self.account = self.account - (self.spinval * self.lines)
        self.account = self.account + won
        self.account = round(self.account, 2)
        self.spinc += 1
        self.totalwon = self.totalwon + won
        self.totalbet = self.totalbet + (self.spinval * self.lines)
        if self.highbank < self.account:
            self.highbank = self.account
        if self.highwin < won:
            self.highwin = won
        print("Won: {0:.2f}".format(won), end="")
        if winlines:
            print(" on {} lines".format(winlines))
        else:
            print("")
        self.drawplayer()

    def endreport(self):
        os.system("clear")
        print("Total Spins: {}".format(self.spinc))
        print("Total Won: {0:.2f}".format(self.totalwon))
        print("Total Bet: {0:.2f}".format(self.totalbet))
        print("Biggest Bank: {0:.2f}".format(self.highbank))
        print("Biggest Win: {0:.2f}".format(self.highwin))