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
        self.last_pregnancy = None
        self.meat_eaten = 0
        self.grass_eaten = 0

    def grow(self, ages, weight):
        self.weight += weight
        self.age += ages

    def eat(self, food, kg):
        self.weight += kg / 4
        if food == "meat":
            Zoo().available_meat -= kg
            self.meat_eaten += kg
        else:
            Zoo().available_grass -= kg
            self.grass_eaten += kg

    def die(self, life_expectancy):
        chance_of_dying = self.age / life_expectancy
        random_number = random.random()
        if random_number > chance_of_dying:
            return True
        else:
            return False

