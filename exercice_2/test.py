import unittest
import exercice_2


class MyTestv1(unittest.TestCase):
    def test_divide_400(self):
        self.assertFalse(exercice_2.is_leap_year_v1(2021))


class MyTestv2(unittest.TestCase):
    def test_divide_400(self):
        self.assertFalse(exercice_2.is_leap_year_v2(2021))

    def test_divide_4(self):
        self.assertFalse(exercice_2.is_leap_year_v2(2003))


class MyTestv3(unittest.TestCase):
    def test_divide_400(self):
        self.assertFalse(exercice_2.is_leap_year_v3(2021))

    def test_divide_4(self):
        self.assertFalse(exercice_2.is_leap_year_v3(2003))

    def test_divide_100(self):
        self.assertFalse(exercice_2.is_leap_year_v3(2100))

class MyTestv4(unittest.TestCase):
    def test_divide_400(self):
        self.assertFalse(exercice_2.is_leap_year_v4(2021))

    def test_divide_4(self):
        self.assertFalse(exercice_2.is_leap_year_v4(2003))

    def test_divide_100(self):
        self.assertFalse(exercice_2.is_leap_year_v4(2100))

    def test_divide_not_4(self):
        self.assertFalse(exercice_2.is_leap_year_v4(3))

    def test_not_int(self):
        with self.assertRaises(TypeError):
            exercice_2.is_leap_year_v4("A")



if __name__ == '__main__':
    unittest.main()
