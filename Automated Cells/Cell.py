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
         is *_hygieneLevel*,deads is *deads* and actual health state is *actual_state*.
         Amount of deads are calculated in every iteration with formula which indepence
         on populaction in next iter. Self var Envorinment represent directive surroundings"""
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
        self.population = self.get_population() * self.map_rating()

    def calculate_mortality(self):  # %
        if self.get_population() is not 0:
            self.deads = 100 - ((float(self.get_population()) / float(self.get_start_population())) * 100)

    def set_state(self):
        ratio = self.get_deads()
        if ratio >= 0 and ratio < 20:
            self.actual_state = 1
            # Description: 'Healthy'
        elif ratio >= 20 and ratio < 40:
            self.actual_state = 2
            # Description 'Low'
        elif ratio >= 40 and ratio < 60:
            self.actual_state = 3
            # Description 'Middle'
        elif ratio >= 60 and ratio < 80:
            self.actual_state = 4
            # Description 'High'
        elif ratio >= 80 and ratio <= 100:
            self.actual_state = 5
            # Description 'Extinct'
        else:
            self.actual_state = 10
        pass

    def set_environment(self, surroundings):
        self.environment = surroundings

    def set_rating(self):
        sum = 25.0*float(self.environment) + 9.0 * 100.0 * float(self.pollution_level) + 7.0 * float(self.actual_state)
        self.rating = float((float(self.population) - sum) / float(self.start_population))
        if self.rating < 0.0:
            self.rating = 0.0

    def map_rating(self):
        actual_rating = self.get_rating()
        if actual_rating <= 1.0 and actual_rating >= 0.9:
            return 1.0
        elif actual_rating < 0.9 and actual_rating >= 0.6:
            return 0.75
        elif actual_rating < 0.6 and actual_rating >= 0.4:
            return 0.5
        elif actual_rating < 0.4 and actual_rating >= 0.15:
            return 0.25
        elif actual_rating < 0.15 and actual_rating >= 0.0:
            return 0.0
        else:
            return 10.0
