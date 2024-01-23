import math


class Stats:


    def __init__(self, x1=0, x2=0):
        """Initializes."""
        self.x1 = x1
        self.x2 = x2
        self.__y = 0
        # Create the attributes here.

    def calc_stddev(self):
        """Calculates the standard deviation."""
        mean = (self.x1 + self.x2) / 2
        variance = (self.x1 - mean)**2 + (self.x2 - mean)**2
        self.__y = math.sqrt(variance)
        # Perform the calculation here. You'll want to use the math.sqrt() method.

    def display_result(self):
        """Displays standard deviation"""
        print(f"The standard deviation rounded to one decimal place is: {round(self.__y, 1)}") 
        return self.__y
        
