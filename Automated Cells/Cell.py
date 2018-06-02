from enum import Enum

class Cell:
    """description of class"""

    # states of simple cell

    # 0-20% - Cell Healthy
    # 21-40% - The beginning of the epidemic development
    # 41-60% - Middle of the epidemic development
    # 61-80% - High Level of the epidemic developmnent
    # 81-100% - Extinction of the population in the cell


    def __init__(self, population, pollutionLevel):
        """Return a Customer object whose population is *population*, level of hygiene
         is *_hygieneLevel*,deads is *deads* and actul health state is *actual_state*."""

        self.population = population
        self.pollution_level = pollutionLevel
        self.start_population = population
        self.deads = 0
        self.actual_state = 0


    ### Get Functions


    def get_deads(self):
        return self.deads
    
    def get_population(self):
        return self.population
    
    def get_start_population(self):
        return self.start_population

    def get_pollution_level(self):
        return self.pollution_level
        
    def get_plot_color(self):
        self.set_state()

        if self.actual_state is 0:
            return 'white'
        elif self.actual_state is 1:
            return 'green'
        elif self.actual_state is 2:
            return 'yellow'
        elif self.actual_state is 3:
            return 'orange'
        elif self.actual_state is 4:
            return 'red'
        elif self.actual_state is 5:
            return 'grey'
        else :
            return 'magenta'
    

    ### Set Functions


    def calculate_population(self):
        if self.get_population() is not 0:
            self.population -= self.get_population() * self.get_pollution_level()
    
    def calculate_mortality(self):
        if self.get_population() is not 0:
            self.deads = 100 - ((float(self.get_population()) / float(self.get_start_population())) * 100)

    def set_state(self):
        ratio = self.get_deads()

        if ratio > 0 and ratio < 20:
            self.actual_state = 1
            # Description: 'Healthy'
        elif ratio > 21 and ratio < 40:
            self.actual_state = 2
            # Description 'Low'
        elif ratio > 41 and ratio < 60:
            self.actual_state = 3
            # Description 'Middle'
        elif ratio > 61 and ratio < 80:
            self.actual_state = 4
            # Description 'High' 
        else :
            self.actual_state = 5
            # Description 'Extinct'
        pass

