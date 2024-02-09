class Solution:
    def sortedInsert(self, head, data):
       
        x = []
        temp = head
        if temp is not None:
            
            x.append(temp.data)
            temp = temp.next
            while(temp != head):
                x.append(temp.data)
                temp = temp.next
            
            for i in range(len(x)):
                if data >= x[i]:
                    if i == (len(x) - 1):
                        x.append(data)
                    pass
                
                else:
                    x.insert(i, data)
                    break
        
        else:
            x.append(data)
            
        res = LinkedList()
        for f in x:
            res.push(f)
            
        return res.head