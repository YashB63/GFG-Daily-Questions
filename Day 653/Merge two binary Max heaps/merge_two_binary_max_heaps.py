class Solution():
    def heapify(self,a,n,i):
        parent=i   

        lchild=(2*i)+1   
        rchild=(2*i)+2   

        if lchild<=n-1 and a[lchild]>a[parent]:
            parent=lchild

        if rchild<=n-1 and a[rchild]>a[parent]:
            parent=rchild

        if i!=parent:
            a[parent],a[i]=a[i],a[parent]
            self.heapify(a,n,parent)

    def mergeHeaps(self, a, b, n, m):
        a+=b   
        for  i in range(int(len(a)/2-1),-1,-1):
          self.heapify(a,len(a),i)
        return a