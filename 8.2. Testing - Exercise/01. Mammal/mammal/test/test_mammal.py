from unittest import TestCase, main
from project.mammal import Mammal


class MammalTests(TestCase):
    def setUp(self):
        self.mammal = Mammal("Gosho", "Tiger", "Rawr!")

    def test_correct_input(self):
        self.assertEqual("Gosho", self.mammal.name)
        self.assertEqual("Tiger", self.mammal.type)
        self.assertEqual("Rawr!", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound_expect_string_return(self):
        self.assertEqual("Gosho makes Rawr!", self.mammal.make_sound())

    def test_info_expect_string_return(self):
        self.assertEqual("Gosho is of type Tiger", self.mammal.info())


if __name__ == "__main__":
    main()
