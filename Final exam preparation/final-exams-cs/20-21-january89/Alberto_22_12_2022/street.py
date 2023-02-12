import random


class Street:
    def __init__(self, type: str, start_x:int, start_y:int, temperature: int, lenght: int):
        self.type = type
        self.start_x = start_x
        self.start_y = start_y
        self.temperature = temperature
        self.lenght = lenght

        # List for the snowflakes on this street
        self.snowflakes = []

    def needs_cleaning(self):
        """Returns a bool if a street needs cleaning"""
        countdown = 2

        for i in range(self.lenght):
            for j in range(len(self.snowflakes)):
                if self.snowflakes[j].position_x == i or self.snowflakes[j].position_x == i:
                    if not self.snowflakes[j].melted:
                        countdown -= 1

        if countdown == 0:
            return True
        else:
            return False

    def __str__(self):
        # This is now working only for horizontal streets
        return f"Street {self.type}-{self.start_y}, it goes from ({0},{self.start_y}) to ({self.lenght},{self.start_y})." \
               f"Temperature: {self.temperature} needs cleaning: {self.needs_cleaning()}, number of snowflakes:{len(self.snowflakes)}"

    def __repr__(self):
        """This method is invoked if I write the name of the object in
        the interpreter. It must
        15
        be called like this, no changes in name, no extra parameters.
        It must return the string I want to be shown"""
        # I just invoke the str
        return self.__str__()