import itertools
import math
raw = open('input/day09.txt', 'r')
# raw = open('input/test.txt', 'r')
f = [line[:-1] for line in raw]

class Node(object):
    position = (0,0)
    visited = []
    follower = None

    def __init__(self):
        self.visited = [(0,0)]
        self.position = (0,0)

    def move(self, direction, distance):
        if distance > 0:
            if direction == "R":
                self.position = (self.position[0]+1, self.position[1])
            elif direction == "L":
                self.position = (self.position[0]-1, self.position[1])
            elif direction == "U":
                self.position = (self.position[0], self.position[1]+1)
            else:
                self.position = (self.position[0], self.position[1]-1)
            self.visited.append(self.position)
            if self.follower is not None:
                self.follower.follow(self.position)
            self.move(direction, distance-1)
    
    def follow(self, leader):
        xdist = leader[0] - self.position[0]
        ydist = leader[1] - self.position[1]
        
        dist = math.dist(leader,self.position)
        if dist >= 2:
            if xdist > 0:
                self.position = (self.position[0] + 1, self.position[1])
            elif xdist < 0:
                self.position = (self.position[0] - 1, self.position[1])
            if ydist > 0:
                self.position = (self.position[0], self.position[1] + 1)
            elif ydist < 0:
                self.position = (self.position[0], self.position[1] - 1)
            self.visited.append(self.position)
        if self.follower is not None:
            self.follower.follow(self.position)

    def add_follower(self, follower):
        if self.follower is None:
            self.follower = follower
        else:
            self.follower.add_follower(follower)

    def get_tail_position(self):
        if self.follower is None:
            return self.position
        else:
            return self.follower.get_tail_position()
    
    def get_tail_visits(self):
        if self.follower is None:
            return len(set(self.visited))
        else:
            return self.follower.get_tail_visits()
    
p1_rope_length = 2
p1_rope = Node()

for _ in range(p1_rope_length-1):
    p1_rope.add_follower(Node())

p2_rope_length = 10
p2_rope = Node()

for _ in range(p2_rope_length-1):
    p2_rope.add_follower(Node())


for line in f:
    direction = line.split(" ")[0]
    distance = int(line.split(" ")[1])
    p1_rope.move(direction, distance)
    p2_rope.move(direction, distance)



p1 = p1_rope.get_tail_visits()

print("part 1: ", p1)

p2 = p2_rope.get_tail_visits()

print("part 2: ", p2)