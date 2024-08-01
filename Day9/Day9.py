distances = open("test.txt").readlines()

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

def dfs(graph):

def bfs(graph):

def dijkstra(graph):
    

def part1(distances:list[str]) -> int:
    graph = prep_distances(distances)



    return 0

print(part1(distances))