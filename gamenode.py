from copy import deepcopy


class GameNode:

    parent = None
    children = []

    game = None

    move = -1

    p1score = 0
    p2score = 0
    diff = 0
    bad_moves = 0
    mm = 0  # 0 = max, 1 = min
    depth = 5

    def __init__(self, game, mm, parent, move, depth):
        self.parent = parent
        self.game = game
        self.mm = mm
        self.move = move
        self.depth = depth

        for x in range(0, self.game.allfields):
            if x is (self.game.allfields / 2) - 1:
                self.p1score = self.game.allbeans[x]
            if x is self.game.allfields - 1:
                self.p2score = self.game.allbeans[x]

        if self.mm == 0:
            self.diff = self.p1score - self.p2score
        else:
            self.diff = self.p2score - self.p1score

        self.bad_moves = 0

        if self.depth > 0:
            for x in game.get_possiblemoves():
                self.children.append(GameNode(game, self.mm, self, x, self.depth-1))
                # self.children.append(GameNode(deepcopy(game), self.mm, self, x, self.depth-1))

