class Person:
    def __init__(self, name: str, age: int, dni: int, gender: str, weight: float, height: float):
        self.name = name
        self.age = age
        self.dni = dni
        self.gender = gender
        self.weight = weight
        self.height = height
        self.dniLetter

    # Properties and setters
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if type(name) != str:
            raise TypeError("Name type must be a string")
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        if type(age) != int:
            raise TypeError("Age type must be an int")
        self.__age = age

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni: int):
        if type(dni) != int:
            raise TypeError("DNI type must be an int")
        dni_str = str(dni)
        if len(dni_str) > 8 or len(dni_str) < 1:
            raise ValueError("Len of dni is not valid: Must be between 1 and 8")
        self.__dni = dni
        self.dniLetter = self.__calculateDniLetter()
    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        if type(gender) != str:
            raise TypeError("Gender type must be a str")
        # if (type(gender) != "male") or (type(gender) != "female"):
        # raise ValueError("Gender must be male of female")
        else:
            self.__gender = gender

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        if type(weight) != float:
            raise TypeError("Weight must be a float")
        self.__weight = weight

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: float):
        if type(height) != float:
            raise TypeError("Height must be a float")
        self.__height = height

    """__calculateDniLetter(): Calculates the DNI letter based on the dni field
    value, and stores this letter into the dniLetter field.
    """

    def __calculateDniLetter(self):
        if self.dni % 2 == 0:
            return "L"
        else:
            return "M"

    """
    __str__(): Returns a String to print on screen the fields in the following
    format:
    Person Information:
    Name: Pepe
    Sex: Male
    Age: 46 years old
    DNI: 821946-H
    Weight: 80.0 kg
    Height: 177.0 cm
    
    """

    def __str__(self):
        return " Name: " + self.name + "\n Sex: " + self.gender + "\n Age: " + str(
            self.age) + " years old" + "\n DNI: " + str(self.dni) + "-" + self.dniLetter + "\n Weight: " + str(self.weight) + "kg" + "\n Height: " + str(self.height )+ "cm"


person1 = Person("Alberto", 22, 3455, "male", 57.0, 16.0)
print(person1)
