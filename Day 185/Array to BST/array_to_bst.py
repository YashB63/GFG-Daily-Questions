class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
	    
    def sortedArrayToBSTUtil(self, nums, l, r, root):
        if l>r: return None
        mid = (l+r)//2
        node = Node(nums[mid])
        if root[0] is None: root[0] = node
        node.left = self.sortedArrayToBSTUtil(nums, l, mid-1, root)
        node.right = self.sortedArrayToBSTUtil(nums, mid+1, r, root)
        return node
    
    def preorder(self, root, nodes):
        if not root: return
        nodes.append(root.data)
        self.preorder(root.left, nodes)
        self.preorder(root.right, nodes)
        
    def sortedArrayToBST(self, nums):
        root = [None]
        self.sortedArrayToBSTUtil(nums, 0, len(nums)-1, root)
        nodes = []
        self.preorder(root[0], nodes)
        return nodes