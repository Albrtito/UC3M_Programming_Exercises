from snowflake import Snowflake

class Street:
    def __init__(self, horizontal: bool, starting_x: int, starting_y: int,
                 length: int, temperature: int):
        """ Creates a street object """
        self.horizontal = horizontal
        self.starting_x = starting_x
        self.starting_y = starting_y
        self.length = length
        self.temperature = temperature
        self.snowflakes = []

    def __str__(self):
        res = "Street "
        if self.horizontal:
            end = "(" + str(self.starting_x + self.length) + "," + str(
                self.starting_y) + ")"
            res += "H-"+str(self.starting_y)
        else:
            end = "(" + str(self.starting_x) + "," + str(self.starting_y +
                                                         self.length) + ")"
            res += "V-"+str(self.starting_x)
        res += ", it goes from (" +str(self.starting_x) + "," + str(
            self.starting_y) + ") to " + end + ". Temperature: " + str(
            self.temperature)
        return res

    def needs_cleaning(self)-> bool:
        """ Checks if the street must be cleaned"""
        if self.temperature >= 2:
            return False
        else:
            # Searching if any of the snowflakes share coordinates
            for index1 in range(len(self.snowflakes)):
                for index2 in range(index1 + 1, len(self.snowflakes)):
                    if (self.snowflakes[index1].x == self.snowflakes[index2].x
                            and self.snowflakes[index1].y ==
                            self.snowflakes[index2].y):
                        return True
            # If we are here, no snowflake shares coordinates
            return False