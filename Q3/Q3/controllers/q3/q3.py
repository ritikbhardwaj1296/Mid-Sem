import math
import sys

# Eucledian distance between two points
def dist_fn(x, y):
    d = math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
    return d
visibility_graph = {'A': {'B', 'D', 'E', 'F', 'H'},
                    'B': {'A', 'C', 'E', 'F', 'J'},
                    'C': {'B', 'D', 'J', 'I', 'H', 'E', 'G'},
                    'D': {'A', 'C', 'E', 'H', 'I', 'G'},
                    'E': {'A', 'D', 'B', 'F', 'S', 'H', 'J', 'K'},
                    'F': {'A', 'B', 'C', 'E', 'J', 'K', 'S', 'H'},
                    'G': {'C', 'D', 'H', 'I', 'J'},
                    'H': {'A', 'C', 'D', 'E', 'I', 'K', 'F', 'J', 'G', 'S'},
                    'I': {'C', 'D', 'G', 'H', 'J', 'K'},
                    'J': {'B', 'C', 'D', 'E', 'S', 'K', 'I', 'G', 'H', 'F'},
                    'K': {'E', 'F', 'J', 'S', 'I', 'H'},
                    'S': {'E', 'F', 'H', 'J', 'K'}
    }

coor_dct = {'A': (0, 0),
            'B': (40, 0),
            'C': (40, 40),
            'D': (0, 40),
            'E': (14, 6),
            'F': (29, 6),
            'G': (21.3, 26.15),
            'H': (14, 21),
            'I': (23, 21),
            'J': (29, 17.5),
            'K': (19, 17.5),
            'S': (21.3, 10.26),
            'alpha': (21.3, 17.5),
            'beta': (19.5, 21)
    }

weighted_graph = {}

for i in visibility_graph.keys():
    w_g = {}
    for j in visibility_graph[i]:
        d = dist_fn(coor_dct[i], coor_dct[j])
        w_g.update({j:d})
    weighted_graph.update({i: w_g})
    
#print(weighted_graph)

# Shortest path (Dijkstra)

def dijkstra_algorithm(start_node, weighted_graph):
    unvisited_nodes = []
    for i in weighted_graph.keys():
        unvisited_nodes.append(i)
 
    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}
 
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
 
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = []
        for i in weighted_graph[current_min_node].keys():
            neighbors.append(i)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + weighted_graph[current_min_node][neighbor]
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append((node))
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append((start_node))
    
    print("The shortest path using visibility graph has a cost value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))
    y = list(reversed(path))
    
    return y, shortest_path[target_node]

start_node = 'S'
target_node = 'G'
prev_n, shrt_path = dijkstra_algorithm(start_node, weighted_graph)
path_lst, cost = print_result(prev_n, shrt_path, start_node, target_node)


path_0 = ['S', 'alpha', 'K', 'beta', 'I', 'G']

#print(path_0[1])
path_0_dist = 0
for i in range(len(path_0)-1):
    dst = dist_fn(coor_dct[path_0[i]], coor_dct[path_0[i+1]])
    path_0_dist += dst
    
print(f"The distance using bug 0 is {path_0_dist}")

import matplotlib.pyplot as plt
fig = plt.figure()
ax  = fig.add_subplot(111)



ax.plot([14,14], [6,21],linewidth=7.0,c='b')

ax.plot([14,29], [6,6],linewidth=7.0,c='b')
ax.plot([29,29], [6,17.5],linewidth=7.0,c='b')
ax.plot([19,29], [17.5,17.5],linewidth=7.0,c='b')
ax.plot([14,23], [21,21],linewidth=7.0,c='b')
ax.plot(21.3, 10.26, marker="o", markersize=20, markeredgecolor="red", markerfacecolor="green")
ax.plot(21.3, 26.15, marker="o", markersize=20, markeredgecolor="red", markerfacecolor="red")

  



x = 1    
for i in  visibility_graph.keys():
  for j in visibility_graph[i]:
    
    if x==1:
        ax.plot([coor_dct[i][0],coor_dct[j][0]], [coor_dct[i][1],coor_dct[j][1]],c='black',label="Visibility graph")
    else:
        ax.plot([coor_dct[i][0],coor_dct[j][0]], [coor_dct[i][1],coor_dct[j][1]],c='black')
    x= 2
    
        
x = 1 
lst = ["S","K","I","G"]
for i in range(len(lst)-1):
  if x==1:
      ax.plot([coor_dct[lst[i]][0],coor_dct[lst[i+1]][0]],[coor_dct[lst[i]][1],coor_dct[lst[i+1]][1]],linewidth=3.0,c='yellow',label="shortest path")
  else:
      ax.plot([coor_dct[lst[i]][0],coor_dct[lst[i+1]][0]],[coor_dct[lst[i]][1],coor_dct[lst[i+1]][1]],linewidth=3.0,c='yellow')
  x=2
      
x=1
lst1 = ["S","alpha","K","beta","I","G"]
for i in range(len(lst1)-1):
  if x==1:
      ax.plot([coor_dct[lst1[i]][0],coor_dct[lst1[i+1]][0]],[coor_dct[lst1[i]][1],coor_dct[lst1[i+1]][1]],linewidth=3.0,c='orange',label="Bug 0 path")
  else :
      ax.plot([coor_dct[lst1[i]][0],coor_dct[lst1[i+1]][0]],[coor_dct[lst1[i]][1],coor_dct[lst1[i+1]][1]],linewidth=3.0,c='orange')
  x=2
ax.legend(loc='upper center')
 
plt.show()


















