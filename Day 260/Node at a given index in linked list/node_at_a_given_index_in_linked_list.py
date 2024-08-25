class Solution:
    def GetNth(self, head, index):
        if index == 1:
            return head.data
        
        i = 1
        cur = head
        while i <index:
            if cur :
                cur = cur.next 
                i +=1
            else :
                return -1
        return cur.data