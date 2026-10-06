import random

def deformation(num_points):
    points = []
    for i in range(num_points):
        points.append(random.randint(-10,10))
    return points