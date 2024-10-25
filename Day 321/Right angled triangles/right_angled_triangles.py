class Solution:
    def rightAngTri(self, a, b, c): 
        if a+b<c or a+c<b or b+c<a:
            return 'No'
        li = [a,b,c]
        li.sort()
        if li[0]**2 + li[1]**2 ==li[2]**2:
            return 'Yes'
        return 'No'