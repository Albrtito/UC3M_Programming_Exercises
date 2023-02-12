import random
from street import Street
from snowplow import SnowPlow
from snowflake import SnowFlake
class City:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

        # List needed
        self.streets = None
        self.snowplows = None

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if width <= 5:
            raise ValueError("Value error for width")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height <= 5:
            raise ValueError("Height of the city must be bigger than 5")
        else:
            self.__height = height

    # METHODS FOR CITY
    def create_streets(self):
        """Create horizontal and vertical streets"""
        # create a list to then turn into a tuple
        streets = []
        # Create a blank matrix with the right magnitude
        for x in range(self.height):
            streets.append([])
            for y in range(self.width):
                streets[x].append(0)
        # create horizontal streets
        for i in range(self.height):
            random_lenght = random.randint(5, self.height)
            random_temperature = random.randint(-5, 4)
            streets[0][i] = Street("H", 0, i, random_temperature, random_lenght)
        # create vertical streets
        for i in range(self.width):
            random_lenght = random.randint(5, self.width)
            random_temperature = random.randint(-5, 4)
            streets[i][0] = Street("V", i, 0, random_temperature, random_lenght)
        # Set the street tuple
        self.streets = tuple(streets)

    def create_snowplows(self):
        """Create the snowplows: One at the beginning of each street. Check the street matrix for values different
        from 0"""
        # list to then turn into tuple
        snowplows = []
        # Create a blank matrix with the right magnitude
        for x in range(self.height):
            snowplows.append([])
            for y in range(self.width):
                snowplows[x].append(0)
        # Check the streets matrix
        for x in range(self.height):
            for y in range(self.width):
                if self.streets[x][y] != 0:
                    snowplows [x][y] = SnowPlow(x,y,random.randint(1,20))

        self.snowplows = tuple(snowplows)

    def create_snow(self,number):
        while number > 0:
            # Check the streets matrix
            for x in range(self.height):
                for y in range(self.width):
                    # If we create a snowflake in this position, can be true or false and the position is not a 0. Then
                    # we can create a snowflake, the number of snowflakes is reduced and the snowflake is created at the
                    # end of the street with it`s temperature
                    if random.randint(0,1) and self.streets[x][y] != 0:
                        number -= 1
                        if self.streets[x][y].type == "H":
                            self.streets[x][y].snowflakes.append(SnowFlake(self.width,y,self.streets[x][y].temperature))
                        if self.streets[x][y].type == "V":
                            self.streets[x][y].snowflakes.append(SnowFlake(x,self.height, self.streets[x][y].temperature))

    def streets_to_clean(self):
        streets_to_clean_str = f"Streets to clean:" \
                               f""
        for i in range(new_city.height):
            for y in range(new_city.width):
                if new_city.streets[i][y] != 0:
                    if self.streets[i][y].needs_cleaning():
                        streets_to_clean_str = streets_to_clean_str + "/n" + str(self.streets[i][y])

        return streets_to_clean_str




new_city = City(12, 12)
new_city.create_streets()
new_city.create_snowplows()
new_city.create_snow(23)

"""
print(new_city.snowplows)
for i in range(new_city.height):
    for y in range(new_city.width):
        if new_city.streets[i][y] != 0:
            print(new_city.streets[i][y].snowflakes)
"""
for i in range(new_city.height):
    for y in range(new_city.width):
        if new_city.streets[i][y] != 0:
            print(new_city.streets[i][y])

print(f"The streets toclean are:"
      f"{new_city.streets_to_clean()}")