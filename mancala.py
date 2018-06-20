import numbers
from tkinter import *
from game import GameModel
from player import Player

MAXPLAYER = 0
MINPLAYER = 1


class MancalaView:
    gamebeans = 4
    gamefields = 6
    gamewindow = None
    gamep1 = None
    gamep2 = None
    ui_p1 = None
    ui_p2 = None
    gamerefreshdelay = 50
    gamepadding = 20
    gameipadding = 10
    gamemodel = None

    first = TRUE

    def __init__(self):
        # create window for view
        self.gamewindow = Tk()
        self.gamewindow.title("MancalaSim")
        self.gamewindow.minsize(600, 200)

        # start refreshing view
        self.gamewindow.after(self.gamerefreshdelay, self.update_view)

    def on_p1click(self, idx):
        # if real player do click function
        if self.gamep1.ptype == 0:
            print("red p1 button move: " + str(idx))
            self.gamemodel.do_move(self.gamep1, idx)

    def on_p2click(self, idx):
        # if real player do click function
        if self.gamep2.ptype == 0:
            print("blue p2 button move: " + str(idx))
            self.gamemodel.do_move(self.gamep2, idx)

    def firstmove(self):
        if self.gamemodel.currentPlayer.ptype > 0:
            self.gamemodel.p1.nextMove()

    def create_view(self, beans, fields):
        self.gamebeans = beans
        self.gamefields = fields

        self.ui_p1 = []
        cnt = 0
        x = 0
        for x in range(0, fields):
            self.ui_p1.append(Button(self.gamewindow, text=str(beans), command=lambda idx=cnt: self.on_p1click(idx)))
            self.ui_p1[x].configure(bg="orange red", fg="black")
            self.ui_p1[x].grid(row=1, column=fields - x, pady=self.gamepadding,
                               padx=self.gamepadding, ipady=self.gameipadding, ipadx=self.gameipadding)
            cnt += 1
        self.ui_p1.append(Label(self.gamewindow, text="0"))
        self.ui_p1[fields].configure(bg="orange red", fg="black")
        self.ui_p1[fields].grid(row=3, column=fields - 1 - x, pady=self.gamepadding,
                                padx=self.gamepadding, ipady=self.gameipadding, ipadx=self.gameipadding)
        self.ui_p1.append(Label(self.gamewindow, text="P1"))
        self.ui_p1[fields + 1].configure(bg=self.gamewindow.cget('bg'), fg=self.gamewindow.cget('bg'))
        self.ui_p1[fields + 1].grid(row=1, column=fields - 1 - x, pady=self.gamepadding,
                                    padx=self.gamepadding, ipady=self.gameipadding, ipadx=self.gameipadding)

        self.ui_p2 = []
        cnt += 1
        for x in range(0, fields):
            self.ui_p2.append(Button(self.gamewindow, text=str(beans), command=lambda idx=cnt: self.on_p2click(idx)))
            self.ui_p2[x].configure(bg="blue", fg="white")
            self.ui_p2[x].grid(row=5, column=x + 1, pady=self.gamepadding,
                               padx=self.gamepadding, ipady=self.gameipadding, ipadx=self.gameipadding)
            cnt += 1
        self.ui_p2.append(Label(self.gamewindow, text="0"))
        self.ui_p2[fields].configure(bg="blue", fg="white")
        self.ui_p2[fields].grid(row=3, column=fields + 1, pady=self.gamepadding,
                                padx=self.gamepadding, ipady=self.gameipadding, ipadx=self.gameipadding)
        self.ui_p2.append(Label(self.gamewindow, text="P2"))
        self.ui_p2[fields + 1].configure(bg=self.gamewindow.cget('bg'), fg=self.gamewindow.cget('bg'))
        self.ui_p2[fields + 1].grid(row=5, column=fields + 1, pady=self.gamepadding,
                                padx=self.gamepadding, ipady=self.gameipadding, ipadx=self.gameipadding)

    def create_game(self, p1, p2):
        self.gamep1 = p1
        self.gamep2 = p2

        self.gamemodel = GameModel(self.gamebeans, self.gamefields, self.gamep1, self.gamep2)

        self.gamewindow.mainloop()

    def update_view(self):
        cnt = 0
        for x in self.ui_p1:
            if cnt <= self.gamefields:
                x.config(text=str(self.gamemodel.allbeans[cnt]))
            else:
                if self.gamemodel.currentPlayer == self.gamep1:
                    x.configure(bg="black", fg="orange red")
                else:
                    x.configure(bg=self.gamewindow.cget('bg'), fg=self.gamewindow.cget('bg'))
            cnt += 1

        cnt = 0
        for x in self.ui_p2:
            if cnt <= self.gamefields:
                x.config(text=str(self.gamemodel.allbeans[(self.gamefields + 1) + cnt]))
            else:
                if self.gamemodel.currentPlayer == self.gamep2:
                    x.configure(bg="white", fg="blue")
                else:
                    x.configure(bg=self.gamewindow.cget('bg'), fg=self.gamewindow.cget('bg'))
            cnt += 1

        if self.first:
            self.gamep1.setGame(self.gamemodel)
            self.gamep2.setGame(self.gamemodel)
            self.firstmove()
            self.first = FALSE

        self.gamewindow.after(self.gamerefreshdelay, self.update_view)


# create the game

mancalagame = MancalaView()
mancalagame.create_view(4, 6)

player1 = Player(1, MAXPLAYER)
player2 = Player(0, MINPLAYER)

mancalagame.create_game(player1, player2)
