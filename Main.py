from Puzzle import Board
import random
from Solver import Solver
import time

w = 4
h = 4

bi = Board(w, h)
print(bi.to_j())
bi.shuffle(50)
print('Shuffled\n')
print(bi.to_j())
print(bi)
# random.shuffle(bi)
# print(bi)
#
# print(len([13,14,6,2,12,5,8,10,4,9,1,15,7,3,11,0]),len([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]))
# s = Solver([16,17,5,1,3,4,2,10,6,8,13,9,7,12,0,14,11,15,18,19], w, h,sm='A*1',goal=[16,17,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0,18,19])
s = Solver(bi.board,w,h,sm='A*1')
t = time.time()
s.solve()
print(time.time()-t)
print('Solved')
s.printSol()

# s.goal.printBoard()
# random.shuffle(bd)
# print(bd)
#
# p = Board(bi,w,h)
# p.printBoard()
# p.getNextBoards()
