import json


class ZooDatabase:
    def __init__(self, species):
        source = open("database.json", "r")
        data = json.load(source)
        for i in range(len(data["Animals"])):
            if species == data["Animals"][i]["species"]:
                self.life_expectancy = data["Animals"][i]["life_expectancy"]
                self.food_type = data["Animals"][i]["food_type"]
                self.gestation_period = data["Animals"][i]["gestation_period"]
                self.newborn_weight = data["Animals"][i]["newborn_weight"]
                self.average_weight = data["Animals"][i]["average_weight"]
                self.weight_age_ratio = data["Animals"][i]["weight_age_ratio"]
                self.food_weight_ratio = data["Animals"][i]["food_weight_ratio"]
        source.close()
