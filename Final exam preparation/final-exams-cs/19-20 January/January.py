import random

# We use a single module for all the classes for simplicity but it is
# recommended to create a module for each class plus one for the main program


class Drone:
    """ A class to represent a drone """

    def __init__(self, idD, power):
        self.idD = idD
        self.power = power
        self.status = 'available'
        self.order = None

    def __str__(self):
        """ Not asked but used to check code is running properly"""
        return ('Drone ' + self.idD + ' with power ' + str(self.power) +
                ' status ' + self.status + ' and order ' + str(self.order))

    # We create properties for power and status, we could also check the types
    # of id or order, but this was enough for the exam
    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, v):
        if v >= 0 and v <= 100:
            self.__power = v
        else:
            self.__power = 0

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, v):
        if v.lower() == 'available' or v.lower() == 'busy':
            self.__status = v
        else:
            self.__status = 'available'


class Order:
    """ A class to represent an order """

    def __init__(self, idO, p, address):
        self.idO = idO
        self.address = address
        self.priority = p

    def __str__(self):
        """ Not asked but used to check code is running properly"""
        return ('Order ' + self.idO + ' with priority ' + str(self.priority)
                + ' and address ' + self.address)


class AreaMap:
    """ Class to represent the map of an area, in addition to attributes it
    will have some methods """

    def __init__(self, whId, rows, columns, houses):
        # The only attribute will be the area map (we could have also rows,
        # columns, etc. but they can be extracted from the map, so we don't
        # repeat information)
        self.areaMap = self.createAreaMap(whId, rows, columns, houses)

    def createAreaMap(self, whId, rows, columns, houses):
        """ Creates the map of the area, addding houses and the warehouse
        position """
        areaMap = []
        # At the beginning everything is street
        for _ in range(rows):
            row = []
            for _ in range(columns):
                row.append('s')
            areaMap.append(row)
        # We randomly set the warehouse
        areaMap[random.randrange(rows)][random.randrange(columns)] = whId
        # Now the houses
        count = 1
        while count <= houses:
            r = random.randrange(rows)
            c = random.randrange(columns)
            if 's' in areaMap[r][c]:
                areaMap[r][c] = 'h' + str(count)
                count += 1
        return areaMap

    def printMap(self):
        """ Not asked but used to check code is running properly"""
        for i in self.areaMap:
            print(i)

    def computeDistance(self, warehouse, address):
        """ Computes the distance between the warehouse and a house """
        i, foundW, foundH = 0, False, False
        while i < len(self.areaMap) and (not foundW or not foundH):
            j = 0
            while j < len(self.areaMap[i]) and (not foundW or not foundH):
                if self.areaMap[i][j] == warehouse and not foundW:
                    w = (i, j)
                    foundW = True
                elif self.areaMap[i][j] == address and not foundH:
                    h = (i, j)
                    foundH = True
                j += 1
            i += 1
        d = ((w[0] - h[0]) ** 2 + (w[1] - h[1]) ** 2) ** 0.5
        return d


class Warehouse:
    """ Class to represent the warehouse, most methods are here """

    def __init__(self, name, drones, nRows, nColumns, nHouses):
        self.name = name
        self.drones = self.createDrones(drones)
        self.orders = []
        self.areaMap = AreaMap(name, nRows, nColumns, nHouses)

    def createDrones(self, n):
        """ Creates a list of drone objects """
        drones = []
        for i in range(0, n):
            drones.append(Drone('drone' + str(i + 1), random.randint(0, 100)))
        return drones

    def insertOrderinList(self, ord: Order):
        """ Inserts an order in the list of orders """
        count, found = 0, False
        while not found and count < len(self.orders):
            if self.orders[count].priority < ord.priority:
                found = True
            else:
                count += 1
        self.orders.insert(count, ord)

    def pickDrone(self, address):
        """ Picks a drone to process an order """
        d, maxValue, indexMaxValue, found, index = 0, 0, -1, False, None
        distance = self.areaMap.computeDistance(self.name, address) * 2
        while not found and d < len(self.drones):
            # We are going to consider only available drones
            if self.drones[d].status == 'available':
                if self.drones[d].power >= distance:
                    found = True
                    index = d
                # We consider this drone in case none has power enough
                elif maxValue < self.drones[d].power:
                    maxValue = self.drones[d].power
                    indexMaxValue = d
            d += 1
        # If none has enough power we recharge the one with maximum power
        if not found:
            if indexMaxValue != - 1:
                self.drones[indexMaxValue].power = 100
                index = indexMaxValue
        # It no one meets the requirements we will return None and distance
        return index, distance

    def processOrder(self, order):
        """ Processes the order """
        self.insertOrderinList(order)
        index, distance = self.pickDrone(order.address)
        if index is not None:
            self.drones[index].order = order
            self.drones[index].power -= distance
            self.drones[index].status = 'busy'
            print(order, 'processed by drone', self.drones[index].idD)
        else:
            print('Unable to process the order %s: all drones are busy'
                  % order.idO)


# main program

name = input('warehouse name? ')
drones = int(input('drones? '))
rowMap = int(input('rows? '))
colMap = int(input('columns? '))
houses = int(input('houses? '))

# Creating the warehouse
w = Warehouse(name, drones, rowMap, colMap, houses)
# Creating the orders
for i in range(5):
    address = 'h' + str(random.randint(1, houses))
    w.processOrder(Order('id' + str(i), random.randint(1, 10), address))
