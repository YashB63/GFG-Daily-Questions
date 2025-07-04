class Solution:
    def deleteDeepest(self, root, d_node):
        q = []
        q.append(root)

        while (len(q)):
            temp = q.pop(0)

            if temp is d_node:
                temp = None
                return

            if temp.right:
                if temp.right is d_node:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)

            if temp.left:
                if temp.left is d_node:
                    temp.left = None
                    return
                else:
                    q.append(temp.left)

    def deleteNode(self, root, key):
        if root is None:
            return None

        if root.left is None and root.right is None:
            if root.data == key:
                return None
            else:
                return root

        key_node = None
        q = []
        q.append(root)

        while (len(q)):
            temp = q.pop(0)

            if temp.data == key:
                key_node = temp

            if temp.left:
                q.append(temp.left)

            if temp.right:
                q.append(temp.right)

        if key_node:
            x = temp.data

            self.deleteDeepest(root, temp)

            key_node.data = x

        return root