class Solution:
    def cloneLinkedList(self, head):
        hash={}
        cur=head
        while cur:
            hash[cur]=Node(cur.data)
            cur=cur.next
        
        cur=head
        while cur:
            hash[cur].next=hash.get(cur.next,None)
            hash[cur].random=hash.get(cur.random,None)
            cur=cur.next
        
        return hash.get(head,None)