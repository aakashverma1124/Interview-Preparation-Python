class DepthFirstSearch:

    def build_graph(v, edges):
        graph = []
        for i in range(v):
            graph.append(list())
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return graph

    def dfs(node, visited, graph, dfs_ans):
        visited[node] = True
        dfs_ans.append(node)

        for nbr in graph[node]:
            if not visited[nbr]:
                DepthFirstSearch.dfs(nbr, visited, graph, dfs_ans)

    def depth_first_search(v, edges, src):
        graph = DepthFirstSearch.build_graph(v, edges)
        visited = [False] * v
        components = []
        for node in range(v):
            if not visited[node]:
                dfs_ans = []
                DepthFirstSearch.dfs(node, visited, graph, dfs_ans)
                components.append(dfs_ans)
        # print(visited)
        return components

if __name__ == '__main__':
    v = 13
    edges = [[0, 1], [0, 2], [0, 5], [1, 3], [1, 5], [2, 3], [3, 4], [4, 5], [6, 7], [8, 9], [9, 10], [11, 12]]
    print(DepthFirstSearch.depth_first_search(v, edges, 0))
