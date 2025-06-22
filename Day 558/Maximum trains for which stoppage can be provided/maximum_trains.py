class Solution():
    def maxStop(self, n, m, trains):
        plateforms = [[] for i in range(n)]
        
        for i in range(m):
            plateforms[trains[i][2]-1].append(trains[i])
        ans = 0
        
        for plateform in plateforms:
            plateform.sort(key=lambda x:x[1])
            prevStart = -1
            
            for train in plateform:
                if train[0] >= prevStart:
                    ans += 1
                    prevStart = train[1]
        return ans