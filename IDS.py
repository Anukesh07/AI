from collections import defaultdict 
class Graph: 
    def __init__(self,vertices):  
        self.V = vertices 
        self.graph = defaultdict(list) 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    def DLS(self,src,target,maxDepth): 
        if src == target : return True 
        if maxDepth <= 0 : return False
        for i in self.graph[src]: 
                if(self.DLS(i,target,maxDepth-1)): 
                    return True
        return False 
    def IDS(self,src, target, maxDepth):
        for i in range(maxDepth): 
            if (self.DLS(src, target, i)): 
                return True
        return False 
k = input("Enter the number of vertices: \n")
g = Graph(int(k))
for i in range(int(k)-1):
    u, v = input("Enter the values of u and v: \n").split()
    g.addEdge(int(u), int(v))
target = input("Enter the target: \n")
maxDepth = input("Enter the maximum depth: \n")
src = input("Enter the source: \n")
if g.IDS(int(src), int(target), int(maxDepth)) == True:
    print("Target is reachable from source " +
          "for the given max depth")
else:
    print("Target is not reachable from source " +
          "for the given max depth!")
