def quickSort(head):
    def solvesort(hd, tmp):
        if not hd or hd==tmp or hd.next == tmp:
            return hd
        x = hd.data
        d = Node(0)
        d.next = hd
        prev, w = d, hd
        
        while w != tmp:
            new = w.next
            if w.data < x:
                prev.next = w.next
                w.next = d.next
                d.next = w
            else:
                prev = prev.next
            w = new
        
        hd.next = solvesort(hd.next, tmp)
        return solvesort(d.next, hd)
    
    return solvesort(head, None)