from Cell import *
import random

class Grid:
    """description of class"""
        
    def __init__(self, size):
        """Return a Customer object Grid type, size of grid: size x size *."""

        self.size = size
        self.matrix = [[Cell(100, random.uniform(0.01, 0.10)) for _ in range(size)] for i in range(size)]
        

    def perform_next_step(self):
        for i in range(self.get_grid_size()):
            for j in range(self.get_grid_size()):
                self.matrix[i][j].calculate_population()
                self.matrix[i][j].calculate_mortality()
                
    def extend_area(self, size):
        pass


    def get_grid_size(self):
        return self.size
