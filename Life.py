
#!/usr/bin/env/python3


#RunLife.py, Esther Schenau and Jeffrey Zhang
#Copyrighted 12 Nov 2014


class Life:
    '''
    creates the environment for cells
    analyzes neighboorhoods for cells
    '''
    def __init__(self, rows, cols, type_cell):
        '''
        intializes the Life environment
        '''
        assert rows >= 0
        assert cols >= 0
        self.rows = rows
        self.cols = cols
        self.population_count = 0
        self.int_matrix = [[0 for i in range (self.cols)] for j in range (self.rows)]
        if type_cell == "Conway": 
            self.matrix = [[ConwayCell(0, "Conway") for i in range (self.cols)] for j in range (self.rows)]
        elif type_cell =="Fredkin": 
            self.matrix = [[FredkinCell(0, "Fredkin") for i in range (self.cols)] for j in range (self.rows)]

        assert self.matrix != None

    def place (self, x,y,cell): 
        '''
        places a live cell on the board
        '''
        assert x >= 0
        assert y >= 0
        self.matrix[x][y]=cell
        if cell.status == 1: 
            self.population_count += 1
    
    #def print_int_matrix (self):
    #   '''
    #    used for debugging
    #    '''
    #    print()
    #    for i in self.int_matrix: 
    #        print ()
    #        for j in i: 
    #            print (j, end ="")
    #    print("\n\n")

    def print_matrix(self):
        '''
        visualization of the board
        '''
        assert self.matrix != None

        for i in self.matrix: 
            print ()
            for j in i:
                if j.str_type == "Conway":
                    if j.status == 1:
                        print("*", end = "")
                    else:
                        print(".",end = "")
                else:
                    if j.status == 1:
                        if j.age < 10:
                            print (j.age, end = "")
                        else:
                            print ("+", end = "")
                    else: 
                        print ("-", end = "" )
        print ()
        print ()


    def get_num_live_neighbors(self,i,j): 
        '''
        i is row, j is col in the matrix
        searching the neighborhood for live cells
        returns number of live neighbors
        '''
        assert self.matrix != None

        #check North south east west and increment number of live neighbors if live neighbor present
        # IF THE TYPE OF CELL is CONWAY: 
            #THEN CHECK DIAGONALS
        number_of_live_neighbors = 0

        x_pos_north = i - 1
        x_pos_south = i + 1
        y_pos_west = j - 1
        y_pos_east = j + 1
        x_pos_NW = i - 1
        y_pos_NW = j - 1
        x_pos_SW = i + 1
        y_pos_SW = j - 1
        x_pos_SE = i + 1
        y_pos_SE = j + 1
        x_pos_NE = i - 1
        y_pos_NE = j + 1

        # check north 
        if (x_pos_north >=0):
            if self.matrix[x_pos_north][j].status == 1:
                number_of_live_neighbors += 1
        #check west 
        if (y_pos_west >=0): 
            if self.matrix[i][y_pos_west].status == 1:
                number_of_live_neighbors +=1 
        #check south
        if ( x_pos_south < self.rows and x_pos_south >= 0) : 
            if self.matrix[x_pos_south][j].status ==1: 
                number_of_live_neighbors +=1 

        #check east
        if (y_pos_east < self.cols and y_pos_east > 0): 
            if self.matrix[i][y_pos_east].status == 1: 
                number_of_live_neighbors += 1

        if self.matrix[i][j].str_type == "Conway": 
            if (x_pos_NW >= 0 and x_pos_NW < self.rows and y_pos_NW >=0 and y_pos_NW <self.cols): 
                if self.matrix[x_pos_NW][y_pos_NW].status == 1: 
                    number_of_live_neighbors += 1 
            if (x_pos_SW >= 0 and x_pos_SW < self.rows and y_pos_SW >= 0 and y_pos_SW < self.cols): 
                if self.matrix[x_pos_SW][y_pos_SW].status == 1: 
                    number_of_live_neighbors += 1
            if (x_pos_SE >= 0 and x_pos_SE < self.rows and y_pos_SE >=0 and y_pos_SE <self.cols): 
                if self.matrix[x_pos_SE][y_pos_SE].status == 1: 
                    number_of_live_neighbors += 1

            if (x_pos_NE >= 0 and x_pos_NE < self.rows and y_pos_NE >=0 and y_pos_NE <self.cols): 
                if self.matrix[x_pos_NE][y_pos_NE].status == 1: 
                     number_of_live_neighbors += 1

        assert number_of_live_neighbors >= 0
        return number_of_live_neighbors


    # def analyze_neighborhood (self, ...): 
    #     pass

    def run (self,n, print_list): 
        
        '''
        function that computes the evolution from generation to generation
        after each evolution --> visualize matrix
        '''

        #Two Matrices  --- 1. Cell Matrix (no changing of the status), 2. Integer Matrix
        
        assert n!=0
        #Integer Matrix (we make our cell matrix when we placed)
        print ("Generation = %s, Population = %d." %(0, self.population_count), end = "")
        self.print_matrix()

        for num in range (1,n+1):

            #Creating Integer Matrix
            for i in range (self.rows): 
                for j in range (self.cols): 
                    cell = self.matrix[i][j]
                    cell.number_of_live_neighbors = self.get_num_live_neighbors(i,j)
                    self.int_matrix[i][j] = cell.number_of_live_neighbors 

            for i in range (self.rows): 
                for j in range (self.cols): 
                    cell = self.matrix[i][j]
                    if cell.str_type == "Conway": 
                        if self.int_matrix[i][j] == 3 and cell.status == 0: 
                            cell.status = 1
                            self.population_count += 1
                        elif (self.int_matrix[i][j] < 2 or self.int_matrix[i][j] > 3) and cell.status == 1: 
                            cell.status = 0
                            self.population_count -=1
                    else: 
                        #Fredkin Cells

                        #if dead to live cell
                        if cell.status == 0:
                            if self.int_matrix[i][j] == 3 or self.int_matrix[i][j] == 1: 
                                cell.status = 1
                                self.population_count += 1
                        #if cell is alive
                        elif cell.status == 1: 
                            if self.int_matrix[i][j] < 6 and self.int_matrix[i][j]%2 ==0:
                                cell.status = 0 
                                self.population_count -= 1
                            else: 
                                cell.age +=1 
                        
                        if cell.age == 2: 
                            self.matrix [i][j] = ConwayCell(1, "Conway")
                    
            assert self.population_count >= 0
                          
            if num in print_list:
                print ("Generation = %s, Population = %d." %(num, self.population_count), end = "")
                self.print_matrix()



class AbstractCell:
    '''
    common cell API for ConwayCell and FredkinCell
    status -- 1 = live, 0 = dead
    '''
    def __init__(self, status, str_type):

        self.status = status
        self.str_type = str_type
        self.number_of_live_neighbors = 0

class ConwayCell(AbstractCell):
    def __init__(self, status, str_type): 
        '''
        initiates a cell from parent class but with Conway rules
        '''
        AbstractCell.__init__(self, status, str_type)
   
class FredkinCell(AbstractCell): 
    def __init__(self, status, str_type): 
        '''
        initiates a cell from parent class with Fredkin rules
        '''
        AbstractCell.__init__(self, status, str_type)
        self.age = 0
