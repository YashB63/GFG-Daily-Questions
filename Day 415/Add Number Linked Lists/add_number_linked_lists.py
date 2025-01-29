class Solution:
    def reverse(self,Head): 
        cur = Head
        prv = None
        nxt = None
        while cur:
            nxt = cur.next
            cur.next = prv
            prv = cur
            cur = nxt
        
        return prv
            
    def addTwoLists(self, l1, l2):
        if l1 is None: 
            return l1 
        if l2 is None: 
            return l2 
      
        l1 = self.reverse(l1) 
      
        l2 = self.reverse(l2) 
      
        head = l1 
        prev = None
        c = 0
        Sum = 0
          
        while l1 is not None and l2 is not None: 
            Sum = c + l1.data + l2.data 
            l1.data = Sum % 10
            c = int(Sum / 10) 
            prev = l1 
            l1 = l1.next
            l2 = l2.next
              
        if l1 is not None or l2 is not None: 
            if l2 is not None: 
                prev.next = l2 
            l1 = prev.next
              
            while l1 is not None: 
                Sum = c + l1.data 
                l1.data = Sum % 10
                c = int(Sum / 10) 
                prev = l1 
                l1 = l1.next
                  
        if c > 0: 
            prev.next = Node(c) 
              
        res = self.reverse(head) 
        while res.data == 0:
            res = res.next
            
        return res