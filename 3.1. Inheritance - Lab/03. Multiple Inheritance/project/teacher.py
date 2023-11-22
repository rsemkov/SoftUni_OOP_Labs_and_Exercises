from project.person import Person
from project.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."


katia_semkova = Teacher()
print(katia_semkova.teach())
print(katia_semkova.get_fired())
print(katia_semkova.sleep())
