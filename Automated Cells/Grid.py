from Cell import *
import random
import numpy as np
import time

class Grid:
    """description of class"""
        
    def __init__(self, size):
        """Return a Customer object Grid type, size of grid: size x size *."""

        self.size = size
        self.cells = [[Cell(random.uniform(0.0,1500.0), random.uniform(0.01, 0.10)) for _ in range(size)] for i in range(size)]
        self.states = np.zeros((size,size), dtype = 'int')
        self.mapped_states = [['' for _ in range(size)] for i in range(size)]
        self.cells_next_it = np.zeros((size,size), dtype = 'int')      

    ### GET functions

    def get_grid_size(self):
        return self.size

    def get_states_colors(self):
        return self.mapped_states
    
    def get_next_it_grid(self):
        return self.cells_next_it

    ### Performing next steps

    def perform_next_step(self,colors):
        for i in range(self.get_grid_size()):
            for j in range(self.get_grid_size()):
                self.cells[i][j].set_state()
                self.states[i][j] = self.cells[i][j].get_actual_state()
                self.mapped_states[i][j] = self.map_color(self.states[i][j],colors) #GUT
        #print (self.states)
        extended_states = np.pad(self.states, pad_width = 1, mode = 'constant', constant_values = 0)
        #print(extended_states)
        tab =np.zeros((self.get_grid_size(),self.get_grid_size()), dtype = 'int') 
        for i in range(self.get_grid_size()):
            for j in range(self.get_grid_size()):
                #start = time.time()
                #self.calculate_environment(extended_states, i, j)
                self.cells[i][j].calculate_population()
                self.cells[i][j].calculate_mortality()
                               
                tab[i][j]=self.cells[i][j].get_deads()
                #self.calculate_environment(i,j)
        print (self.states)

    def calculate_environment(self, extended_states, i, j):
        environment = 0
        for x in range(3):
            for y in range(3):
                if extended_states[i-1+x][j-1+y] > 1 and extended_states[i-1+x][j-1+y] < 5:
                    environment+=1 
        self.cells[i][j].set_environment(environment - int(extended_states[i][j] > 1 and extended_states[i][j] < 5))
        #print( 'environment: ' + str (environment - int(extended_states[i][j] > 1 and extended_states[i][j] < 5) ) )
        pass

    def map_color(self, actual_state,colors):        
        if actual_state == 0:
            return colors[0]
        elif actual_state == 1:
            return colors[1]
        elif actual_state == 2:
            return colors[2]
        elif actual_state == 3:
            return colors[3]
        elif actual_state == 4:
            return colors[4]
        elif actual_state == 5:
            return colors[5]
        else :
            return colors[6]

    def reload_grid(self):
        self.cells_next_it = np.zeros((self.size,self.size), dtype = 'int')  
        pass