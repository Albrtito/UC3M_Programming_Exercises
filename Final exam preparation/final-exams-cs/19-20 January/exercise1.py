"""
A Warehouse Management System
Retail companies like Amazon are experimenting with the use of drones to deliver goods to their clients. This will
reduce the delivery costs and the time needed to do it. The purpose of this exercise is to simulate a warehouse
management system, where drones are used, according to the following description:

+ Each warehouse has a name, a series of drones, serves a given neighborhood and is able to receive orders.
+ A drone has an id, a current power (in the range 0 to 100), a status (available or busy) and can be used to
deliver an order (initially they have no order).
+ An order has a priority, an id and the address where it has to be delivered.
+ The map of the area has a name of the neighborhood and is a matrix where each element is either a string
representing the id of a house or ’s’ for positions where there are no houses (see example below)
+ For every order in the warehouse, a drone is selected to serve it. See below details about how drones are
selected.
Considering the above description, you are asked to:
"""

"""
1. (1pt) Define the needed classes and their init methods creating properties for all the attributes needing it.
Creating non-needed properties will be penalized.
"""
"""
Needed classes:
Class: Warehouse(name,drones,neighbourhood)
    self.name -> With setter and attribute
    self.drones -> With setter and attribute
    self.neighbourhood -> With setter and attribute
    Methods: Orders
Class: Drone(id, power, status)
    self.order = None
    self.status -> With setter and attribute
    self.power -> With setter and attribute
    self.id -> With setter and attribute

Class: Order (priority, id, address)
    self.priority -> With setter and attribute
    self.id -> With setter and attribute
    self.address -> With setter and attribute

Class: AreaMap (neighbourhood,map : matrix)
"""






