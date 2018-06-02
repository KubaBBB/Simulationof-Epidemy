from enum import Enum

class Cell:
    """description of class"""

    # states of simple cell

    # 0-20% - Cell Healthy
    # 21-40% - The beginning of the epidemic development
    # 41-60% - Middle of the epidemic development
    # 61-80% - High Level of the epidemic developmnent
    # 81-100% - Extinction of the population in the cell
    #
    #HygieneLevel = Enum('Healthy', 'Low', 'Middle', 'High', 'Extinct')

    #_population = 0 # int - define amount of population in simple cell
     
    #_pollutionLevel = 1 # int - number from 1-10
      
    #_actualState = 0
    
    #_infected = 0 # int - amount of infected people => infected < population


    def __init__(self, population, pollutionLevel):
        """Return a Customer object whose population is *_population*, level of hygiene
         is *_hygieneLevel* and amount od infected people is *_infected*."""

        self.population = population
        self.pollution_level = pollutionLevel
        self.start_population = population
        self.deads = 0
        self.actual_state = 0

        ### Get Functions

    def get_population(self):
        return self.population
    
    def get_pollution_level(self):
        return self.pollution_level
    
    ### Set Functions

    def calculate_pop(self):
        self.population -= self.population * self.pollution_level
    
    def calculate_mortality(self):
        self.deads = 100 - ((float(self.population) / float(self.start_population)) * 100)

    def set_state(self):
        ratio = self.deads

        if ratio > 0 and ratio < 20:
            self.actual_state = 1
            #print 'Healthy'
        elif ratio > 21 and ratio < 40:
            self.actual_state = 2
            #print 'Low'
        elif ratio > 41 and ratio < 60:
            self.actual_state = 3
            #print 'Middle'
        elif ratio > 61 and ratio < 80:
            self.actual_state = 4
            #print 'High'return color 
        else :
            self.actual_state = 5
            #print 'Extinct'
        pass

    def get_plot_color(self):
        self.set_state()

        if self.actual_state == 0:
            return 'white'
        elif self.actual_state == 1:
            return 'green'
        elif self.actual_state == 2:
            return 'yellow'
        elif self.actual_state == 3:
            return 'orange'
        elif self.actual_state == 4:
            return 'red'
        elif self.actual_state == 5:
            return 'grey'
        else :
            return 'magenta'
