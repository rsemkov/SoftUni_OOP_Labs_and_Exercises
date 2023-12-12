from unittest import TestCase, main
from project.student import Student


class StudentTests(TestCase):
    def setUp(self):
        self.student = Student("Goshko", {"risuvane": ["cvete", "vaza"]})

    def test_input_if_courses_is_none(self):
        self.student = Student("Goshko")
        self.assertEqual("Goshko", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_input_if_courses_is_not_none(self):
        self.assertEqual("Goshko", self.student.name)
        self.assertEqual({"risuvane": ["cvete", "vaza"]}, self.student.courses)

    def test_enroll_when_course_is_already_added_expect_notes_to_be_added(self):
        self.student.enroll("risuvane", ["kelepir"])
        self.assertEqual({"risuvane": ["cvete", "vaza", "kelepir"]}, self.student.courses)

    def test_enroll_course_not_in_keys_and_add_course_notes_is_empty_expect_course_added_with_notes(self):
        self.student.enroll("shpaklovane", ["kelepir"])
        self.assertEqual({"risuvane": ["cvete", "vaza"], "shpaklovane": ["kelepir"]}, self.student.courses)

    def test_enroll_course_not_in_keys_and_add_course_notes_is_positive_expect_course_added_with_notes(self):
        self.student.enroll("shpaklovane", ["kelepir"], "Y")
        self.assertEqual({"risuvane": ["cvete", "vaza"], "shpaklovane": ["kelepir"]}, self.student.courses)

    def test_enroll_course_not_in_keys_and_add_course_notes_is_negative_expect_course_added_with_notes(self):
        self.student.enroll("shpaklovane", ["kelepir"], "N")
        self.assertEqual({"risuvane": ["cvete", "vaza"], "shpaklovane": []}, self.student.courses)

    def test_add_notes_if_course_not_exist_expect_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("asd", ["a"])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_if_course_exists_expect_notes_added_to_course(self):
        self.assertEqual("Notes have been updated", self.student.add_notes("risuvane", ["a"]))

    def test_leave_course_if_course_not_in_keys_expect_error_raised(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("asd")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_if_course_in_keys_expect_course_removal_and_message_return(self):

        self.assertEqual("Course has been removed", self.student.leave_course("risuvane"))


if __name__ == "__main__":
    main()

