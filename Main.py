from Puzzle import Board
import random
from Solver import Solver

w = 5
h = 2

bi = Board(w, h)
bi.shuffle(500)
print('Shuffled\n')
print(bi)
# random.shuffle(bi)
# print(bi)
#
# print(len([13,14,6,2,12,5,8,10,4,9,1,15,7,3,11,0]),len([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]))
# s = Solver([13,14,6,2,12,5,8,10,4,9,1,15,7,3,11,0], w, h,sm='A*1',goal=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0])
s = Solver(bi.board,w,h,sm='A*1')
s.solve()
print('Solved')
s.printSol()
# s.goal.printBoard()
# random.shuffle(bd)
# print(bd)
#
# p = Board(bi,w,h)
# p.printBoard()
# p.getNextBoards()
