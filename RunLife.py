#!/usr/bin/env/py_listthon3
#Esther Schenau and Jeffrey_list Zhang

from Life import *

#---------------------------------------
#*** Life<ConwayCell> 21x13 
#---------------------------------------
print ("*** Life<ConwayCell> 21x13 ***")
print()

x_list = [8,8,8,8,8,9,10,11,12,12,12,12,12]
y_list = [4,5,6,7,8,7,6,5,4,5,6,7,8]
assert len(x_list)==len(y_list)
life_board = Life(21,13,"Conway")
# add all the live cells on
z_list = zip(x_list,y_list)
for i,j in z_list:
    life_board.place(i,j,ConwayCell(1, "Conway"))
print_list =[0,1,2,3,4,5,6,7,8,9,10,11,12]
life_board.run(12, print_list)


#---------------------------------------
#*** Life<ConwayCell> 20x29 ***
#---------------------------------------



print ("*** Life<ConwayCell> 20x29 ***")
print ()

x_list = [3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 13]
y_list =  [3, 4, 3, 11, 12, 13, 20, 21, 22, 23, 4, 11, 21, 4, 5, 11, 12, 13, 20, 21, 22, 5]
assert len(x_list)==len(y_list)
life_board = Life(20,29,"Conway")
# add all the live cells on
z_list = zip(x_list,y_list)
for i,j in z_list:
    life_board.place(i,j,ConwayCell(1, "Conway"))
print_list2 = [0,4,8,12,16,20,24,28]
life_board.run(28, print_list2)


#---------------------------------------
#*** Life<ConwayCell> 109x69 ***
#---------------------------------------

print ("*** Life<ConwayCell> 109x69 ***")
print ()
x_list =  [34, 35, 36, 37, 38, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74]
y_list =  [34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34]
assert len(x_list)==len(y_list)
life_board = Life(109,69,"Conway")
# add all the live cells on
z_list = zip(x_list,y_list)
for i,j in z_list:
    life_board.place(i,j,ConwayCell(1, "Conway"))
print_list3 = [0,1,2,3,4,5,6,7,8,9,283,323,2500]
life_board.run(2500, print_list3)


#print_grids= [0,1,2,3,4,5,6,7,8, 9, 10, 11, 12] 
#life_board.run (5, print_grids)

#---------------------------------------
#*** Life<FredkinCell> 20x20 ***
#---------------------------------------
print ("*** Life<FredkinCell> 20x20 ***")
print ()
x_list =  [9, 9, 10, 10]
y_list =  [9, 10, 9, 10]
assert len(x_list)==len(y_list)
life_board = Life(20,20, "Fredkin")
# add all the live cells on
z_list = zip(x_list,y_list)
for i,j in z_list:
    life_board.place(i,j,FredkinCell(1, "Fredkin"))
print_list4 = [0,1,2,3,4,5]
life_board.run(5, print_list4)
