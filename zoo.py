from animal import Animal
import random

class Zoo:
    def __init__(self, animals, capacity, budget):
        self.animals = animals
        self.capacity = capacity
        self.budget = budget
        self.available_meat = 300
        self.available_grass = 200

    def accommodate(self, new_animal):
        names_list = []
        for animal in self.animals:
            if animal.species == new_animal.species:
                names_list.append(animal.name)
        if len(self.animals) < self.capacity and new_animal.name not in names_list:
            self.animals.append(animal)
        elif new_animal.name not in names_list:
            print("There is suck species with the same name. Rename your animal")
        else:
            pass

    def get_income(self, num_animals):
        self.budget += 60 * num_animals

    def outcome(self, kg_meat, kg_grass):
        total_meat = 0
        total_grass = 0
        for animal in self.animals:
            total_grass += animal.grass_eaten
            total_meat += animal.meat_eaten
        self.budget -= total_grass * 2 + total_meat * 4

    def clear_dead_animals(self):
        for animal in self.animals:
            if animal.die() is True:
                self.animals.remove(animal)

    def gender_baby(self):
        random_number = random.random()
        if random_number > 0.5:
            return "male"
        return "female"

    def reproduce(self, animal1, animal2):
        if animal1.species == animal2.species and animal1.gender != animal2.gender:
            if animal1.gender == "female" and animal1.age - animal1.last_pregnancy >= 6:
                animal1.last_pregnancy = animal1.age
            elif animal2.age - animal2.last_pregnancy >= 6:
                animal2.last_pregnancy = animal2.age
            baby = Animal(animal1.species, 0, None, self.gender_baby(), 1)
            return baby
        else:
            return "Cannot reproduce"
