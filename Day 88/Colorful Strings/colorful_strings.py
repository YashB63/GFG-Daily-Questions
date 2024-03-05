class Solution:
    def possibleStrings(ob, n, red, blue, green):
        
        def f(num,d1,d2,d3):
            if d1>=d2 and d1>=d3:
                r=d1+1
                x,y=d2,d3
            elif d2>=d3:
                r=d2+1
                x,y=d1,d3
            else:
                r=d3+1
                x,y=d1,d2
            
            up=d1=d2=1
            for i in range(r,num+1):
                up*=i
            for i in range(1,max(2,x+1)):
                d1*=i
            for i in range(1,max(2,y+1)):
                d2*=i
            res=(up//d1)//d2
            return res
        
        x=n-red-blue-green
        ans=0
        for r in range(x+1):
            for b in range(x-r+1):
                ans+=f(n,red+r,blue+b,green+x-r-b)
                
        return ans