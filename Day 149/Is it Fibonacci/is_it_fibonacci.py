def fun(N, K, GeekNum):
    currWindow = GeekNum
    if N<=K:
        return currWindow[-1]

    currSum = sum(currWindow)
    currWindow.append(currSum)
    start, end = 0, K
    while(end < N-1):
        currSum = currSum + currWindow[end]- currWindow[start]
        currWindow.append(currSum)
        start += 1
        end += 1
    return currWindow[-1]
    
class Solution():
    def solve(self, N, K, GeekNum):
        return fun(N, K, GeekNum)