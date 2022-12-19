""" 
Created by Angel Garcia Olaya. PLG-UC3M
Since 2022/06/17
Version 1.0
"""

from generator import Generator
from interval import Interval
from daily_market import Daily_Market
import random

generators = []

for i in range(10):
    tipos = ("renovable", "gas", "nuclear")
    tipo = tipos[random.randrange(3)]
    generator = Generator("generator" + str(i), tipo)
    # We fix the gas price (the exam did not say how to do it)
    generator.create_offer(50)
    generators.append(generator)

market = Daily_Market(generators)
market.create_intervals()
market.select_generators()
print(market)
print()

for generator in market.generators:
    print(generator.name, "Profit:", round(generator.profit, 2))