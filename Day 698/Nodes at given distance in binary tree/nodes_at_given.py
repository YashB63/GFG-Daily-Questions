class Solution:
    def __init__(self):
        pass

    def newNode(self, val):
        return Node(val)
    
    def buildTree(self, s):
        if len(s) == 0 or s[0] == 'N':
            return None
        
        ip = s.split()
        root = self.newNode(int(ip[0]))
        queue = []
        queue.append(root)
        i = 1
        while len(queue) > 0 and i < len(ip):
            currNode = queue.pop(0)
            currVal = ip[i]
            if currVal != 'N':
                currNode.left = self.newNode(int(currVal))
                queue.append(currNode.left)
            i += 1
            if i >= len(ip):
                break
            currVal = ip[i]
            if currVal != 'N':
                currNode.right = self.newNode(int(currVal))
                queue.append(currNode.right)
            i += 1
        return root
    
    def createmapping(self, root, cm, target):
        q = []
        q.append(root)
        cm[root] = None
        ans = None
        
        while len(q) > 0:
            temp = q.pop(0)
            if temp.data == target:
                ans = temp
            if temp.left:
                cm[temp.left] = temp
                q.append(temp.left)
            if temp.right:
                cm[temp.right] = temp
                q.append(temp.right)
        return ans
    
    def check(self, startNode, visited, ans, k, cm):
        if k == 0 or startNode is None:
            if startNode:
                ans.append(startNode.data)
            return
        
        visited[startNode] = True
        
        if not visited.get(startNode.left, False) and startNode.left:
            self.check(startNode.left, visited, ans, k - 1, cm)
        
        if not visited.get(startNode.right, False) and startNode.right:
            self.check(startNode.right, visited, ans, k - 1, cm)
        
        if not visited.get(cm[startNode], False) and cm[startNode]:
            self.check(cm[startNode], visited, ans, k - 1, cm)
    
    def KDistanceNodes(self, root, target, k):
        ans = []
        cm = {}
        st = self.createmapping(root, cm, target)
        visited = {}
        self.check(st, visited, ans, k, cm)
        ans.sort()
        return ans