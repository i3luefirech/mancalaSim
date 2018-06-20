import numbers


class GameModel:
    fields = 0
    allfields = 0
    startbeans = 0
    allbeans = []
    beans_start = 0
    beans_in = 0
    beans_out = 0

    currentPlayer = None
    p1 = None
    p2 = None

    def __init__(self, beans, fields, p1, p2):
        print("fields: " + str(fields))
        self.fields = fields
        self.allfields = (fields + 1) * 2
        self.startbeans = beans
        self.p1 = p1
        self.p2 = p2
        self.currentPlayer = self.p1
        self.beans_start = beans * fields * 2
        self.beans_in = self.beans_start
        self.beans_out = 0

        for x in range(0, self.allfields):
            if x == int(self.allfields / 2) - 1 or x == self.allfields - 1:
                self.allbeans.append(0)
            else:
                self.allbeans.append(self.startbeans)

    def do_move_p1(self, move):
        print("seed the beans from " + str(move))
        playbeans = self.allbeans[move]
        print("beans " + str(playbeans))
        self.allbeans[move] = 0
        index = move + 1
        while playbeans > 0:
            if self.allfields - 1 == index:
                index += 1
            if self.allfields == index:
                index = 0
            self.allbeans[index] += 1
            playbeans -= 1
            if playbeans == 0 and self.allbeans[index] == 1 and int(self.allfields / 2) - 1 != index:
                if 0 <= index < self.fields:
                    self.allbeans[int(self.allfields / 2) - 1] += 1
                    self.allbeans[index] = 0
                    # add values from vis a vis
                    diff = self.fields - index
                    wonbeans = self.allbeans[self.fields + diff]
                    self.allbeans[self.fields + diff] = 0
                    self.allbeans[int(self.allfields / 2) - 1] += wonbeans
            index += 1
        self.currentPlayer = self.p2
        if self.currentPlayer.ptype > 0:
            print("run bot next moves")
            self.p2.nextMove()

    def do_move_p2(self, move):
        print("seed the beans from " + str(move))
        playbeans = self.allbeans[move]
        print("beans " + str(playbeans))
        self.allbeans[move] = 0
        index = move + 1
        while playbeans > 0:
            if int(self.allfields / 2) - 1 == index:
                index += 1
            if self.allfields == index:
                index = 0
            self.allbeans[index] += 1
            playbeans -= 1
            if playbeans == 0 and self.allbeans[index] == 1 and self.allfields - 1 != index:
                if int(self.allfields / 2) <= index < self.allfields - 1:
                    self.allbeans[self.allfields - 1] += 1
                    self.allbeans[index] = 0
                    # add values from vis a vis
                    diff = self.allfields - 1 - index
                    print("diff " + str(diff))
                    wonbeans = self.allbeans[-1 + diff]
                    self.allbeans[-1 + diff] = 0
                    self.allbeans[self.allfields - 1] += wonbeans
            index += 1
        self.currentPlayer = self.p1
        print("test")
        if self.currentPlayer.ptype > 0:
            print("run bot next movew")
            self.p1.nextMove()

    def do_move(self, player, move):
        if self.currentPlayer == player:
            if player == self.p1:
                if 0 <= move < self.fields and self.allbeans[move] > 0:
                    self.do_move_p1(move)
                else:
                    print("not allowed!!!!")
            elif player == self.p2:
                if int(self.allfields / 2) <= move < self.allfields - 1 and self.allbeans[move] > 0:
                    self.do_move_p2(move)
                else:
                    print("not allowed!!!! ")
            else:
                print("unknown player")
        else:
            print("not your turn")

    def get_possiblemoves(self):
        moves_list = []

        if self.currentPlayer is self.p1:
            allbeans = self.allbeans
            for x in range(0, int(self.allfields / 2) - 1):
                if allbeans[x] > 0:
                    moves_list.append(x)

        if self.currentPlayer is self.p1:
            allbeans = self.allbeans
            for x in range(int(self.allfields / 2), self.allfields - 1):
                if allbeans[x] > 0:
                    moves_list.append(x)

        return moves_list
