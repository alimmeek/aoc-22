temp = []

with open('input.txt', 'r') as f:
    for line in f:
        temp.append(line.strip('\n').split(','))

contained = 0

for elem in temp:
    x = elem[0].split('-')
    y = elem[1].split('-')
    
    #if int(x[0]) >= int(y[0]) or int(x[1]) <= int(y[1]):
    #    contained += 1
    #elif int(x[0]) <= int(y[0]) or int(x[1]) >= int(y[1]):
    #    contained += 1

    x_seq = [i for i in range(int(x[0]), int(x[1]) + 1)]
    for j in range(int(y[0]), int(y[1])+1):
        if j in x_seq:
            contained += 1
            break

print(contained)