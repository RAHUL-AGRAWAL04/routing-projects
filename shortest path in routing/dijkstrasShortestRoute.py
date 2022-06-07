# Python program for Dijkstra's single  
# source shortest path algorithm. The program is  
# for adjacency matrix representation of the graph 
  
# Library for INT_MAX 
import sys 
   
class Graph(): 
   
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
   
    def printSolution(self, dist): 
        print ("Vertex Distance from Source") 
        for node in range(self.V): 
            print ('0 to',node, ': Cost :', dist[node]) 
   
   
    def minDistance(self, dist, sptSet): 
   
        # Initilaize minimum distance for next node 
        min = sys.maxsize  
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
   
        return min_index 


    def dijkstra(self, src): 
   
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
   
        for cout in range(self.V): 
            u = self.minDistance(dist, sptSet) 
            sptSet[u] = True
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                    dist[v] = dist[u] + self.graph[u][v] 
   
        self.printSolution(dist) 
   
# Driver program 

print('Dijstra\'s Algo Demonstration')
n = int(input('Enter No of nodes: '))
g = Graph(n)

matrix = []
print('Enter from adjacency matrix...')
for i in range(n):
	matrix.append(list(map(int,input('Enter row for node {}: '.format(i)).split())))

g.graph = matrix
g.dijkstra(0); 
  
