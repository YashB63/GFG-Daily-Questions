class Solution:
    def unvisitedLeaves(self, N, leaves, frogs):
        
        x = [False for _ in range(leaves + 1)]
        for i in frogs:
            if i == 1:
                return 0
            if i <= leaves and not x[i]:
                for j in range(i, leaves + 1, +i):
                    x[j] = True
                    
        return x.count(False) - 1