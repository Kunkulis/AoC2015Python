distances = open("input.txt").readlines()

def prep_distances(distances:list[str]):
    split_distance = []
    for line in distances:
        split_line = line.strip().split()
        split_distance.append((split_line[0],split_line[2],int(split_line[-1])))
    
    graph = build_graph(split_distance)
    return graph

def build_graph(distances):
    graph={}
    for city1, city2, distance in distances:
        if city1 not in graph:
            graph[city1]={}
        if city2 not in graph:
            graph[city2]={}
        graph[city1][city2]=distance
        graph[city2][city1]=distance
    return graph

def dfs(graph,node,current_distance, visited, shortest_longest_distances):    

    visited.add(node)        
    if len(visited)==len(graph): 
        shortest_longest_distances[0] = max(shortest_longest_distances[0], current_distance)
        shortest_longest_distances[1] = min(shortest_longest_distances[1], current_distance)
    else:
        for neighbor, distance in graph[node].items():
            if neighbor not in visited:
                dfs(graph, neighbor, current_distance + distance, visited, shortest_longest_distances)
    
    visited.remove(node)  

def part1(distances:list[str]) -> int:
    graph = prep_distances(distances)
    shortest_longest_distances = [0, float('inf')]

    for node in graph:
        dfs(graph,node,0,set(),shortest_longest_distances)    
    return shortest_longest_distances

print(part1(distances))