class Solution:
    def topDown(self, n):
        hmap = {}
        def helper(num,hmap):
            if num<=0:
                return 0
            if num == 1:
                return 1
            if num in hmap:
                return hmap[num]
            hmap[num] = (helper(num-1,hmap)+helper(num-2,hmap))%(10**9+7)
            return hmap[num]
        return helper(n,hmap)
        
    def bottomUp(self, n):
        a,b,temp = 0,1,1
        for i in range(2,n+1):
            temp = (a+b)%(10**9+7)
            a = b
            b = temp
            
        return temp