def compute(head): 
    
    val = ""
    while head:
        val += head.data 
        head = head.next
    if val[::-1] == val:
        return 1
    else:
        return 0