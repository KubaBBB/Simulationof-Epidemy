from Cell import *
import random

class Grid:
    """description of class"""
        
    def __init__(self, size):
        """Return a Customer object Grid type, size of grid: size x size *."""

        self.size = size
        self.cells = [[Cell(random.uniform(0.0,1500.0), random.uniform(0.01, 0.10)) for _ in range(size)] for i in range(size)]
        self.states = [['' for _ in range(size)] for i in range(size)]

    def perform_next_step(self):
        for i in range(self.get_grid_size()):
            for j in range(self.get_grid_size()):
                self.cells[i][j].calculate_population()
                self.cells[i][j].calculate_mortality()
                self.states[i][j] = self.cells[i][j].get_plot_color()
                
    def extended_area(self, size):
        
        pass


    def get_grid_size(self):
        return self.size

    def get_states_colors(self):
        return self.states