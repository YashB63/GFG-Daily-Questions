class Solution:

    def isCircular(self, path):
       
        x=y=0
        d='n'
        for i in path:
            if i=='G' and d=='n': x+=1
            elif i=='G' and d=='s': x-=1
            elif i=='G' and d=='e': y+=1
            elif i=='G' and d=='w': y-=1
            elif i=='L' and d=='n': d='w'
            elif i=='L' and d=='s': d='e'
            elif i=='L' and d=='e': d='n'
            elif i=='L' and d=='w': d='s'
            elif i=='R' and d=='n': d='e'
            elif i=='R' and d=='s': d='w'
            elif i=='R' and d=='e': d='s'
            elif i=='R' and d=='w': d='n'
        return 'Circular' if x==0 and y==0 else 'Not Circular'