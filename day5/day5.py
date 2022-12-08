import string

class Stack:

    def __init__(self):
        self._Arr = []

    def __repr__(self):
        return "\n".join(self._Arr[::-1])
    
    def pop(self):
        return self._Arr.pop()
    
    def push(self, item):
        self._Arr.append(item)

    def peek(self):
        return self._Arr[-1]

lines = []
with open("input.txt", "r") as f:
    for line in f:
        lines.append(line.strip('\n'))

stacks = lines[0:8]
temp = []
for line in stacks:
    temp.append(line.split(' '))

for el in temp:
    n = len(el)
    i = 1
    while (i != n):
        if el[i:i+4] == ['', '', '', '']:
            i += 1
            del el[i:i+3]
        i += 1
        n = len(el)

del temp[0][3:6]
del temp[1][7:10]

#for el in temp:
#    print(el)

arr_of_stacks = [Stack() for _ in range(9)]

for i in range(len(temp)-1, -1, -1):
    for j in range(len(temp[i])):
        if temp[i][j] != '':
            arr_of_stacks[j].push(temp[i][j])

moves_temp = lines[10:]
moves = []
for move in moves_temp:
    temp = []
    for char in move:
        if char in string.digits:
            temp.append(int(char))
    if len(temp) == 4:
        num = str(temp[0]) + str(temp[1])
        del temp[0:2]
        temp.insert(0, int(num))
    moves.append(temp)

# num source dest

for move in moves:
    temp = []
    for _ in range(move[0]):
        temp.append(arr_of_stacks[move[1]-1].pop())
    
    temp.reverse()
    for i in range(len(temp)):  
        arr_of_stacks[move[2]-1].push(temp[i])

at_top = []
for i in range(len(arr_of_stacks)):
    at_top.append(arr_of_stacks[i].peek())

print(at_top)