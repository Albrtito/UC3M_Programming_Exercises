from street import Street
from snowplow import Snowplow
from snowflake import Snowflake
import random


class City:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.streets = None
        self.snowplows = None
        
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height: int):
        if height >= 5:
            self.__height = height
        else:
            self.__height = 5

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        if width >= 5:
            self.__width = width
        else:
            self.__width = 5

    def create_streets(self):
        """ Creates the tuple of streets of the city"""
        # This list will be converted to a tuple at the end
        aux = []
        # Horizontal streets
        for s in range(self.height):
            temp = random.randint(-5, 4)
            length = random.randint(5,self.width)
            aux.append(Street(True, 0, s, length, temp))
        # Vertical streets
        for s in range(self.width):
            temp = random.randint(-5, 4)
            length = random.randint(5, self.height)
            aux.append(Street(False, s, 0, length, temp))

        self.streets = tuple(aux)

    def create_snowplows(self):
        """ Creates the snowplows of the city"""
        # This list will be converted to a tuple at the end
        aux = []
        for street in self.streets:
            x = street.starting_x
            y = street.starting_y
            fuel = random.randint(1, 20)
            aux.append(Snowplow(x, y, fuel))
        self.snowplows = tuple(aux)

    def snow(self, number: int):
        """ Makes it snow"""
        for counter in range(number):
            # Selecting the street
            street = self.streets[random.randrange(len(self.streets))]
            # Selecting a random position in the street
            pos = random.randrange(street.length)
            if street.horizontal:
                x = pos
                y = street.starting_y
            else:
                x = street.starting_x
                y = pos
            # Creating the snowflake
            sn = Snowflake(x, y, street.temperature)
            street.snowflakes.append(sn)

    def streets_to_clean(self)-> str:
        """ Returns the streets that need to be cleaned"""
        res = ""
        for street in self.streets:
            if street.needs_cleaning():
                res = res + str(street) + "\n"
        return res

    def clean_street(self):
        """ cleans the streets """
        for index in range(len(self.streets)):
            # Aux variable to make the code easier to understand
            street = self.streets[index]
            if street.needs_cleaning():
                # The first snowplow belongs to the 1st street and so on
                snowplow = self.snowplows[index]
                finish = False
                while not finish:
                    snowplow.fuel -= 1
                    # To avoid problems with the index, we start removing
                    # from the last element of the list
                    for ind in range(len(street.snowflakes) - 1, -1, -1):
                        if (street.snowflakes[ind].x == snowplow.x and
                                street.snowflakes[ind].y == snowplow.y):
                            del(street.snowflakes[ind])
                    if street.horizontal:
                        # If the street is horizontal, we move in x
                        snowplow.x = snowplow.x + 1
                        # If we reached the end of the street we finish
                        finish = snowplow.x > street.length
                    else:
                        # If it is vertical, we move in y
                        snowplow.y = snowplow.y + 1
                        finish = snowplow.y > street.length
                    # If it reached the end of the street or no fuel, finish
                    finish = finish or snowplow.fuel <= 0

