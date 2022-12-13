import itertools
import textwrap
raw = open('input/day07.txt', 'r')
# raw = open('input/test.txt', 'r')
f = raw.read()

def flatten(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])

class Node:
    size = 0
    parent = None
    children = None
    name = ""

    def __init__(self, name):
        self.name = name
        self.children = {}

    def get_child(self, name):
        return self.children[name]
    
    def add_child(self, name):
        child = Node(name)
        child.parent = self
        self.children[name] = child
        return child
    
    def get_sub_dirs(self):
        if len(self.children) == 0:
            return []
        else:
            return flatten([self, [child.get_sub_dirs() for child in self.children.values()]])
    
    def get_size(self):
        if len(self.children) == 0:
            return self.size
        else:
            return sum([child.get_size() for child in self.children.values()])
    
    def get_depth(self):
        if self.parent is None:
            return 0
        else:
            return 1 + self.parent.get_depth()
    
    def __str__(self):
        if len(self.children) == 0:
            desc = f"(file, size={self.get_size()})"
        else:
            desc = f"(dir, size={self.get_size()})"
        res = f"- {self.name} {desc}"
        for child in self.children.values():
            indent = "  " * child.get_depth()
            res += f"\n{indent}{str(child)}"
        return res
    
    def __hash__(self):
        return hash(repr(self))
    
    def __repr__(self):
        return self.name

    def __eq__(self,other):
        return hash(self) == hash(other)
    
    def __lt__(self, other):
        return self.get_size() < other.get_size()

root = Node("/")
current = root
commands = [ [ line.split(" ") for line in command.strip().splitlines()] for command  in f.strip().split("$")][1:]

for cmd in commands:
    if cmd[0][0] == "cd":
        target = cmd[0][1]
        if target == "/":
            current = root
        elif target == "..":
            current = current.parent
        else:
            current = current.get_child(target)
    elif cmd[0][0] == "ls":
        for result in cmd[1:]:
            child = current.add_child(result[1])
            if result[0] != "dir":
                child.size = int(result[0])            

max_dir_size = 100000

dirs = root.get_sub_dirs()
sizes = [dir.get_size() for dir in dirs]

p1 = sum([x for x in sizes if x <= max_dir_size])

print(f"part 1: {p1}")

total_size = 70000000
unused = total_size - root.get_size()
required = 30000000
min_to_delete = required - unused

p2 = min([dir for dir in dirs if dir.get_size() >= min_to_delete]).get_size()

print(f"part 2: {p2}")