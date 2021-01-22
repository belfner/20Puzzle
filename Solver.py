from Puzzle import Board
import bisect
from sortedcontainers import SortedKeyList

class Solver:
    w = 0
    h = 0
    openList = SortedKeyList(key= lambda x:x.fn)
    openSet = set()
    closedList = []
    closedSet = set()
    start = None
    goal = None
    finalboard = None
    pathFound = False
    currID = 0
    path = []
    sol_len = 0


    def __init__(self, start, w, h, goal=None, sm='BrF'):
        self.w = w
        self.h = h
        self.sm = sm
        self.start = Board(w, h, board=start, stateID=self.currID) #set id of initial state to 0
        self.currID += 1  #itterate id for next batch of boards

        if goal:
            self.goal = Board(w, h, board=goal)
        else:
            self.goal = Board(w, h)

        self.start.diff = self.compareBoards(self.start,self.goal)
        self.start.goal = self.goal

        self.addToOpen(self.start) #adds initial state to openList
        # self.openSet.add(tuple(self.start.board))

    def compareBoards(self, b1, b2):
        diff = 0
        for i in range(1,self.w * self.h):
            x1, y1 = b1.getIndex(i)
            x2, y2 = b2.getIndex(i)
            if i >= 10:
                m = 2
            else:
                m = 1
            diff += (abs(x2 - x1)*m)
            diff += (abs(y1 - y2)*m)


        return diff

    def solve(self):
        while not self.pathFound:
            self.step()

    def step(self):
        if len(self.closedSet)%25000 == 0 and len(self.closedSet) != 0:
            print(f'Closed set size: {len(self.closedSet)}\nOpen list size: {len(self.openList)}')
            print()
        currentBoard = self.openList.pop(0) #gets highest priority state from openList and then removes it
        while tuple(currentBoard.board) in self.closedSet:
            currentBoard = self.openList.pop(0)
        # if currentBoard.board == [1, 0, 2, 3, 4, 5, 6, 7, 8]:
        #     x = 1
        # self.openSet.remove(tuple(currentBoard.board))
        nextBoards, newID = currentBoard.getNextBoards(self.currID)
        self.currID = newID
        for board in [b for b in nextBoards if b]: #gets all successor states from current state
            self.addToOpen(board) #runs add to open on each of the new states
        # self.openList.sort(key= lambda x: x.fn)
        self.closedList.append(currentBoard) #append the current state to the closed list
        self.closedSet.add(tuple(currentBoard.board))

    def calc_path(self):
        self.path = [self.finalboard]
        while self.path[-1].previousB is not None:
            self.path.append(self.path[-1].previousB)
        self.path = list(reversed(self.path))[:-1]
        self.sol_len = len(self.path)

    def printSol(self):
        print(f'Closed set size: {len(self.closedSet)}\nOpen list size: {len(self.openList)}')
        print()
        path = [self.finalboard]
        # for s in self.closedList:
        #     print(s.stateID)
        # while path[-1].previousID != -1:
        #     # print(path[-1].previousID)
        #     previousState = [s for s in self.closedList if s.stateID == path[-1].previousID][0]
        #     path.append(previousState)
        while path[-1].previousB is not None:
            path.append(path[-1].previousB)
        #
        # for b in reversed(path):
        #     print(b)

        self.sol_len = len(path)

    def insort(self, board):
        keyfunc = lambda x: x.fn
        # self.openList.append(board)
        # self.openList.sort(key=keyfunc)
        if len(self.openList) == 0:
            self.openList.append(board)
            return

        x = keyfunc(board)
        lo = 0
        hi = len(self.openList)
        while lo < hi:
            mid = (lo + hi) // 2
            if keyfunc(self.openList[mid]) <= x:
                lo = mid + 1
            else:
                hi = mid
        self.openList.insert(lo, board)

    def addToOpen(self, board): #checks for completion then checks all requirements for adding state to the open list

        if tuple(board.board) in self.closedSet or board in self.openList: # if the state is in the closed list then skip it
            return
        if self.sm == 'BrF':
            board.fn = board.gn
        elif self.sm == 'A*1':
            # d = self.compareBoards(board,self.goal)
            # if d != board.diff:
            #     x=0
            # board.fn = board.gn + self.compareBoards(board,self.goal)
            board.fn = board.gn + board.diff
        # if tuple(board.board) in self.openSet:
        #     if board.fn < self.openList[self.openList.index(board)].fn:
        #         self.openList.remove(self.openList[self.openList.index(board)])
        #         # self.openList.append(board)
        #         self.insort(board)
        if board == self.goal:
            self.pathFound = True
            self.finalboard = board
            return
        else:
            # self.openList.append(board)
            # self.insort(board)
            self.openList.add(board)
            # self.openSet.add(tuple(board.board))

