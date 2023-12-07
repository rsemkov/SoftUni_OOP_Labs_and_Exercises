from unittest import TestCase, main


class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception("Already fed.")

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception("Cannot sleep while hungry")

        self.sleepy = False

################ TEST ###################


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat("Gosho")

    def test_correct_initialization(self):
        self.assertEqual("Gosho", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_feed_when_already_fed_expected_raise_exception(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_feed_when_not_fed_expected_fed_True_sleepy_True_size_increase_by_one(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_sleep_when_not_fed_expect_raise_exception(self):
        self.cat.sleepy = True
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_sleep_when_fed_expect_sleepy_change_to_False(self):
        self.cat.sleepy = True
        self.cat.fed = True
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
