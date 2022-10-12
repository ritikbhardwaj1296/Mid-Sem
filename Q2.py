# -*- coding: utf-8 -*-
import math

init_rob = (10, 10)
rob_area = 0.4
vel = 5

C1 = [(0,0), (10, 0), (0, 40), (10, 40)]
C2 = [(10,34), (11.7, 34), (10, 40), (11.7, 40)]
C3 = [(11.7,20), (24, 20), (11.7, 40), (24, 40)]
C4 = [(11.7,7), (24, 7), (11.7, 20), (24, 20)]
C5 = [(24,7), (30, 7), (24, 40), (30, 40)]
C6 = [(30,34), (32, 34), (30, 40), (32, 40)]
C7 = [(32,0), (40, 0), (32, 40), (40, 40)]
C8 = [(10,0), (32, 0), (10, 7), (32, 7)]

L = [C1, C2, C3, C4, C5, C6, C7, C8]

def dist_fn(x, y):
    d = math.sqrt((x[0] - y[0])**2 + (x[1] + y[1])**2)
    return d

def center_cell(cell):
    c = (cell[0][0] + cell[1][0]) / 2, (cell[0][1] + cell[2][1]) / 2
    return c

def move_cell(cell, rob_area):
    #center = center_cell(cell)
    area_cell = abs(cell[0][0] - cell[1][0]) * abs(cell[0][1] - cell[2][1])
    distance = area_cell / rob_area
    #dist = dist_fn(center, cell[0])
    total_dist = distance
    return total_dist

tot_dist = 0
for i in range(len(L)-1):
    ds = 0
    d1 = dist_fn(init_rob, L[i+1][1])
    d2 = move_cell(L[i], rob_area)
    ds = d1 + d2
    
    tot_dist += ds
    init_rob = L[i][-1]
    
print(f"total distance is : {tot_dist} meters")
print(f"Total time is : {tot_dist / vel} seconds")
    


