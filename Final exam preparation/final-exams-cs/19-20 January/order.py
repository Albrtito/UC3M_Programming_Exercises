class Order:
    def __init__(self, priority: int, id: int, address: str):
        self.priority = priority
        self.id = id
        self.address = address

    # Properties and setters

    # For priority: Int, can be seen and edited
    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        if type(priority) != int:
            raise TypeError("priority must be an int")
        else:
            self.__priority = priority

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

    # For address: Str, seen and edited
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if type(address) != str:
            raise TypeError("Address must be a str")
        else:
            self.__address = address