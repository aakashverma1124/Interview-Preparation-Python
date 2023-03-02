class DepthFirstSearch :
    
    def buildGraph(v,edges):
        graph = [[] for _ in range(v+1)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return graph
    
    
    def dfs(node, visited, graph,d):
        visited[node] = True
        d.append(node)
        for nbr in graph[node]:
            if not visited[nbr]:
                DepthFirstSearch.dfs(nbr,visited,graph,d)
    
    @staticmethod
    def depthFirstSearch(v, edges, src):
        graph = DepthFirstSearch.buildGraph(v, edges)
        visited = [False]*(v+1)
        d = []
        for i in range(1,v+1):
            if not visited[i]:
                DepthFirstSearch.dfs(i, visited, graph, d)
        return d
    
if __name__ == '__main__':
    v = 9
    edges = [[1, 2], [1, 5], [2, 3], [3, 7], [4, 6], [4, 7], [5, 6], [5, 7], [8, 9]]
    src = 1
    for a in DepthFirstSearch.depthFirstSearch(v, edges, src):
        print(a ,end = ' ')
            
            
        
        
                
