class Solution:
    def printTable(self, n):
        multiplier = 10
        while(multiplier):
            print(n*multiplier,end=" ")
            multiplier-=1
        print()