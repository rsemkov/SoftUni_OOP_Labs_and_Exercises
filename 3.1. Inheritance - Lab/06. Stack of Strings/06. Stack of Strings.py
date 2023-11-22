class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if self.data:
            return False
        return True

    def __str__(self):
        reversed_data = list(reversed(self.data))
        return f'[{", ".join(reversed_data)}]'


guz = Stack()
guz.push("carrot")
guz.push("apple")
print(guz.is_empty())
print(str(guz))