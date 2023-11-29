class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.start_idx = 0
        self.end_idx = len(iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.end_idx < self.start_idx:
            raise StopIteration
        self.end_idx -= 1
        return self.iterable[self.end_idx + 1]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
