import string

char_set = list(string.ascii_letters)

groups = []
with open("input.txt", "r") as f:
    group = []
    for line in f:
        group.append(line.strip('\n'))
        if len(group) == 3:
            groups.append(group)
            group = []

priority_sum = 0

for elem in groups:
    for char in elem[0]:
        if char in elem[1] and char in elem[2]:
            priority_sum += char_set.index(char) + 1
            break

print(priority_sum)
