class Solution():
    def cloneGraph(self, node):
        if not node:
            return None
            
        visited = {}
        
        def dfs(current_node):
            if current_node in visited:
                return visited[current_node]
                
            clone = Node(current_node.val)
            visited[current_node] = clone
            
            for neighbor in current_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
                
            return clone
            
            
        return dfs(node)