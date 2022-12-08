elf_arr = []

with open("input_1.txt", "r") as f:
    temp = 0
    for line in f:
        try:
            temp += int(line)
        except ValueError:
            elf_arr.append(temp)
            temp = 0

elf_arr.sort(reverse=True)

print(elf_arr[0] + elf_arr[1] + elf_arr[2])