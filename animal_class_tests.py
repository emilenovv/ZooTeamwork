import unittest
from animal import Animal



class AnimalTests(unittest.TestCase):

    def setUp(self):
        self.animal = Animal("tiger", 144, "DiviaLud", "male", 300)

    def test_init(self):
        self.assertEqual(self.animal.species, "tiger")
        self.assertEqual(self.animal.age, 144)
        self.assertEqual(self.animal.name, "DiviaLud")
        self.assertEqual(self.animal.gender, "male")
        self.assertEqual(self.animal.weight, 300)

    def test_grow(self):
        self.animal.grow(2, 50)
        self.assertEqual(self.animal.age, 146)
        self.assertEqual(self.animal.weight, 350)

    def test_eat_meat(self):
        self.animal.eat("meat", 4)
        self.assertGreater(self.animal.weight, 12)
        self.assertEqual(self.animal.meat_eaten, 4)
        #self.assertEqual(self.animal.Zoo.available_meat, 296)

        self.animal.eat("meat", 4)
        self.assertGreater(self.animal.weight, 16)
        self.assertEqual(self.animal.meat_eaten, 8)
        #self.assertEqual(self.animal.Zoo.available_meat, 292)

    def test_eat_grass(self):
        self.animal.eat("grass", 4)
        self.assertGreater(self.animal.weight, 12)
        self.assertEqual(self.animal.grass_eaten, 4)
        #self.assertEqual(self.animal.Zoo.available_grass, 196)

        self.animal.eat("grass", 4)
        self.assertGreater(self.animal.weight, 16)
        self.assertEqual(self.animal.grass_eaten, 8)
        #self.assertEqual(self.animal.Zoo.available_grass, 192)

    def test_die(self):
        died_or_not = []
        for i in range(100):
            died_or_not.append(self.animal.die(180))
        self.assertIn(True, died_or_not)
        self.assertIn(False, died_or_not)



if __name__ == '__main__':
    unittest.main()
