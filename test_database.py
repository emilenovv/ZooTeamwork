import unittest
import zoo_database
import animal


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.tiger = animal.Animal("tiger", 5, "Emil", "male", 80)
        self.panda = animal.Animal("panda", 1, "Pan", "female", 120)

    def test_full_init(self):
        self.assertEqual(self.tiger.species, "tiger")
        self.assertEqual(self.tiger.age, 5)
        self.assertEqual(self.tiger.name, "Emil")
        self.assertEqual(self.tiger.gender, "male")
        self.assertEqual(self.tiger.weight, 80)
        self.assertEqual(self.tiger.life_expectancy, 15)
        self.assertEqual(self.tiger.food_weight_ratio, 0.07)
        self.assertEqual(self.panda.food_weight_ratio, 0.1)



if __name__ == '__main__':
    unittest.main()