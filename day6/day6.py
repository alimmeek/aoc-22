line = ""
with open("input.txt", "r") as f:
    for l in f:
        line = l.strip('\n')

for i in range(14, len(line)):
    sl = line[i-14:i]
    print(sl)
    if all(sl.count(char) == 1 for char in sl):
        print(i)
        break