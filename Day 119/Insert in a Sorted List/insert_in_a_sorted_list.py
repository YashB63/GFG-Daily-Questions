class Solution:
    def sortedInsert(self, head1,key):
        
        if head1==None:
            return head1
        curr=head1
        prev=None
        while curr and curr.data<key:
            prev=curr
            curr=curr.next
        ins_node=Node(key)
        if prev==None:
            ins_node.next=head1
            head1=ins_node
            return head1
            
       
        ins_node.next=curr
        prev.next=ins_node
        return head1