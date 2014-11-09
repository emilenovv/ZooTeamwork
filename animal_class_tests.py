import unittest
from animal import Animal



class AnimalTests(unittest.TestCase):

    def setUp(self):
        self.animal = Animal("tiger", 144, "DiviaLud", "male", 120)

    def test_init(self):
        self.assertEqual(self.animal.species, "tiger")
        self.assertEqual(self.animal.age, 144)
        self.assertEqual(self.animal.name, "DiviaLud")
        self.assertEqual(self.animal.gender, "male")
        self.assertEqual(self.animal.weight, 120)

        self.assertEqual(self.animal.life_expectancy, 15)
        self.assertEqual(self.animal.food_type, "meat")
        self.assertEqual(self.animal.gestation_period, 3)
        self.assertEqual(self.animal.newborn_weight, 1)
        self.assertEqual(self.animal.average_weight, 250)
        self.assertEqual(self.animal.weight_age_ratio, 3)
        self.assertEqual(self.animal.food_weight_ratio, 0.07)

    def test_grow(self):
        self.animal.age = 10    # months
        self.animal.grow()
        self.assertEqual(self.animal.age, 10.01)
        self.assertEqual(self.animal.weight, 120.1)

    def test_grow_with_month(self):
        self.animal.age = 10.30    # months
        self.animal.grow()
        self.assertEqual(self.animal.age, 11.00)
        self.assertEqual(self.animal.weight, 120.1)

    def test_grow_avarage_weight(self):
        self.animal.weight = 250    # months
        self.animal.grow()
        self.assertEqual(self.animal.weight, 250)

    def test_eat_meat(self):
        self.animal.weight = 10
        self.animal.age = 10
        self.animal.eat()
        self.assertEqual(self.animal.weight, 10.1)
        self.assertEqual(self.animal.age, 10.01)
        self.assertEqual(self.animal.meat_eaten, 0.7)

        self.animal.weight = 10
        self.animal.eat()
        self.assertEqual(self.animal.age, 10.02)
        self.assertEqual(self.animal.meat_eaten, 1.4)

    def test_eat_grass(self):
        self.animal.food_type = "grass"
        self.animal.weight = 10
        self.animal.age = 10
        self.animal.eat()
        self.assertEqual(self.animal.weight, 10.1)
        self.assertEqual(self.animal.age, 10.01)
        self.assertEqual(self.animal.grass_eaten, 0.7)

        self.animal.weight = 10
        self.animal.eat()
        self.assertEqual(self.animal.age, 10.02)
        self.assertEqual(self.animal.grass_eaten, 1.4)

    def test_age_in_days(self):
        self.animal.age = 1.01
        self.assertEqual(self.animal.age_in_days(), 31)
        self.animal.age = 10.10
        self.assertEqual(self.animal.age_in_days(), 310)

    def test_die(self):
        died_or_not = []
        for i in range(100):
            died_or_not.append(self.animal.die())
        self.assertIn(True, died_or_not)
        self.assertIn(False, died_or_not)



if __name__ == '__main__':
    unittest.main()
