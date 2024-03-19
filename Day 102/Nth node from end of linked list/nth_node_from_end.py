def getNthFromLast(head,n):
    
    curr = head
    count = 0
    
    while curr != None:
        count+=1
        curr = curr.next
        
    curr = head  
    
    if count < n:
        return -1
       
    for i in range(1,(count-n+1)):
        curr = curr.next
        
    return curr.data