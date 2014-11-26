##!/usr/bin/env python3
#TestLife"."py
#Jeffrey Zhang and Esther Schenau


from unittest import main, TestCase
from Life import *

class TestLife (TestCase):
    


    #---------
    #Life Board
    #---------

    def test_life_place1(self):
        x = Life(2,2, "Conway")
        x.place(0,0,ConwayCell(1, "Conway"))
        self.assertEqual(x.matrix[0][0].status,1)
        self.assertEqual(x.matrix[0][0].str_type,"Conway")

    def test_life_place2(self):
        x = Life(2,2, "Conway")
        x.place(1,1,ConwayCell(0, "Conway"))
        self.assertEqual(x.matrix[0][0].status,0)
        self.assertEqual(x.matrix[1][1].str_type,"Conway")

    def test_life_place3(self): 
        x = Life(2,2, "Conway")
        x.place(1,0,ConwayCell(1, "Conway"))
        self.assertEqual(x.matrix[1][0].status,1)
        self.assertEqual(x.matrix[1][0].str_type,"Conway")
    
    def test_print_matrix1(self):
        x = Life(2,2, "Conway")
        x.place(1,1,ConwayCell(0, "Conway"))
        y = x.print_matrix()
        self.assertEqual(y,None)

    def test_int_matrix1(self): 
        x = Life(3,3,"Fredkin")
        x.place(0,0, FredkinCell(1, "Fredkin"))
        self.assertEqual(x.int_matrix, [[0,0,0],[0,0,0],[0,0,0]])

    #---------
    #Life Running
    #---------

    def test_run1(self):
        x = Life(3,3, "Conway")
        x.place(0,1,ConwayCell(0, "Conway"))
        x.place(1,1,ConwayCell(1, "Conway"))
        x.place(2,1,ConwayCell(1, "Conway"))
        x.place(2,2,ConwayCell(0, "Conway"))
        self.assertEqual(x.run(2, []),None)

    def test_run2(self):
        x = Life(5,5, "Conway")
        x.place(0,1,ConwayCell(0, "Conway"))
        x.place(1,1,ConwayCell(1, "Conway"))
        x.place(2,1,ConwayCell(1, "Conway"))
        x.place(2,2,ConwayCell(0, "Conway"))
        x.place(3,1,ConwayCell(1, "Conway"))
        x.place(4,2,ConwayCell(1, "Conway"))
        self.assertEqual(x.run(3, []),None)

    #---------
    #Life Live Neighbors
    #---------

    def test_life_live_neighbors(self):
        x = Life (2,2,"Conway")
        x.place (0,0, ConwayCell(0, "Conway"))
        x.place(0,1, ConwayCell(1, "Conway"))
        self.assertEqual (x.get_num_live_neighbors(0,1), 0)
    
    def test_life_live_neighbors2(self): 
        x = Life (2,2,"Conway")
        x.place (0,0, ConwayCell(0, "Conway"))
        x.place(0,1, ConwayCell(1, "Conway"))
        self.assertEqual (x.get_num_live_neighbors(1,1), 1)
    
    def test_life_live_neighbors3(self): 
        x = Life (4,4,"Conway")
        x.place (0,0, ConwayCell(1, "Conway"))
        x.place(0,2, ConwayCell(1, "Conway"))
        x.place(1,0, ConwayCell(1, "Conway"))
        self.assertEqual (x.get_num_live_neighbors(1,1), 3)

    def test_life_live_neightbors4(self):

        x = Life (8,8,"Conway")
        x.place(0,0, ConwayCell(1, "Conway"))
        x.place(0,1, ConwayCell(1, "Conway"))
        x.place(0,2, ConwayCell(1, "Conway"))
        x.place (0,3, ConwayCell(1, "Conway"))
        x.place(1,0, ConwayCell(1, "Conway"))
        x.place(1,1, ConwayCell(1, "Conway"))
        x.place (1,2, ConwayCell(1, "Conway"))
        x.place(1,3, ConwayCell(1, "Conway"))
        x.place(2,0, ConwayCell(1, "Conway"))
        x.place(2,1, ConwayCell(1, "Conway"))
        x.place (2,2, ConwayCell(1, "Conway"))
        x.place(2,3, ConwayCell(1, "Conway"))
        self.assertEqual (x.get_num_live_neighbors(1,1), 8)

    def test_life_live_neightbors5(self): 
        x = Life (8,8,"Conway")
        x.place(0,0, ConwayCell(1, "Conway"))
        x.place(0,1, ConwayCell(1, "Conway"))
        x.place(0,2, ConwayCell(1, "Conway"))
        x.place (0,3, ConwayCell(1, "Conway"))
        x.place(1,0, ConwayCell(1, "Conway"))
        x.place(1,1, ConwayCell(1, "Conway"))
        x.place (1,2, ConwayCell(1, "Conway"))
        x.place(1,3, ConwayCell(1, "Conway"))
        x.place(2,0, ConwayCell(1, "Conway"))
        x.place(2,1, ConwayCell(1, "Conway"))
        x.place (2,2, ConwayCell(1, "Conway"))
        x.place(2,3, ConwayCell(1, "Conway"))
        self.assertEqual (x.get_num_live_neighbors(0,0), 3)

    def test_life_live_neightbors6(self): 
        x = Life (8,8,"Conway")
        x.place(0,0, ConwayCell(1, "Conway"))
        x.place(0,1, ConwayCell(1, "Conway"))
        x.place(0,2, ConwayCell(1, "Conway"))
        x.place (0,3, ConwayCell(1, "Conway"))
        x.place(1,0, ConwayCell(1, "Conway"))
        x.place(1,1, ConwayCell(1, "Conway"))
        x.place (1,2, ConwayCell(1, "Conway"))
        x.place(1,3, ConwayCell(1, "Conway"))
        x.place(2,0, ConwayCell(1, "Conway"))
        x.place(2,1, ConwayCell(1, "Conway"))
        x.place (2,2, ConwayCell(1, "Conway"))
        x.place(2,3, ConwayCell(1, "Conway"))
        self.assertEqual (x.get_num_live_neighbors(1,0), 5)

    def test_run1 (self): 
        x = Life(2,2, "Conway")
        x.place(0,0,ConwayCell(1, "Conway"))
        x.place(0,1,ConwayCell(1, "Conway"))
        x.place(1,0,ConwayCell(1, "Conway"))
        x.run(3,[])
        self.assertEqual(x.population_count, 4)
  
    def test_run2 (self):
        x = Life(2,4, "Conway")
        x.place(0,0,ConwayCell(1, "Conway"))
        x.place(0,1,ConwayCell(1, "Conway"))
        x.place(0,3,ConwayCell(1, "Conway"))
        y = x.run(3,[3])
        self.assertEqual(x.population_count, 0)

    def test_run3 (self): 
        x = Life(4,5, "Conway")
        x.place(0,2,FredkinCell(1, "Fredkin"))
        x.place(0,1,FredkinCell(1, "Fredkin"))
        x.place(0,3,FredkinCell(1, "Fredkin"))
        x.place(0,0,FredkinCell(1, "Fredkin"))
        x.place(1,1,FredkinCell(1, "Fredkin"))
        x.print_matrix()
        x.run(20, [])
        self.assertEqual(x.population_count, 0)
  
main()
