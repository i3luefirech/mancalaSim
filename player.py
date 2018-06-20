import random

from gametree import GameTree


class Player:

    nextmove = None
    gametree = None

    ptype = 0

    tree = None

    game = None

    i = 0

    def __init__(self, ptype, mm):
        self.ptype = ptype
        if ptype > 0:
            print("create player minimax/alphabeta")
            self.tree = GameTree(mm)
        else:
            print("create player human")

    def setGame(self, game):
        self.game = game
        if self.ptype > 0:
            self.tree.createTree(game)

    def nextMove(self):
        print("calc next move")
        realmove = -1
        count = 0
        while realmove == -1 and count < self.game.fields:
            if 0 > self.i:
                print("to small move number")
                self.i = 0
            elif self.i >= (self.game.allfields / 2) - 1:
                print("to big move number")
                self.i = 0
            else:
                count += 1
                if self.game.allbeans[self.i] > 0:
                    realmove = self.i
                    print("found move: " + str(realmove))
                else:
                    print("no beans next")
                    self.i += 1
                    count += 1
        self.game.do_move(self, realmove)
        self.i += 1
