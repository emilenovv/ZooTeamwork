import unittest
from zoo import Zoo
from animal import Animal


class ZooTest(unittest.TestCase):

    def setUp(self):
        self.first_animals = [Animal("tiger", 144, "DiviaLud", "male", 300),
                              Animal("tiger", 96, "Pam", "female", 280),
                              Animal("panda", 72, "Pom-Pom", "male", 340)]

        self.zoo = Zoo(self.first_animals, 100, 1200)

        self.animal1 = Animal("panda", 48, "Jully", "female", 350)
        self.animal2 = Animal("panda", 48, "Lilly", "female", 350)
        self.animal3 = Animal("tiger", 144, "DiviaLud", "male", 300)
        self.animal4 = Animal("tiger", 96, "Pam", "female", 280)

    def test_init(self):
        self.assertEqual(self.zoo.animals, self.first_animals)
        self.assertEqual(self.zoo.capacity, 100)
        self.assertEqual(self.zoo.budget, 1200)

    def test_names_for_species(self):
        self.assertEqual(self.zoo.names_for_species(self.animal3),
                         ["DiviaLud", "Pam"])

    def test_names_for_species_doesnot_have_such_species(self):
        self.assertEqual(self.zoo.names_for_species(Animal(
            "horse", 96, "Pam", "female", 280)), [])

    def test_accomodate(self):
        self.assertTrue(self.zoo.accommodate(self.animal1))
        self.assertIn(self.animal1, self.zoo.animals)

    def test_accomodate_no_more_space(self):
        zoo1 = Zoo(self.first_animals, 3, 1200)
        self.assertEqual(zoo1.accommodate(self.animal1), "No more space!")

    def test_accomodate_exists_name(self):
        animal = Animal("panda", 48, "Pom-Pom", "female", 350)
        message = "There is such species with the same name. Rename your animal"
        self.assertEqual(self.zoo.accommodate(animal), message)

    def test_get_income(self):
        self.zoo.get_income()
        self.assertEqual(self.zoo.budget, 1380)

    def test_outcome(self):
        self.first_animals[0].eat()  # tiger
        self.first_animals[1].eat()  # tiger
        self.first_animals[2].eat()  # panda
        # 21 * 4 + 19.6 * 4 + 34 * 2 = 162.4 + 68 = 230.4
        self.zoo.outcome()
        self.assertEqual(self.zoo.budget, 969.6)

    def test_clear_dead_animals_all_died(self):
        for i in range(100):
            self.zoo.clear_dead_animals()
        self.assertEqual(self.zoo.animals, [])

    def test_gender_baby(self):
        genders = []
        for i in range(1000):
            genders.append(self.zoo.gender_baby())
        self.assertIn("female", genders)
        self.assertIn("male", genders)

    def test_name_baby(self):
        # "Boo"
        print("Give it a name Boo!!!")
        baby = Animal("tiger", 0, None, "female", 1)
        self.assertEqual(self.zoo.name_baby(baby), "Boo")

    def test_does_name_exist(self):
        animal = Animal("tiger", 0, None, "female", 1)
        name = "Boo"
        name2 = "Pam"
        self.assertFalse(self.zoo.does_name_exist(name, animal))
        self.assertTrue(self.zoo.does_name_exist(name2, animal))

    def test_can_get_pregnant(self):
        self.animal1.give_birth = 0
        self.assertTrue(self.zoo.can_get_pregnant(self.animal1))
        self.assertEqual(self.animal1.give_birth, 53)
        # animal1 age = 48
        self.animal1.give_birth = 44
        self.assertFalse(self.zoo.can_get_pregnant(self.animal1))
        self.assertEqual(self.animal1.give_birth, 44)

    def test_create_a_baby(self):
        # tiger
        baby = self.zoo.create_a_baby(self.animal3)
        self.assertIn(baby, self.zoo.animals)
        self.assertEqual(baby.species, self.animal3.species)
        self.assertEqual(baby.weight, self.animal3.newborn_weight)
        self.assertEqual(baby.age, 0)
        self.assertIn(baby.gender, ["male", "female"])

    def test_reproduce_first_animal_too_small(self):
        self.animal4.last_pregnancy = 0
        self.animal3 = Animal("tiger", 12, "DiviaLud", "male", 300)
        self.animal4 = Animal("tiger", 96, "Pam", "female", 280)
        self.assertEqual(self.zoo.reproduce(self.animal3, self.animal4),
                         "Cannot reproduce. Animals are too young")

    def test_reproduce_second_animal_too_small(self):
        self.animal4.last_pregnancy = 0
        self.animal3 = Animal("tiger", 12, "DiviaLud", "male", 300)
        self.animal4 = Animal("tiger", 96, "Pam", "female", 280)
        self.assertEqual(self.zoo.reproduce(self.animal4, self.animal3),
                         "Cannot reproduce. Animals are too young")

    def test_reproduce_both_animals_too_small(self):
        self.animal4.last_pregnancy = 0
        self.animal3 = Animal("tiger", 12, "DiviaLud", "male", 300)
        self.animal4 = Animal("tiger", 12, "Pam", "female", 280)
        self.assertEqual(self.zoo.reproduce(self.animal4, self.animal3),
                         "Cannot reproduce. Animals are too young")

    def test_reproduce_same_gender(self):
        self.assertEqual(self.zoo.reproduce(self.animal1, self.animal2),
                         "Cannot reproduce")

    def test_reproduce_different_species(self):
        self.assertEqual(self.zoo.reproduce(self.animal1, self.animal3),
                         "Cannot reproduce")

    def test_reproduce_before_six_months(self):
        self.animal4.age = 44
        self.animal4.give_birth = 40
        self.assertEqual(self.zoo.reproduce(self.animal3, self.animal4),
                         "Cannot reproduce")
        self.assertEqual(self.zoo.reproduce(self.animal4, self.animal3),
                         "Cannot reproduce")

    def test_reproduce_successfully(self):
        baby = self.zoo.reproduce(self.animal3, self.animal4)
        self.assertIn(baby, self.zoo.animals)
        self.assertEqual(baby.species, self.animal3.species)
        self.assertEqual(baby.weight, self.animal3.newborn_weight)
        self.assertEqual(baby.age, 0)
        self.assertIn(baby.gender, ["male", "female"])

if __name__ == '__main__':
    unittest.main()
