from project.animals.animal import Mammal
from project.food import Food, Meat, Vegetable, Fruit, Seed


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if not (isinstance(food, Vegetable) or isinstance(food, Fruit)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.1 * food.quantity
        self.food_eaten += food.quantity


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.4 * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if not (isinstance(food, Meat) or isinstance(food, Vegetable)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.3 * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 1 * food.quantity
        self.food_eaten += food.quantity

