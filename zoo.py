from animal import Animal
import random


class Zoo:

    def __init__(self, animals, capacity, budget):
        self.animals = animals
        self.capacity = capacity
        self.budget = budget

        #self.available_meat = 300
        #self.available_grass = 200

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
        self.budget += aninmal_brings * len(self.animals)

    def outcome(self):
        total_meat = 0
        total_grass = 0
        grass_price = 2
        meat_price = 4
        for animal in self.animals:
            total_grass += animal.grass_eaten
            total_meat += animal.meat_eaten

        self.budget -= total_grass * grass_price + total_meat * meat_price

    def clear_dead_animals(self, life_expectancy):
        for animal in self.animals:
    ############## life_expectancy #############
            if animal.die(life_expectancy) is True:
                self.animals.remove(animal)

    def gender_baby(self):
        random_number = random.random()
        if random_number > 0.5:
            return "male"
        return "female"

    def reproduce(self, animal1, animal2):
        min_age = 24
        cannot_get_pregnant = 6
        if animal1.age < min_age or animal2.age < min_age:
            return "Cannot reproduce. Animals are too young"

        if animal1.species == animal2.species and animal1.gender != animal2.gender:
            if animal1.gender == "female" and animal1.age - animal1.last_pregnancy >= 6:
                animal1.last_pregnancy = animal1.age
            elif animal2.age - animal2.last_pregnancy >= cannot_get_pregnant:
                animal2.last_pregnancy = animal2.age
            baby = Animal(animal1.species, 0, None, self.gender_baby(), 1)
            return baby
        else:
            return "Cannot reproduce"
