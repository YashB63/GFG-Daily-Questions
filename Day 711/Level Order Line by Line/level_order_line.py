import queue

class Solution:
    def levelOrder(self, root):
        result = []

        q = queue.Queue()
        q.put(root)

        while q.qsize():
            curr_level_size = q.qsize()

            level = []

            for i in range(curr_level_size):
                curr_node = q.get()
                level.append(curr_node.data)

                if curr_node.left:
                    q.put(curr_node.left)

                if curr_node.right:
                    q.put(curr_node.right)

            result.append(level)

        return result