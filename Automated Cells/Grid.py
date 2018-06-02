from Cell import *
import random

class Grid:
    """description of class"""
        
    def __init__(self):
        """Return a Customer object whose population is *_population*, level of hygiene
         is *_hygieneLevel* and amount od infected people is *_infected*."""
        
        self.matrix = [[Cell(100, random.uniform(0.01, 0.10)) for _ in range(10)] for i in range(10)]
        

    def perform_next_step(self):
        for i in range(10):
            for j in range(10):
                self.matrix[i][j].calculate_pop()
                self.matrix[i][j].calculate_mortality()
                
