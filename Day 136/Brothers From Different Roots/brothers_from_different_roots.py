class Solution:
    
    def findInorder(self, root, l):
        if root==None:
            return
        
        self.findInorder(root.left,l)
        l.append(root.data)
        self.findInorder(root.right,l)
        
    def countPairs(self, root1, root2, x): 
        
        l1=[]
        l2=[]
        self.findInorder(root1, l1)
        self.findInorder(root2, l2)
        c=0
        i=0
        j=len(l2)-1
        while(i<len(l1) and j>=0):
            if(l1[i]+l2[j]==x):
                c=c+1
                i=i+1
                j=j-1
            elif(l1[i]+l2[j]>x):
                j=j-1
            else:
                i=i+1
        return(c)