class Solution:
    def sortedListToBST(self, head):
        lis=[]
        
        while head:
            lis.append(head.data)
            head=head.next
        def B(lis):
            if len(lis)==1:
                return TNode(lis[0])
            
            mid=len(lis)//2
            node=TNode(lis[mid])
            
            node.left=B(lis[:mid])
            if mid+1<len(lis):
                node.right=B(lis[mid+1:])
            return node
        return B(lis)