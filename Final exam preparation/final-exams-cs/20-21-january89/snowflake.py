"""
@author: Angel Garcia Olaya. PLG-UC3M
@since: January 2020
@version: 1.0
"""
class Snowflake:
    """ This class represents a snowflake """
    def __init__(self, x: int, y: int, temperature: int):
        """ Creates a snowflake object """
        self.x = x
        self.y = y
        self.__temperature = temperature

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x: int):
        if x >= 0:
            self.__x = x
        else:
            self.__x = 0
            
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y: int):
        if y >= 0:
            self.__y = y
        else:
            self.__y = 0

    @property
    def melted(self):
        if self.__temperature >= 2:
            return True
        else:
            return False