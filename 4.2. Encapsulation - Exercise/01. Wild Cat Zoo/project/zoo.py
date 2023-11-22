from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > len(self.animals) and self.__budget >= price:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker):
        fired_worker = list(filter(lambda x: x.name == worker, self.workers))
        if not fired_worker:
            return f"There is no {worker} in the zoo"

        self.workers.remove(fired_worker[0])
        return f"{worker} fired successfully"

    def pay_workers(self):
        salaries_total = sum([x.salary for x in self.workers])
        if salaries_total > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries_total
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        animal_expenses_total = sum([x.money_for_care for x in self.animals])
        if animal_expenses_total > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= animal_expenses_total
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = [f"You have {len(self.animals)} animals"]
        lions = [x for x in self.animals if isinstance(x, Lion)]
        tigers = [x for x in self.animals if isinstance(x, Tiger)]
        cheetahs = [x for x in self.animals if isinstance(x, Cheetah)]

        result.append(f"----- {len(lions)} Lions:")
        for lion in lions:
            result.append(f"{lion.__repr__()}")

        result.append(f"----- {len(tigers)} Tigers:")
        for tiger in tigers:
            result.append(f"{tiger.__repr__()}")

        result.append(f"----- {len(cheetahs)} Cheetahs:")
        for cheetah in cheetahs:
            result.append(f"{cheetah.__repr__()}")

        return '\n'.join(result)

    def workers_status(self):
        result = [f"You have {len(self.workers)} workers"]
        keepers = [x for x in self.workers if isinstance(x, Keeper)]
        caretakers = [x for x in self.workers if isinstance(x, Caretaker)]
        vets = [x for x in self.workers if isinstance(x, Vet)]

        result.append(f"----- {len(keepers)} Keepers:")
        for keeper in keepers:
            result.append(f"{keeper.__repr__()}")

        result.append(f"----- {len(caretakers)} Caretakers:")
        for caretaker in caretakers:
            result.append(f"{caretaker.__repr__()}")

        result.append(f"----- {len(vets)} Vets:")
        for vet in vets:
            result.append(f"{vet.__repr__()}")

        return '\n'.join(result)
