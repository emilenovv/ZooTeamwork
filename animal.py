import random
from zoo_database import ZooDatabase
#from zoo import Zoo


class Animal(ZooDatabase):
    DAYS_IN_MONTH = 30
    DAYS_IN_YEAR = 365

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
        age_in_days = self.age * Animal.DAYS_IN_MONTH
        age_in_days += 1
        if self.weight < self.average_weight:
            weight_age_ratio_per_day = self.weight_age_ratio / Animal.DAYS_IN_MONTH
            self.weight += weight_age_ratio_per_day
        if age_in_days % Animal.DAYS_IN_MONTH < 15:
            self.age = age_in_days // 30
        else:
            self.age = (age_in_days // 30) + 1

    def eat(self, food):
        kg = self.weight * self.food_weight_ratio
        self.weight += kg
        if food == "meat" and self.food_type == food:
            #Zoo().available_meat -= kg

            self.meat_eaten += kg
        elif food == "grass" and self.food_type == food:
            #Zoo().available_grass -= kg
            self.grass_eaten += kg

        else:
            return "I don't eat {}. Give me other food.".format(food)

    def die(self):
        life_expectancy_days = self.life_expectancy * Animal.DAYS_IN_YEAR
        age_in_days = self.age * Animal.DAYS_IN_MONTH
        chance_of_dying = age_in_days / life_expectancy_days
        random_number = random.random()
        if random_number > chance_of_dying:
            return True
        else:
            return False
