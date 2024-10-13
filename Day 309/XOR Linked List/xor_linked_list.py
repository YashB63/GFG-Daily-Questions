def insert(head, data):
    r=Node(data)
    r.npx=head
    return r
    
def getList(head):
    q=[]
    while head:
        q.append(head.data)
        head=head.npx
    return q