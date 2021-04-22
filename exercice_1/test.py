import unittest
import exercice_1


class MyTestCase(unittest.TestCase):
    # Test join function
    def test_concat(self):
        self.assertEqual("Hello World", exercice_1.join(["Hello", "World"], " "))

    def test_list_empty(self):
        self.assertEqual("", exercice_1.join([], " "))

    def test_not_list(self):
        with self.assertRaises(TypeError):
            exercice_1.join(0, "")

    # Test avg function
    def test_avg(self):
        self.assertEqual(2, exercice_1.avg([1, 2, 3]))

    def test_avg_empty(self):
        with self.assertRaises(ZeroDivisionError):
            exercice_1.avg([])
            exercice_1.avg("")

    def test_avg_typeerror(self):
        with self.assertRaises(TypeError):
            exercice_1.avg(1)



if __name__ == '__main__':
    unittest.main()
