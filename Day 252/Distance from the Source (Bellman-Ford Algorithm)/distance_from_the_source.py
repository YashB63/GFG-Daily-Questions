class Solution:
    def bellman_ford(self, V, edges, S):
        if V==0:
            return -1
        if V==1:
            return 1
        distances = [float('inf')]*V
        distances[S] = 0
        
        for i in range(V-1):
            for source,destination,weight in edges:
                new_distance = distances[source] +weight
                if new_distance<distances[destination]:
                    distances[destination] = new_distance
                    
        for source,destination,weight in edges:
            new_distance = distances[source] +weight
            if new_distance<distances[destination]:
                return [-1]
        for i in range(V):
            distances[i] = min(distances[i],10**8)
            
        return distances