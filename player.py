import os

class Player:
    def __init__(self, spinval):
        self.account = 0
        self.spinval = spinval
        self.lines = 20
        self.spinc = 0  # spin count
        self.totalwon = 0  # total won
        self.totalbet = 0  # total bet
        self.highbank = 0
        self.highwin = 0

    def funds(self, funds):  # add funds to player
        self.account = funds
        self.highbank = self.account  # highest bank point


    def checkplay(self):
        tmp = self.spinval * self.lines
        if self.account >= tmp:
            return 1
        else:
            return 0

    def get_spinval(self):
        return self.spinval

    def drawplayer(self):
        return print("[ Bank: £{0:,.2f}   Stake: £{1:,.2f} ]".format(self.account, (self.spinval * self.lines) ))


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
        print("[ Won: {0:,.2f}".format(won), end="")
        if winlines:
            print(" on {} lines ]".format(winlines))
        else:
            print(" ]")
            #self.drawplayer()
        return

    def endreport(self):
        print("Total Spins: {}".format(self.spinc))
        print("Total Won: £{0:,.2f}".format(self.totalwon))
        print("Total Bet: £{0:,.2f}".format(self.totalbet))
        print("Biggest Bank: £{0:,.2f}".format(self.highbank))
        print("Biggest Win: £{0:,.2f}".format(self.highwin))