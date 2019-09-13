from Puzzle import Board
import bisect

class Solver:
    w = 0
    h = 0
    openList = []
    openSet = set()
    closedList = []
    closedSet = set()
    start = None
    goal = None
    finalboard = None
    pathFound = False
    currID = 0

    def __init__(self, start, w, h, goal=None, sm='BrF'):
        self.w = w
        self.h = h
        self.sm = sm
        self.start = Board(w, h, board=start, stateID=self.currID) #set id of initial state to 0
        self.currID += 1 #itterate id for next batch of boards

        if goal:
            self.goal = Board(w, h, board=goal)
        else:
            self.goal = Board(w, h)

        self.addToOpen(self.start) #adds initial state to openList
        self.openSet.add(tuple(self.start.board))

    def compareBoards(self, b1, b2):
        diff = 0
        for i in range(self.w * self.h):
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
        currentBoard = self.openList.pop(0) #gets highest priority state from openList and then removes it
        # if currentBoard.board == [1, 0, 2, 3, 4, 5, 6, 7, 8]:
        #     x = 1
        self.openSet.remove(tuple(currentBoard.board))
        nextBoards, newID = currentBoard.getNextBoards(self.currID)
        self.currID = newID
        for board in [b for b in nextBoards if b]: #gets all successor states from current state
            self.addToOpen(board) #runs add to open on each of the new states
        # self.openList.sort(key= lambda x: x.fn)
        self.closedList.append(currentBoard) #append the current state to the closed list
        self.closedSet.add(tuple(currentBoard.board))

    def printSol(self):
        print(len(self.openList))
        print(len(self.closedList))
        print()
        path = [self.finalboard]
        # for s in self.closedList:
        #     print(s.stateID)
        while path[-1].previousID != -1:
            # print(path[-1].previousID)
            previousState = [s for s in self.closedList if s.stateID == path[-1].previousID][0]
            path.append(previousState)
        #
        for b in reversed(path):
            print(b)

        print(len(path))

    def insort(self, board):
        if len(self.openList) == 0:
            self.openList.append(board)
            return
        keyfunc = lambda x: x.fn
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

        if tuple(board.board) in self.closedSet: # if the state is in the closed list then skip it
            return
        if self.sm == 'BrF':
            board.fn = board.gn
        elif self.sm == 'A*1':
            board.fn = board.gn + self.compareBoards(board,self.goal)
        if tuple(board.board) in self.openSet:
            if board.fn < self.openList[self.openList.index(board)].fn:
                self.openList.remove(self.openList[self.openList.index(board)])
                # self.openList.append(board)
                self.insort(board)
        elif board == self.goal:
            self.pathFound = True
            self.finalboard = board;
            return
        else:
            # self.openList.append(board)
            self.insort(board)
            self.openSet.add(tuple(board.board))

