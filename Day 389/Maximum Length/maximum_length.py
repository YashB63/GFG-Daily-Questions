class Solution():
    def solve(self, a, b, c):
        maximum=max(a,b,c)
        if(maximum>2*(a+b+c+1-maximum)):
            return -1
        else:
            return (a+b+c)