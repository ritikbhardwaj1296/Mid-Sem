import math
# Equation for line
def line_eq(x1, y1):
    slope = (y1[1] - x1[1]) / (y1[0] - x1[0])
    #y = slope * (x - x1[0]) + x1[1]
    return [slope, -1, (x1[1]-x1[0]*slope)]    

# Eucledian distance between two points
def dist_fn(x, y):
    d = math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
    return d

# Perpendicular distance between a point and a line segment
# L = [a, b, c] coefficients of the line L
def perp_dist(x1, L):
    perp = abs(L[0] * x1[0] + L[1] * x1[1] + L[2]) / math.sqrt(L[0]**2 + L[1]**2)
    return perp


# Perpendicular distance from a polygon
# L = [[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]]
def polygon_perp_dist(x1, L):
    dist_dct = {}
    for i in L:
        dist = perp_dist(x1, i)
        dist_dct.update({i: dist})
    min_dist = min(dist_dict.values())
    dist_dct_1 = {}
    for j, k in dist_dct.items():
        dist_dct_1.update({k: j})
    return min_dist, min_dct_1[min_dist]

# Tangent vector to a polygon
# Coord = [(a1, b1), (a2, b2), (a3, b3), (a4, b4)]
def tan_vec(x1, Coord):
    L = []
    for i in range(len(Coord)):
        line = line_eq(Coord[i], Coord[i-1])
        L.append(line)
    perp_dist, close_line = polygon_perp_dist(x1, L)
    fin_coord = []
    count = 0
    for j in L:
        if j == close_line:
            fin_coord.append(coord[count])
            fin_coord.append(coord[count-1])
            break
        count += 1
    tan_1 = line_eq(x1, fin_coord[0])
    tan_2 = line_eq(x1, fin_coord[1])
    
    return tan_1, tan_2
        
    
            
    