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
        self.environment = 0
        self.rating = 0.0

    ### Get Functions
    
    def get_rating(self):
        return self.rating

    def get_deads(self):
        return self.deads
    
    def get_population(self):
        return self.population

    def get_environment(self):
        return self.environment

    def get_start_population(self):
        return self.start_population

    def get_pollution_level(self):
        return self.pollution_level
       
    def get_actual_state(self):
        return self.actual_state
    
    ### Set Functions
    
    def calculate_population(self):
        if self.get_population() is not 0:
            self.population -= self.get_population() * self.get_pollution_level()
    #self.map_rating()
    def calculate_mortality(self):  # %
        if self.get_population() is not 0:
            self.deads = 100 - ((float(self.get_population()) / float(self.get_start_population())) * 100)

    def set_state(self):
        ratio = self.get_deads()
        if ratio >= 0 and ratio < 20:
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

    def set_environment(self, surroundings):
        self.environment = surroundings

    def set_rating(self):
        self.rating =  float(self.population) - (float(self.environment) + 3.0 * 100.0 * float(self.pollution_level) + 5.0 * float(self.actual_state ) )  / float(self.start_population) 
        #print('Pop ' +str(self.population))
        #print('Env ' + str(self.environment))
        #print('pll lvl ' + str(self.pollution_level))
        #print('act st '+ str(self.actual_state))
        #print('start pl ' + str(self.start_population))
        #print ('rat ' + str(self.rating))

    def map_rating(self):
        actual_rating = self.get_rating()
        if actual_rating <= 1.0 and actual_rating >= 0.90:
            return 1.0
        elif actual_rating < 0.9 and actual_rating >= 0.60:
            return 0.75
        elif actual_rating < 0.6 and actual_rating > 0.30:
            return (0.5)
        elif actual_rating < 0.30 and actual_rating > 0.15:
            return 0.25
        elif actual_rating < 0.15 and actual_rating > 0.0:
            return 0.0
        else:
            return 10.0
