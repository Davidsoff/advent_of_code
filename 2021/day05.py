from functools import reduce

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def add_to(field, x,y,width):
    idx = (y*width)+x
    field[idx] += 1

def add_line(line, field, width):
    xmin = min(line[0], line[2])
    xmax = max(line[0], line[2])
    ymin = min(line[1], line[3])
    ymax = max(line[1], line[3])
    
    xrange = [line[0]] if line[0] == line[2] else range(xmin, xmax+1)
    yrange = [line[1]] if line[1] == line[3] else range(ymin, ymax+1)
    for x in xrange:      
        for y in yrange:
            add_to(field,x ,y,width)

def add_diagonal(line, field, width):
    xdir = -1 if line[0] > line[2] else 1
    ydir = -1 if line[1] > line[3] else 1

    xrange = list(range(line[0], line[2]+xdir, xdir))
    yrange = list(range(line[1], line[3]+ydir, ydir))

    for i in range(0,len(xrange)):
        x = xrange[i]
        y = yrange[i]
        add_to(field,x ,y,width)

def print_field(field, width):
    print('\n'.join(' '.join("." if x == 0 else str(x) for x in row) for row in chunks(field, width)))
    print()

f = open('input/day05.txt', 'r')

coords = [list(map(int, x.replace(" -> ", ",").split(","))) for x in f]
xs = reduce(list.__add__, [[x[0], x[2]] for x in coords])
ys = reduce(list.__add__, [[x[1], x[3]] for x in coords])

horizontal = [x for x in coords if x[1]==x[3]]
vertical = [x for x in coords if x[0]==x[2]]
diag = [x for x in coords if x[0]!=x[2] and x[1]!=x[3]]
not_diag = horizontal + vertical

height = max(ys)+1
width = max(xs)+1
field = [0 for _ in range(0,height*width)]

for l in not_diag:
    add_line(l, field, width)

points = [x for x in field if x >= 2]
print(len(points))

for l in diag:
    add_diagonal(l, field, width)

points = [x for x in field if x >= 2]
print(len(points))