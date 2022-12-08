class Node:
    def __init__(self, s=0, t="", n="", p=None):
        self.size = s
        self.type = t
        self.name = n
        self.parent = p
        self.children = []
    
    def __repr__(self):
        return f"{self.type} {self.name}"
    
    def is_child(self, N: "Node"):
        for i in range(len(self.children)):
            if self.children[i].size == N.size and self.children[i].type == N.type and self.children[i].name == N.name and self.children[i].parent == N.parent and self.children[i].children == N.children:
                return i
        return -1

smol_sum = 0
dirs = []

class Tree:
    def __init__(self):
        self.root = None
    
    def _traversal(self, n: "Node"):
        if n.children != []:
            for child in n.children:
                self._traversal(child)
        print(n.size)
    
    def traversal(self):
        self._traversal(self.root)
    
    def calc_dir_sizes(self, n:"Node"):
        if n.type == "txt":
            return n.size
        elif n.children == []:
            return 0
        else:
            sum = 0
            for child in n.children:
                sum += self.calc_dir_sizes(child)
            n.size = sum
            return sum
    
    def less_than_100000(self, n:"Node"):
        global smol_sum
        if n.children != []:
            for child in n.children:
                self.less_than_100000(child)
        if n.type == "dir" and n.size < 100000:
            smol_sum += n.size
    
    def get_dirs(self, n: "Node"):
        global dirs
        if n.children != []:
            for child in n.children:
                self.get_dirs(child)
        if n.type == "dir":
            dirs.append(n)

cwd = Node(t="dir", n="/")
t = Tree()
t.root = cwd

with open("input.txt", "r") as f:
    for line in f:
        if line[0] == '$':
            if line[2:4] == "cd":
                if line[5] == "/":
                    cwd = t.root
                elif line[5:7] == "..":
                    cwd = cwd.parent
                else:
                    filename = ""
                    for char in line[5:]:
                        if char != '\n':
                            filename += char
                    temp = Node(t="dir", n=filename, p=cwd)
                    x = cwd.is_child(temp)
                    if x >= 0:
                        cwd = cwd.children[x]
                    else:
                        cwd.children.append(temp)
                        cwd = temp
        else:
            try:
                temp = int(line[0:3])
                size = ""
                counter = 0
                for char in line:
                    counter += 1
                    if char != ' ':
                        size += char
                    else:
                        break
                filename = ""
                for char in line[counter+1:]:
                    if char != '\n':
                        filename += char
                cwd.children.append(Node(s=int(size), t="txt", n=filename, p=cwd))
            except ValueError:
                filename = ""
                for char in line[4:]:
                    if char != '\n':
                        filename += char
                cwd.children.append(Node(t="dir", n=filename, p=cwd))

t.calc_dir_sizes(t.root)
t.less_than_100000(t.root)
t.get_dirs(t.root)

required = 30000000 - (70000000 - t.root.size)
smallest = 70000000
for el in dirs:
    if el.size < smallest and el.size >= required:
        smallest = el.size

print(smallest)