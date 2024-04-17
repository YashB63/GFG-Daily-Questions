class Solution:

    def candyStore(self, candies,N,K):
        
        candies.sort()
        buy=0
        free=N-1
        mini=0
        while (buy<=free):
            mini+=candies[buy]
            buy+=1
            free-=K
        buy=N-1
        free=0
        maxi=0
        while (free<=buy):
            maxi+=candies[buy]
            buy-=1
            free+=K
        return [mini,maxi]