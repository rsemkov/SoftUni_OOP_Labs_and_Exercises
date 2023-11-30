class vowels:
    VOWELS = "aeiouyAEIOUY"

    def __init__(self, str_input):
        self.str_input = str_input
        self.start_idx = 0
        self.end_idx = len(str_input) - 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.start_idx <= self.end_idx:
            current_char = self.str_input[self.start_idx]
            self.start_idx += 1
            if current_char in self.VOWELS:
                return current_char
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)