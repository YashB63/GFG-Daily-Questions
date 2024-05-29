def graphColoring(graph, k, V):
    
    def valid(color, vertex, color_chart):
        for destination in range(V):
            if graph[vertex][destination] == 1 and color_chart[destination] == color:
                return False
        return True
    def dfs(vertex, color_chart):
        if vertex == V:
            return True
        for color in range(k):
            if valid(color, vertex, color_chart):
                color_chart[vertex] = color
                if dfs(vertex+1, color_chart):
                    return True
                color_chart[vertex] = -1
        return False
    return dfs(0, [-1]*V)