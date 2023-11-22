from project.animal import Animal


class Dog(Animal):
    def bark(self):
        return "barking..."


kuche = Dog()
print(kuche.eat())
print(kuche.bark())