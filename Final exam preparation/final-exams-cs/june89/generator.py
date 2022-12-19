"""
Created by Angel Garcia Olaya
Date: 17/06/2022
Version: 1.0
"""

import random

class Generator:
    def __init__(self, name: str, tipo: str):
        self.name = name
        self.kind = tipo
        self.offer = []
        self.price = 0.0
        self.profit = 0.0

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, tipo):
        if type(tipo) != str:
            raise TypeError("Kind must be a str")
        elif tipo.lower() not in ("renovable", "gas", "nuclear"):
            raise ValueError ("Valid kinds are renovable, gas and nuclear")
        else:
            self.__kind = tipo.lower()

    def create_offer(self, gas_price: int):
        for hour in range(24):
            self.offer.append(random.randint(10, 100))
        if self.kind == 'renovable' or self.kind == "nuclear":
            self.price = random.uniform(0, 30)
        else:
            self.price = random.uniform(gas_price, gas_price * 2)
