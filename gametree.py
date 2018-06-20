from copy import deepcopy
from datetime import datetime
from datetime import timedelta

from gamenode import GameNode


class GameTree:

    game = None

    root = None

    mm = 0

    start_time = 0

    def __init__(self, mm):
        print("create tree")
        self.mm = mm

    def millis(self):
        dt = datetime.now() - self.start_time
        ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
        return ms

    def createTree(self, game):
        depth = 5
        self.game = game
        print("create own game from original")
        self.start_time = datetime.now()
        self.root = GameNode(game, self.mm, None, -1, depth)
        # self.root = GameNode(deepcopy(game), self.mm, None, -1, depth)
        print("time to calc tree depth (" + str(depth) + ") in " + str(self.millis()) + " ms")
