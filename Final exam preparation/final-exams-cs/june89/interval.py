"""
Created by Angel Garcia Olaya
Date: 17/06/2022
Version: 1.0
"""

from generator import Generator

class Interval:
    def __init__(self, hour: int, demand: int):
        self.hour = hour
        self.demand = demand
        self.producers = []

    def __str__(self):
        result = "Hour: " + str(self.hour) + " Demand: " + str(
            self.demand) + "\n"
        for producer in self.producers:
            result += producer.name + " Offer: " + str(
                producer.offer[self.hour]) + " Price: " + \
                         str(round(producer.price, 2)) + "\n"
        return result