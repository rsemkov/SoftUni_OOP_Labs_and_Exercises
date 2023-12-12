from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTests(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100, 200)

    def test_correct_input(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_fuel_is_less_than_needed_fuel_expect_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_fuel_is_enough_expect_fuel_to_be_reduced_with_fuel_needed_amount(self):
        self.vehicle.drive(8)
        self.assertEqual(90, self.vehicle.fuel)

    def test_refuel_when_the_current_plus_added_fuel_exceed_the_capacity_expect_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_when_the_current_plus_added_fuel_do_not_exceed_the_capacity_expect_fuel_increase(self):
        self.vehicle.capacity = 110
        self.vehicle.refuel(9)
        self.assertEqual(109, self.vehicle.fuel)

    def test_str_representation_expect_string_with_object_data(self):
        self.assertEqual("The vehicle has 200 horse power with 100 "
                         "fuel left and 1.25 fuel consumption", self.vehicle.__str__())


if __name__ == "__main__":
    main()
