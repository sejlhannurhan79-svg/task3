import math

def show(point):
    print("(", point[0], ",", point[1], ")")

def move(point, new_x, new_y):
    return (new_x, new_y)

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


a, b = map(int, input().split())
p1 = (a, b)
show(p1)

c, d = map(int, input().split())
p1 = move(p1, c, d)
show(p1)

e, f = map(int, input().split())
p2 = (e, f)

print(f"{dist(p1, p2):.2f}")