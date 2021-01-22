import random
import time


# x =(int)(time.time())
# print(x)
random.seed(10000)


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
    previousMove = -1

    def __init__(self, width, height, board=None, previousID=None, stateID=1, gn=0, previousMove=-1, diff=0, goal=None, previousB=None):

        if board:
            self.board = board  # assigns array to board
        else:
            self.board = list(range(width * height))[1:] + [0]
        self.diff = diff
        self.goal = goal
        self.previousMove = previousMove
        # set width and height of board
        self.width = width
        self.height = height

        if previousID:
            self.previousID = previousID  # sets previous stateID

        self.gn = gn  # sets g(n) Default is 0 which would be the inital state

        self.stateID = stateID

        self.priorityValue = 0

        self.previousB = previousB

    def getNextBoards(self, nextID, shuffle=False):
        ind = self.board.index(0)
        x = (ind % self.width)
        y = ind // self.width
        # print(x, y)
        moves = []
        nextBoards = []
        if x != 0 and self.previousMove != 1:
            nextID += 1
            moves.append(0)
            newboard = self.board.copy()
            newboard[ind] = newboard[ind - 1]
            newboard[ind - 1] = 0
            b = Board(self.width, self.height, board=newboard, stateID=nextID, previousID=self.stateID, gn=self.gn + 1, previousMove=0, goal=self.goal, previousB=self)

            if not shuffle:
                new_diff = self.diff
                i = self.board[ind - 1]
                if i >= 10:
                    m = 2
                else:
                    m = 1
                x1, y1 = self.goal.getIndex(i)
                x2, y2 = self.getIndex(i)
                # subtract old tile position score
                new_diff -= (abs(x2 - x1) * m)
                new_diff -= (abs(y1 - y2) * m)
                # add new tile position score
                new_diff += (abs(x1 - x) * m)
                new_diff += (abs(y1 - y) * m)
                b.diff = new_diff
            nextBoards.append(b)
        else:
            nextBoards.append(None)

        if x != self.width - 1 and self.previousMove != 0:
            nextID += 1
            moves.append(2)
            newboard = self.board.copy()
            newboard[ind] = newboard[ind + 1]
            newboard[ind + 1] = 0
            b = Board(self.width, self.height, board=newboard, stateID=nextID, previousID=self.stateID, gn=self.gn + 1, previousMove=1, goal=self.goal, previousB=self)

            if not shuffle:
                new_diff = self.diff
                i = self.board[ind + 1]
                if i >= 10:
                    m = 2
                else:
                    m = 1
                x1, y1 = self.goal.getIndex(i)
                x2, y2 = self.getIndex(i)
                # subtract old tile position score
                new_diff -= (abs(x2 - x1) * m)
                new_diff -= (abs(y1 - y2) * m)
                # add new tile position score
                new_diff += (abs(x1 - x) * m)
                new_diff += (abs(y1 - y) * m)
                b.diff = new_diff

            nextBoards.append(b)
        else:
            nextBoards.append(None)

        if y != 0 and self.previousMove != 3:
            nextID += 1
            moves.append(1)
            newboard = self.board.copy()
            newboard[ind] = newboard[ind - self.width]
            newboard[ind - self.width] = 0
            b = Board(self.width, self.height, board=newboard, stateID=nextID, previousID=self.stateID, gn=self.gn + 1, previousMove=2, goal=self.goal, previousB=self)
            if not shuffle:
                new_diff = self.diff
                i = self.board[ind - self.width]
                if i >= 10:
                    m = 2
                else:
                    m = 1
                x1, y1 = self.goal.getIndex(i)
                x2, y2 = self.getIndex(i)
                # subtract old tile position score
                new_diff -= (abs(x2 - x1) * m)
                new_diff -= (abs(y1 - y2) * m)
                # add new tile position score
                new_diff += (abs(x1 - x) * m)
                new_diff += (abs(y1 - y) * m)
                b.diff = new_diff
            nextBoards.append(b)
        else:
            nextBoards.append(None)

        if y != self.height - 1 and self.previousMove != 2:
            nextID += 1
            moves.append(3)
            newboard = self.board.copy()
            newboard[ind] = newboard[ind + self.width]
            newboard[ind + self.width] = 0
            b = Board(self.width, self.height, board=newboard, stateID=nextID, previousID=self.stateID, gn=self.gn + 1, previousMove=3, goal=self.goal, previousB=self)
            if not shuffle:
                new_diff = self.diff
                i = self.board[ind + self.width]
                if i >= 10:
                    m = 2
                else:
                    m = 1
                x1, y1 = self.goal.getIndex(i)
                x2, y2 = self.getIndex(i)
                # subtract old tile position score
                new_diff -= (abs(x2 - x1) * m)
                new_diff -= (abs(y1 - y2) * m)
                # add new tile position score
                new_diff += (abs(x1 - x) * m)
                new_diff += (abs(y1 - y) * m)
                b.diff = new_diff
            nextBoards.append(b)
        else:
            nextBoards.append(None)

        return nextBoards, nextID

    def shuffle(self, x):
        boards = set()
        h = self
        p = -1
        for i in range(x):
            nextBoards, id = h.getNextBoards(0, shuffle=True)
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

        # print(len(boards))

    def getIndex(self, num, board=None):
        if board is not None:
            ind = board.index(num)
        else:
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
                # print(y,x,self.w*y+x)W
                ret += str(self.board[self.width * y + x]).rjust(c)
                if x < self.width - 1:
                    ret += ' '
            if y < self.height:
                ret += '\n'
        return ret

    def to_j(self):
        return ' '.join([str(x) for x in self.board])
