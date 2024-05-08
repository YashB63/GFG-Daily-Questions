class Solution:
   
    def serialize(self, root):
        
        q=deque()
        arr=[]
        q.append(root)
        while q:
            for i in range(len(q)):
                curr=q.popleft()
                if curr:
                    arr.append(str(curr.data))
                    q.append(curr.left)
                    q.append(curr.right)
                else:
                    arr.append('N')
        return arr
    
    def deSerialize(self, a):
        
        return buildTree(" ".join(a))