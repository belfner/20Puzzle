import random

random.seed(10065423)

class Board:
    board = []
    width = 0
    height = 0
    previousID = -1
    stateID = -1
    gn = -1  # g(n)
    hn = -1  # h(n)
    fn = -1  # f(n)
    priorityValue = -1

    def __init__(self, width, height, board=None, previousID=None, stateID=1, gn=0):

        if board:
            self.board = board  # assigns array to board
        else:
            self.board = list(range(width * height))

        # set width and height of board
        self.width = width
        self.height = height

        if previousID:
            self.previousID = previousID  # sets previous stateID

        self.gn = gn  # sets g(n) Default is 0 which would be the inital state

        self.stateID = stateID

        self.priorityValue = 0

    def getNextBoards(self, nextID):
        ind = self.board.index(0)
        x = (ind % self.width)
        y = ind // self.width
        # print(x, y)
        moves = []
        nextBoards = []
        if x != 0:
            nextID += 1
            moves.append(0)
            newboard = self.board.copy()
            hold = newboard[ind - 1]
            newboard[ind - 1] = 0
            newboard[ind] = hold
            nextBoards.append(
                Board(self.width, self.height, board=newboard, stateID=nextID, previousID=self.stateID, gn=self.gn + 1))
        else:
            nextBoards.append(None)

        if x != self.width - 1:
            nextID += 1
            moves.append(2)
            newboard = self.board.copy()
            hold = newboard[ind + 1]
            newboard[ind + 1] = 0
            newboard[ind] = hold
            nextBoards.append(
                Board(self.width, self.height, board=newboard, stateID=nextID, previousID=self.stateID, gn=self.gn + 1))
        else:
            nextBoards.append(None)

        if y != 0:
            nextID += 1
            moves.append(1)
            newboard = self.board.copy()
            hold = newboard[ind - self.width]
            newboard[ind - self.width] = 0
            newboard[ind] = hold
            nextBoards.append(
                Board(self.width, self.height, board=newboard, stateID=nextID, previousID=self.stateID, gn=self.gn + 1))
        else:
            nextBoards.append(None)

        if y != self.height - 1:
            nextID += 1
            moves.append(3)
            newboard = self.board.copy()
            hold = newboard[ind + self.width]
            newboard[ind + self.width] = 0
            newboard[ind] = hold
            nextBoards.append(
                Board(self.width, self.height, board=newboard, stateID=nextID, previousID=self.stateID, gn=self.gn + 1))
        else:
            nextBoards.append(None)
        # for b in nextBoards:
        #     print()
        #     b.printBoard()

        return nextBoards, nextID

    def shuffle(self, x):
        boards = set()
        h = self
        p = -1
        for i in range(x):
            nextBoards, id = h.getNextBoards(0)
            n = random.randrange(4)

            while n == p or not nextBoards[n]:
                n = random.randrange(4)
            h = nextBoards[n]
            if n == 0:
                p = 1
            elif n == 1:
                p = 0
            elif n == 2:
                p = 3
            else:
                p = 2
            # print(n)
            boards.add(tuple(h.board))
        self.board = h.board

        print(len(boards))

    def getIndex(self, num):
        ind = self.board.index(num)
        x = (ind % self.width)
        y = ind // self.width
        return (x, y)

    def __eq__(self, other):
        if isinstance(other, Board):
            return self.board == other.board
        return False

    def __hash__(self):
        return hash(tuple(self.board))

    def __str__(self):
        ret = ''
        c = len(str(self.width * self.height - 1))
        for y in range(self.height):
            for x in range(self.width):
                # print(y,x,self.w*y+x)
                ret += str(self.board[self.width * y + x]).rjust(c)
                if x < self.width - 1:
                    ret += ' '
            if y < self.height:
                ret += '\n'
        return ret
