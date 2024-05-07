class Solution:
    def getLevelDiff(self, root):
        
        es = 0
        os = 0
        q = [root]
        odd = True
        while q:
            newlis = []
            for i in q:
                if odd:
                    os += i.data
                else:
                    es += i.data
                if i.left:
                    newlis.append(i.left)
                if i.right:
                    newlis.append(i.right)
            odd ^= True
            q = newlis
        return os - es