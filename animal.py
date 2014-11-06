import random
#from zoo import Zoo


class Animal:
    life_expectancy = 50

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        self.last_pregnancy = 0
        self.meat_eaten = 0
        self.grass_eaten = 0
        self.life_expectancy = 0
        self.food_type = None
        self.gestation_period = 0
        self.newborn_weight = 0
        self.average_weight = 0
        self.weight_age_ratio = 0
        self.food_weight_ratio = 0

    def grow(self):
        self.weight += weight
        self.age += ages

    def eat(self, food, kg):
        self.weight += kg
        if food == "meat":
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
