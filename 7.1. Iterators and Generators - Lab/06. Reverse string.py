def reverse_text(str_input):
    yield str_input[-1::-1]


for char in reverse_text("step"):
    print(char, end='')