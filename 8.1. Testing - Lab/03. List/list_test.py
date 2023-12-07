from unittest import TestCase, main
from list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.integer_list = IntegerList(1, 2, 3, 3.5, "3", False)

    def test_correct_init(self):
        expected_result = [1, 2, 3]
        self.assertEqual(expected_result, self.integer_list.get_data())

    def test_add_element_if_element_not_integer_expect_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.integer_list.add("3")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_element_if_element_is_integer_expect_element_add_to_list_and_return_list(self):
        expected_result = [1, 2, 3, 4]
        self.integer_list.add(4)
        self.assertEqual(expected_result, self.integer_list.get_data())

    def test_remove_index_when_index_out_of_range_expect_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.integer_list.remove_index(10)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index_when_index_is_in_range_expect_remove_the_element_on_given_index_and_return_it(self):
        expected_result = 1
        self.assertEqual(expected_result, self.integer_list.remove_index(0))

    def test_get_index_when_index_out_of_range_expect_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.integer_list.get(10)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_index_when_index_is_in_range_expect_the_element_on_given_index_to_be_returned(self):
        expected_result = 1
        self.assertEqual(expected_result, self.integer_list.get(0))

    def test_insert_el_when_el_is_out_of_range_expect_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.integer_list.insert(10, 3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_el_when_el_is_not_type_integer_expect_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.integer_list.insert(1, "3")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_el_when_el_is_with_valid_idx_and_valid_type_expect_l_to_be_inserted_on_given_idx(self):
        expected_result = [9, 1, 2, 3]
        self.integer_list.insert(0, 9)
        self.assertEqual(expected_result, self.integer_list.get_data())

    def test_get_biggest_expect_the_biggest_to_be_returned(self):
        expected_result = 3
        self.assertEqual(expected_result, self.integer_list.get_biggest())

    def test_get_index_expect_the_index_of_given_el_to_be_returned(self):
        expected_result = 0
        self.assertEqual(expected_result, self.integer_list.get_index(1))


if __name__ == "__main__":
    main()