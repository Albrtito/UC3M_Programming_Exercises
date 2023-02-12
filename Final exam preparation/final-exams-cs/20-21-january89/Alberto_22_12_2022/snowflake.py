import random


class SnowFlake:
    def __init__(self, position_x: int, position_y: int, temperature: int):
        self.position_x = position_x
        self.position_y = position_y
        # For the private temperature -> Maybe it should be given by the street they are at
        self.__temperature = temperature

    # Properties and setters for position
    @property
    def position_x(self):
        return self.__position_x

    @position_x.setter
    def position_x(self, position_x):
        if position_x < 0:
            raise ValueError("Position_x must be bigger than 0")
        else:
            self.__position_x = position_x

    @property
    def position_y(self):
        return self.__position_y

    @position_y.setter
    def position_y(self, position_y):
        if position_y < 0:
            raise ValueError("position_y must be bigger than 0")
        else:
            self.__position_y = position_y

    # Melted property -> Read only
    @property
    def melted(self):
        if self.__temperature < 2:
            return False
        else:
            return True