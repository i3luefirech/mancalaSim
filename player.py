

class Player:

    nextmove = None
    gametree = None

    ptype = 0

    def __init__(self, ptype):
        self.ptype = ptype
        if ptype > 0:
            print("create player minimax/alphabeta")
        else:
            print("create player human")