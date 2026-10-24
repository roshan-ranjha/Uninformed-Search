graph={'A':['B','C'],
       'B':['D','E','F'],
       'C':['G','H'],
       'D':[],
       'E':['I'],
       'F':[],
       'G':[],
       'H':[],
       'I':[]
       }

def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited=set()
    print(start)
    visited.add(start)
    if start==goal:
        print("Goal Found!!")
        return True
    for neighbour in graph[start]:
        if neighbour not in visited:
         if dfs(graph,neighbour,goal, visited):
            return True
    return False

dfs(graph,'A', 'G')