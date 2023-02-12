class Drone:
    def __init__(self, id: int, power: int, status: str):
        self.id = id
        self.power = power
        # The status will be inputted as a string but converted into a bool in the setter
        self.status = status
        # The order is an attribute of type Order:
        # No order initially
        self.order = None

    # Properties and setters

    # For id: Int, can be seen and edited
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        if type(id) != int:
            raise TypeError("Id must be an int")
        else:
            self.__id = id

    # For power: Int, can be seen and edited, must be in the range 0 to 100
    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        # If it is not an int -> Error
        if type(power) != int:
            raise TypeError("Power must be an int")
        # If it is not within the desired range -> Error
        if 0 > power or 100 < power:
            raise ValueError("Power must be within the range (0,100)")
        else:
            self.__power = power

    # For the status
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        # If the input is not a string -> Error
        if type(status) != str:
            raise TypeError("Status must be a string")
        # Convert the string into a bool value:
        if status == "available":
            status = True
        elif status == "busy":
            status = False
        else:
            raise ValueError("Status must be available or busy")
        self.__status = status

    # For the order: Is an object of class order, seen and edited
    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        if type(order) != Order:
            raise TypeError("Order must be an object of class order")
        else:
            self.__order = order

