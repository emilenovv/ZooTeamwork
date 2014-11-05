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
        self.first_animals[0].eat("meat", 8)  # tiger
        self.first_animals[1].eat("meat", 10)  # tiger
        self.first_animals[2].eat("bamboo", 4)  # panda
        # 8 * 4 + 10 * 4 + 4 * 2 = 80
        self.zoo.outcome()
        self.assertEqual(self.zoo.budget, 1120)

    def test_clear_dead_animals_all_died(self):
        for i in range(100):
            self.zoo.clear_dead_animals(180)
        self.assertEqual(self.zoo.animals, [])

    def test_gender_baby(self):
        genders = []
        for i in range(1000):
            genders.append(self.zoo.gender_baby())
        self.assertIn("female", genders)
        self.assertIn("male", genders)

    def test_reproduce_same_gender(self):
        self.assertEqual(self.zoo.reproduce(self.animal1,
                                            self.animal2), "Cannot reproduce")

    def test_reproduce_different_species(self):
        self.assertEqual(self.zoo.reproduce(self.animal1,
                                            self.animal3), "Cannot reproduce")

    def test_reproduce_before_six_months(self):
        self.animal4.last_pregnancy = 48
        self.assertEqual(self.zoo.reproduce(self.animal1,
                                            self.animal4), "Cannot reproduce")

####################################################
    def test_reproduce_female_is_second_argument(self):
        self.animal4.last_pregnancy = 0
        self.assertNotEqual(self.zoo.reproduce(self.animal3,
                                               self.animal4), "Cannot reproduce")

    def test_reproduce_female_is_first_argument(self):
        self.animal4.last_pregnancy = 0
        self.assertNotEqual(self.zoo.reproduce(self.animal4,
                                               self.animal3), "Cannot reproduce")

#####################################################

    def test_reproduce_first_animal_too_small(self):
        self.animal4.last_pregnancy = 0
        self.animal3 = Animal("tiger", 12, "DiviaLud", "male", 300)
        self.animal4 = Animal("tiger", 96, "Pam", "female", 280)
        self.assertEqual(self.zoo.reproduce(self.animal3,
                                            self.animal4), "Cannot reproduce. Animals are too young")

    def test_reproduce_second_animal_too_small(self):
        self.animal4.last_pregnancy = 0
        self.animal3 = Animal("tiger", 12, "DiviaLud", "male", 300)
        self.animal4 = Animal("tiger", 96, "Pam", "female", 280)
        self.assertEqual(self.zoo.reproduce(self.animal4,
                                            self.animal3), "Cannot reproduce. Animals are too young")

    def test_reproduce_both_animals_too_small(self):
        self.animal4.last_pregnancy = 0
        self.animal3 = Animal("tiger", 12, "DiviaLud", "male", 300)
        self.animal4 = Animal("tiger", 12, "Pam", "female", 280)
        self.assertEqual(self.zoo.reproduce(self.animal4,
                                            self.animal3), "Cannot reproduce. Animals are too young")

    def test_load(self):
        self.zoo.load()


if __name__ == '__main__':
    unittest.main()
