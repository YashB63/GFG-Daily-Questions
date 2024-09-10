class Solution:
    def linkdelete(self, head, n, m):
        nn,mm=n,m
        
        arr=[]
        while head:
            if mm==0:
                if nn>0:
                    nn-=1
                if nn==0:
                    nn,mm=n,m
            else:
                mm-=1
                arr.append(head)
            head=head.next
        
        
        for i in range(len(arr)-1):
            arr[i].next=arr[i+1]
        
        arr[-1].next=None
        
        return arr[0]