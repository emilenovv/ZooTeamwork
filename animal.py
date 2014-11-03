import random
from zoo import Zoo


class Animal:
    life_expectancy = 50

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight

    def grow(self, ages, weight):
        self.weight += weight
        self.age += ages

    def eat(self, food, kg):
        self.weight += kg / 4
        if food == "meat":
            Zoo().available_meat -= kg
        else:
            Zoo().available_grass -= kg

    def die(self, life_expectancy):
        chance_of_dying = self.age / life_expectancy
        random_number = random.random()
        if random_number > chance_of_dying:
            return True
        else:
            return False


