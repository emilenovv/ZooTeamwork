import unittest
from animal import Animal


class AnimalTests(unittest.TestCase):
    def setUp(self):
        self.animal = Animal("tiger", 12, "DiviaLud", "male", 300)

    def test_init(self):
        self.assertEqual(self.animal.species, "tiger")
        self.assertEqual(self.animal.age, 12)
        self.assertEqual(self.animal.name, "DiviaLud")
        self.assertEqual(self.animal.gender, "male")
        self.assertEqual(self.animal.weight, 300)

    def test_grow(self):
        self.animal.grow(2, 50)
        self.assertEqual(self.animal.age, 14)
        self.assertEqual(self.animal.weight, 350)

    def test_eat(self):
        self.animal.eat(4)
        self.asserGreater(self.animal.weight, 12)

    def test_die(self):
        died_or_not = []
        for i in range(100):
            died_or_not.append(self.animal.die(15))
        self.assertIn(True, died_or_not)
        self.assertIn(False,died_or_not)



if __name__ == '__main__':
    unittest.main()