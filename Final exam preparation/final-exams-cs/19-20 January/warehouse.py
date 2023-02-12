from drone import Drone
from order import Order
from map import Map


class Warehouse:
    def __init__(self, name: str, drone_number: list, neighbourhood: str):
        self.name = name
        self.drone_number = drone_number
        self.neighbourhood = neighbourhood

        # The list of drones of the warehouse, created by a method:
        self.drone_list = self.create_drones(drone_number)
        # The list of orders coming in:
        self.orders = []

        # Objects needed
        self.map = Map(self.neighbourhood, [])

    # properties and setters

    # For name variable: Must be a str, can be seen and edited
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) != str:
            raise TypeError("Name must be a str")
        else:
            self.__name = name

    # For drones: List, can be seen and edited

    @property
    def drone_number(self):
        return self.drone_number

    @drone_number.setter
    def drone_number(self, drone_number):
        if type(drone_number) != list:
            raise TypeError("Drones must be a list")
        else:
            self.drone_number = drone_number

    # For neighbourhood: Str, can be seen and edited

    @property
    def neighbourhood(self):
        return self.__neighbourhood

    @neighbourhood.setter
    def neighbourhood(self, neighbourhood):
        if type(neighbourhood) != str:
            raise TypeError("Name must be a str")
        else:
            self.__neighbourhood = neighbourhood

    # METHODS OF THE WAREHOUSE CLASS

    def create_drones(self, drone_number):
        drone_list = []
        for i in range(drone_number):
            drone_list.append(Drone(f"drone{i}"))
        return drone_list

    # Creates the list of orders, it creates this list ordered
    def insert_order_in_list(self, order: Order):
        # If the list is not empty we can add normally
        if len(self.orders) != 0:
            insert_index = len(self.orders)
        # If it is empty, we add at index 0: Add the first element
        else:
            insert_index = 0
        # We check for every element in the list of orders: We start at the end, if the element to the left is smaller
        # (priority) than the one we are comparing, we move the one comparing one to the left. We do that until there
        # are no smaller priority orders
        for i in range(len(self.orders)):
            if self.orders[insert_index - 1].priority < order.priority:
                insert_index -= 1
        # When we finish changing the index, we insert the order into the list
        self.orders.insert(insert_index, order)

    # Returns a tuple with a drone id suited for the address specified and the distance to that address
    def pick_drone(self, order_address: str):
        # Choose the drone for the order_address
        # The fist available one is chosen by looking at the list from start to finish
        for i in range(len(self.drone_list)):
            if self.drone_list[i].power == 2 * self.map.compute_distance(self.name, order_address):
                return_tuple = (self.drone_list[i].id, self.map.compute_distance((self.name, order_address)))
                return return_tuple

        # Else we charge the drone to it`s max power
        self.drone_list[0].power = 100
        # We create a different return dictionary and return it
        return_tuple = (self.drone_list[0].id, self.map.compute_distance((self.name, order_address)))

        return return_tuple

    def process_order(self, order):
        self.orders.append(order)
        for i in range(len(self.drone_list)):
            if self.drone_list[i].id == self.pick_drone(order.address)[0]:
                drone = self.drone_list[i]
                drone.status = "busy"
                drone.order = order
            else:
                print("No drone with the id required")
