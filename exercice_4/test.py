import unittest
from unittest.mock import MagicMock
import exercice_4


class MyTestCase(unittest.TestCase):

    def test_enable_true(self):
        mock = MagicMock()
        mock.get_actual_temp.return_value = 25
        mock.get_last_days_temp.return_value = [20, 15, 25, 30, 27, 22, 18]

        pool_temp = exercice_4.pool_temp(pool_logic=mock)
        pool_temp.enable_heater()

        mock.set_heater.assert_called_with(pool_temp, active=True)

    def test_enable_false_actual_temp(self):
        mock = MagicMock()
        mock.get_actual_temp.return_value = 20
        mock.get_last_days_temp.return_value = [20, 15, 25, 30, 27, 22, 18]

        pool_temp = exercice_4.pool_temp(pool_logic=mock)
        pool_temp.enable_heater()

        mock.set_heater.assert_called_with(pool_temp, active=False)

    def test_enable_false_last_days_temp(self):
        mock = MagicMock()
        mock.get_actual_temp.return_value = 25
        mock.get_last_days_temp.return_value = [20, 15, 25, 18, 15, 22, 18]

        pool_temp = exercice_4.pool_temp(pool_logic=mock)
        pool_temp.enable_heater()

        mock.set_heater.assert_called_with(pool_temp, active=False)


if __name__ == '__main__':
    unittest.main()
