string = input()
counter = 1
max_length = 1
max_char = 0

for index in range(len(string)):
    character = string[index]
    if max_char == 0:
        max_char = character
    else:
        if max_char == character:
            counter += 1
            max_length = max(max_length, counter)
        else:
            counter = 1
            max_char = character
print(max_length)
