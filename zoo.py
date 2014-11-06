from animal import Animal
import random
import json

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

    def name_baby(self, baby):
        name = input("You have a newborn {}. Give it a name: ".format(baby.species))
        return name

    def does_name_exist(self, name, animal):
        names_list = self.names_for_species(animal)
        if name in names_list:
            return True
        else:
            return False

    def reproduce(self, animal1, animal2):
        min_age = 24
        cannot_get_pregnant = 6
        if animal1.age < min_age or animal2.age < min_age:
            return "Cannot reproduce. Animals are too young"

        if animal1.species == animal2.species and animal1.gender != animal2.gender:
            if animal1.gender == "female" and animal1.age - animal1.last_pregnancy >= cannot_get_pregnant:
                animal1.last_pregnancy = animal1.age
            elif animal2.gender == "female" and animal2.age - animal2.last_pregnancy >= cannot_get_pregnant:
                animal2.last_pregnancy = animal2.age
            baby = Animal(animal1.species, 0, None, self.gender_baby(), animal1.newborn_weight)
            while True:
                baby.name = self.name_baby(baby)
                if self.does_name_exist(baby.name, baby) is False:
                    break
            self.accommodate(baby)
            return baby
        else:
            return "Cannot reproduce"

    def load(self):
        infile = open("database.json", "r")
        data = json.load(infile)
        for i in range(len(data["Animals"])):
            self.animals.append(Animal(

                data["Animals"][i]["species"],
                data["Animals"][i]["life_expectancy"],
                data["Animals"][i]["food_type"],
                data["Animals"][i]["gestation_period"],
                data["Animals"][i]["newborn_weight"],
                data["Animals"][i]["average_weight"],
                data["Animals"][i]["weight_age_ratio"],
                data["Animals"][i]["food_weight_ratio"],
                ))