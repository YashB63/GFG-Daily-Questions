class Solution():
    def isCompleteBT(self, root):
        q= deque()
        q.append(root)
        f=0
        while q :
            curr=q.popleft()
            if(curr==None):
                f=1
            else:
                if(f==1):
                  return False
                q.append(curr.left)
                q.append(curr.right)
        return True