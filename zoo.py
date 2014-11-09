from animal import Animal
import random


class Zoo:

    def __init__(self, animals, capacity, budget):
        self.animals = animals
        self.capacity = capacity
        self.budget = budget

    def names_for_species(self, new_animal):
        names_list = []
        for animal in self.animals:
            if animal.species == new_animal.species:
                names_list.append(animal.name)
        return names_list

    def accommodate(self, new_animal):
        names_list = []
        names_list = self.names_for_species(new_animal)

        if len(self.animals) == self.capacity:
            return "No more space!"
        elif new_animal.name not in names_list:
            self.animals.append(new_animal)
            return True
        elif new_animal.name in names_list:
            return "There is such species with the same name. Rename your animal"

    def get_income(self):
        animal_brings = 60
        self.budget += animal_brings * len(self.animals)

    def outcome(self):
        total_meat = 0
        total_grass = 0
        grass_price = 2
        meat_price = 4
        for animal in self.animals:
            total_grass += animal.grass_eaten
            total_meat += animal.meat_eaten

        self.budget -= total_grass * grass_price + total_meat * meat_price

    def clear_dead_animals(self):
        for animal in self.animals:
            if animal.die() is True:
                self.animals.remove(animal)

    def gender_baby(self):
        random_number = random.random()
        if random_number > 0.5:
            return "male"
        return "female"

    def name_baby(self, baby):
        name = input(
            "You have a newborn {} {}. Give it a name: ".format(baby.gender, baby.species))
        return name

    def does_name_exist(self, name, animal):
        names_list = self.names_for_species(animal)
        if name in names_list:
            return True
        else:
            return False

    def can_get_pregnant(self, female_animal):
        after_birth_period = 6  # months
        age = female_animal.age
        give_birth = female_animal.give_birth
        gestation_period = female_animal.gestation_period

        if age >= give_birth + after_birth_period:
            female_animal.give_birth = age + gestation_period
            return True
        return False

    def create_a_baby(self, parent):
        baby = Animal(
            parent.species, 0, None, self.gender_baby(),
            parent.newborn_weight)
        while True:
            baby.name = self.name_baby(baby)
            if self.does_name_exist(baby.name, baby) is False:
                self.accommodate(baby)
                return baby
            else:
                print("There is an animal with the same name! \
                    Please rename the baby!")

    def reproduce(self, animal1, animal2):
        min_age = 24
        if animal1.age < min_age or animal2.age < min_age:
            return "Cannot reproduce. Animals are too young"

        same_species = animal1.species == animal2.species
        different_gender = animal1.gender != animal2.gender

        if same_species and different_gender:
            if animal1.gender == "female" and self.can_get_pregnant(animal1):
                baby = self.create_a_baby(animal1)
                return baby
            elif animal2.gender == "female" and self.can_get_pregnant(animal2):
                baby = self.create_a_baby(animal2)
                return baby
        return "Cannot reproduce"
