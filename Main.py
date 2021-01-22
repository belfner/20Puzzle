from Puzzle import Board
import random
from Solver import Solver
import time

w = 4
h = 4

bi = Board(w, h)
print(bi.to_j())
bi.shuffle(10)
print('Shuffled\n')
print(bi.to_j())
print(bi)
# random.shuffle(bi)
# print(bi)
#
# print(len([13,14,6,2,12,5,8,10,4,9,1,15,7,3,11,0]),len([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]))
s = Solver([1, 0, 7, 2, 5, 4, 6, 3, 9, 14, 11, 8, 10, 13, 15, 12], w, h, sm='A*1')
# s = Solver(bi.board,w,h,sm='A*1')
t = time.perf_counter()
s.solve()
print(time.perf_counter() - t)
print('Solved')
s.printSol()

# s.goal.printBoard()
# random.shuffle(bd)
# print(bd)
#
# p = Board(bi,w,h)
# p.printBoard()
# p.getNextBoards()
