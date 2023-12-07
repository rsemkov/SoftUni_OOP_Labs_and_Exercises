from unittest import TestCase, main


class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception("Not enough energy.")

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f"{self.name} has saved {self.money} money."

# TESTING ############


class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker("Gosho", 8000, 100)

    def test_initialization(self):
        self.assertEqual("Gosho", self.worker.name)
        self.assertEqual(8000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_successful_work_expect_money_increase_and_energy_decrease(self):
        self.worker.work()
        self.assertEqual(8000, self.worker.money)
        self.assertEqual(99, self.worker.energy)

    def test_unsuccessful_work_not_enough_energy_expect_exception_error(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_rest_expect_energy_raise(self):
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_get_info_expected_string_return(self):
        self.assertEqual("Gosho has saved 0 money.", self.worker.get_info())


if __name__ == "__main__":
    main()
