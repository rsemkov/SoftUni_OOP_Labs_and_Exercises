from unittest import TestCase, main
from car_manager import Car


class CarTests(TestCase):
    def setUp(self):
        self.car = Car("BMW", "E46", 10, 40)

    def test_correct_input(self):
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("E46", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(40, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_incorrect_input_make_is_null_or_empty_expect_raised_error(self):
        with self.assertRaises(Exception) as ex:
            car = Car("", "E46", 10, 40)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_incorrect_input_model_is_null_or_empty_expect_raised_error(self):
        with self.assertRaises(Exception) as ex:
            car = Car("BMW", "", 10, 40)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_incorrect_input_fuel_consumption_is_zero_or_negative_expect_raised_error(self):
        with self.assertRaises(Exception) as ex:
            car = Car("BMW", "E46", 0, 40)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_incorrect_input_fuel_capacity_is_zero_or_negative_expect_raised_error(self):
        with self.assertRaises(Exception) as ex:
            car = Car("BMW", "E46", 10, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_incorrect_input_fuel_amount_is_negative_expect_raised_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_if_fuel_amount_is_zero_or_negative_expect_raised_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_if_fuel_amount_more_than_zero_with_total_amount_exceeding_the_capacity_expect_increase_only_to_capacty_levels(self):
        self.car.refuel(45)
        self.assertEqual(40, self.car.fuel_capacity)

    def test_refuel_if_fuel_amount_more_than_zero_and_total_fuel_not_exceeding_capacity_expect_fuel_amount_increase_with_given_amount(self):
        self.car.refuel(40)
        self.assertEqual(40, self.car.fuel_capacity)

    def test_drive_if_needed_fuel_is_not_enough_expect_raised_error(self):
        self.car.refuel(10)
        with self.assertRaises(Exception) as ex:
            self.car.drive(101)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_if_needed_fuel_is_enough_expect_fuel_amount_decrease(self):
        self.car.refuel(10)
        self.car.drive(100)
        self.assertEqual(0, self.car.fuel_amount)


if __name__ == "__main__":
    main()