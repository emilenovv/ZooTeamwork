import random
from zoo_database import ZooDatabase
#from zoo import Zoo


class Animal(ZooDatabase):

    def __init__(self, species, age, name, gender, weight, life_expectancy=0,
                 food_type=None, gestation_period=0, newborn_weight=0, average_weight=0,
                 weight_age_ratio=0, food_weight_ratio=0):
        super().__init__(species)
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        self.last_pregnancy = 0
        self.meat_eaten = 0
        self.grass_eaten = 0

    def grow(self):
        self.weight += weight
        self.age += ages

    def eat(self):
        kg = self.weight * self.food_weight_ratio
        self.weight += kg
        if self.food_type == "meat":
            #Zoo().available_meat -= kg

            self.meat_eaten += kg
        else:
            #Zoo().available_grass -= kg
            self.grass_eaten += kg

    def die(self, life_expectancy):
        chance_of_dying = self.age / life_expectancy
        random_number = random.random()
        if random_number > chance_of_dying:
            return True
        else:
            return False
