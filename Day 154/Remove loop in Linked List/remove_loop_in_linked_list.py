class Solution:
    
    def removeLoop(self, h):
        
        rethead = h
        s = set()
        prev = None
        while h:
            
            if h in s:
                prev.next = None
                return rethead

            s.add(h)
            prev = h
            h = h.next

        return rethead
