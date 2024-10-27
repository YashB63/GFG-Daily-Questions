class Solution:
    def maxChildren(self, greed, cookie):
        g = greed
        s = cookie
    
        g.sort() 
        s.sort() 
    
    
        cookie_count = 0
    
        child = 0
        cookie = 0
        while cookie < len(s) and child < len(g):
            while cookie < len(s) and s[cookie] < g[child]:
                cookie += 1
    
            if cookie == len(s):
                return cookie_count 
    
            cookie_count += 1
            child += 1
            cookie += 1
    
        return cookie_count