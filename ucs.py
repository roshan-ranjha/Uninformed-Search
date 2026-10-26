import heapq

graph={'S':[('A',5),('B',3)],
       'A':[('C',2),('D',4)],
       'B':[('E',5),('F',7)],
       'C':[],
       'D':[('R',6),('G',8)],
       'E':[('G',4)],
       'F':[],
       'R':[],
       'G':[]
       }
def ucs(graph, start, goal):
    pq=[]
    visited=set()
    cost={start:0}
    parent={start:None}
    heapq.heappush(pq,(0,start))
    while pq:
        current_cost,current=heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        if current==goal:
            path=[]
            while current is not None:
                path.append(current)
                current=parent[current]
            path.reverse()
            return path, current_cost
        for neighbour,edge_cost in graph[current]:
            if neighbour not in visited:
                new_cost=edge_cost + current_cost
                if neighbour not in cost or new_cost<cost[neighbour]:
                    cost[neighbour]=new_cost
                    parent[neighbour]=current
                    heapq.heappush(pq,(new_cost,neighbour))
        
path_traveled, total_cost= ucs(graph,'S','R')
print("Path Traversed: ",path_traveled)
print("Total Cost: ", total_cost)
print("Length of path: ",len(path_traveled)-1)
