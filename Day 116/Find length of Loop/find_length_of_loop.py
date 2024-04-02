def countNodesinLoop(head):
   
    dummy = Node(None)
    dummy.next = head
    head = dummy
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    if fast == None or fast.next == None:
        return 0
    else:
        fast = head 
        while fast != slow:
            fast = fast.next
            slow = slow.next
        n = 0 
        while fast:
            fast = fast.next
            n += 1
            if fast == slow:
                break
    return n