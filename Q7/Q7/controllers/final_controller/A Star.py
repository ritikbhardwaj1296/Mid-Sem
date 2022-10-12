import math
def dist_fn(x, y):
    d = math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
    return d

def aStarAlgo(start_node, stop_node):
    open_set = set()
    open_set.add(start_node)
    closed_set = set()
    g = {}               #store distance from starting node
    parents = {}         # parents contains an adjacency map of all nodes
    #distance of starting node from itself is zero
    g[start_node] = 0
    #start_node is root node i.e it has no parent nodes
    #so start_node is set to its own parent node
    parents[start_node] = start_node
    while len(open_set) > 0:
        n = None
        #node with lowest f() is found
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                #nodes 'm' not in first and last set are added to first
                #n is set its parent
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                #for each node m,compare its distance from start i.e g(m) to the
                #from start through n node
                else:
                    if g[m] > g[n] + weight:
                        #update g(m)
                        g[m] = g[n] + weight
                        #change parent of m to n
                        parents[m] = n
                        #if m in closed set,remove and add to open
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n == None:
            print('Path does not exist!')
            return None
        
        # if the current node is the stop_node
        # then we begin reconstructin the path from it to the start_node
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path
        # remove n from the open_list, and add it to closed_list
        # because all of his neighbors were inspected
        open_set.remove(n)
        closed_set.add(n)
    print('Path does not exist!')
    return None

#define fuction to return neighbor and its distance
#from the passed node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
    
    
#for simplicity we ll consider heuristic distances given
#and this function returns heuristic distance for all nodes

graph_dct = {}

a = 2
count = 1
for i in range(10):
    b = 2
    for j in range(10):
        graph_dct.update({count: (b, a)})
        b += 4
        count += 1
    a += 4
    
#print(graph_dct)


heuristicsd = {}

for k in range(1,101):
    d = dist_fn(graph_dct[66], graph_dct[k])
    heuristicsd.update({k: d})
    
#print(heuristic)

Graph_nodes = {}

for l in range(1, 101):
    z = []
    danger = [14, 15, 16, 17, 18, 28, 38, 48, 58, 57, 56, 55, 24, 34, 44, 54, 64, 65, 66]
    if l == 1:
        neighbor = [l+1, l+10, l+11]
        for m in neighbor:
            if (l in danger) or (m in danger):
                dis = 100000
                z.append((m, dis))
            else:
                dis = dist_fn(graph_dct[l], graph_dct[m])
                z.append((m, dis))
            
    elif l == 10:
        neighbor = [l-1, l+10, l+9]
        for m in neighbor:
            if (l in danger) or (m in danger):
                dis = 100000
                z.append((m, dis))
            else:
                dis = dist_fn(graph_dct[l], graph_dct[m])
                z.append((m, dis))
            
    elif l == 91:
        neighbor = [l+1, l-10, l-9]
        for m in neighbor:
            if (l in danger) or (m in danger):
                dis = 100000
                z.append((m, dis))
            else:
                dis = dist_fn(graph_dct[l], graph_dct[m])
                z.append((m, dis))
            
    elif l == 100:
        neighbor = [l-1, l-10, l-11]
        for m in neighbor:
            if (l in danger) or (m in danger):
                dis = 100000
                z.append((m, dis))
            else:
                dis = dist_fn(graph_dct[l], graph_dct[m])
                z.append((m, dis))
    
    elif l in [2, 3, 4, 5, 6, 7, 8, 9]:
        neighbor = [l+1, l-1, l+10, l+11, l+9]
        for m in neighbor:
            if (l in danger) or (m in danger):
                dis = 100000
                z.append((m, dis))
            else:
                dis = dist_fn(graph_dct[l], graph_dct[m])
                z.append((m, dis))
            
    elif l in [11, 21, 31, 41, 51, 61, 71, 81, 91]:
        neighbor = [l+1, l+10, l-10, l-9, l+11]
        for m in neighbor:
            if (l in danger) or (m in danger):
                dis = 100000
                z.append((m, dis))
            else:
                dis = dist_fn(graph_dct[l], graph_dct[m])
                z.append((m, dis))
            
    elif l in [20, 30, 40, 50, 60, 70, 80, 90]:
        neighbor = [l-1, l+10, l-10, l-11, l+9]
        for m in neighbor:
            if (l in danger) or (m in danger):
                dis = 100000
                z.append((m, dis))
            else:
                dis = dist_fn(graph_dct[l], graph_dct[m])
                z.append((m, dis))
            
    elif l in [92, 93, 94, 95, 96, 97, 98, 99]:
        neighbor = [l-1, l-10, l+1, l-11, l-9]
        for m in neighbor:
            if (l in danger) or (m in danger):
                dis = 100000
                z.append((m, dis))
            else:
                dis = dist_fn(graph_dct[l], graph_dct[m])
                z.append((m, dis))
            
    else:
        neighbor = [l-10, l-11, l-9, l-1, l+1, l+10, l+9, l+11]
        for m in neighbor:
            if (l in danger) or (m in danger):
                dis = 100000
                z.append((m, dis))
            else:
                dis = dist_fn(graph_dct[l], graph_dct[m])
                z.append((m, dis))
            
    Graph_nodes.update({l: z})





def heuristic(n):
    return heuristicsd[n]

#Describe your graph here
# =============================================================================
# Graph_nodes = {
#     'A': [('B', 6), ('F', 3)],
#     'B': [('A', 6), ('C', 3), ('D', 2)],
#     'C': [('B', 3), ('D', 1), ('E', 5)],
#     'D': [('B', 2), ('C', 1), ('E', 8)],
#     'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
#     'F': [('A', 3), ('G', 1), ('H', 7)],
#     'G': [('F', 1), ('I', 3)],
#     'H': [('F', 7), ('I', 2)],
#     'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
# }
# =============================================================================
#print(Graph_nodes)
path_11 = aStarAlgo(11, 66)

#print(path_11)
coordinatesdf = []
for i in path_11:
    crd = graph_dct[i]
    coordinatesdf.append(crd)
    
#print(coordinatesdf)
real_coord = []
for vc in coordinatesdf:
    a = vc[0]
    b = vc[1]
    if a < 20:
        a = a - 20
    elif a >= 20:
        a = a - 20 
    if b < 20:
        b = b - 20
    elif b >= 20:
        b = b -20
    real_coord.append((a, b))

print(real_coord)



