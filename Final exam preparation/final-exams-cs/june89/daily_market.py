"""
Created by Angel Garcia Olaya
Date: 17/06/2022
Version: 1.0
"""
import random
from interval import Interval
from generator import Generator


class Daily_Market:
    def __init__(self, generators):
        self.hours = []
        self.generators = generators

    @property
    def generators(self):
        return self.__generators

    @generators.setter
    def generators(self, generadores):
        if type(generadores) != list or len(generadores) == 0:
            raise TypeError("List cannot be empty")
        else:
            for generador in generadores:
                if type(generador) != Generator:
                    raise TypeError("Elements must be of type Generator")
        # If we are here, everything went well
        self.__generators = generadores

    def create_intervals(self):
        for hour in range(24):
            demand = random.randint(100, 200)
            interval = Interval(hour, demand)
            self.hours.append(interval)

    def sort_generators(self):
        lst = self.generators
        for i in range(len(lst) - 1):
            for j in range(0, len(lst) - 1 - i):
                if lst[j].price > lst[j + 1].price:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]


    def select_generators(self):
        # sorting generators
        self.sort_generators()
        for interval in self.hours:
            pending = interval.demand
            index = 0
            while pending > 0:
                current_gen = self.generators[index]
                pending -= current_gen.offer[interval.hour]
                interval.producers.append(current_gen)
                index = index + 1
            # The last one fixes the price
            hourly_price = interval.producers[-1].price
            for producer in interval.producers:
                producer.profit += producer.offer[interval.hour] * \
                                    hourly_price

    def __str__(self):
        result = ""
        for hora in self.hours:
            result += str(hora) + "\n"
        return result