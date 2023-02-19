from heapq import *
import math

class DijkstraAlgorithm:

	def buildGraph(edges, nodes):

		graph = []
		for i in range(nodes + 1):
			graph.append(list())
		for edge in edges:
			graph[edge[0]].append((edge[1], edge[2]))
			graph[edge[1]].append((edge[0], edge[2]))
		return graph

	def shortestPath(edges, nodes, src):
		graph = DijkstraAlgorithm.buildGraph(edges, nodes)
		min_heap = []
		
		visited = [False] * (nodes + 1)
		distance = [math.inf] * (nodes + 1)

		distance[src] = 0
		heappush(min_heap, (distance[src], src))

		while min_heap:
			curr_distance, curr_node = heappop(min_heap)
			
			if visited[curr_node]: continue
			
			visited[curr_node] = True

			for nbr_pair in graph[curr_node]:
        
				if visited[nbr_pair[0]]: continue
				new_distance = curr_distance + nbr_pair[1]
				if new_distance < distance[nbr_pair[0]]:
					distance[nbr_pair[0]] = new_distance
					heappush(min_heap, (new_distance, nbr_pair[0]))
			
		return distance

if __name__ == '__main__':
    edges = [[1, 2, 6], [1, 3, 3], [1, 4, 15], [2, 4, 4], [2, 5, 5], [3, 5, 6]]
    v = 5
    src = 1
    ans = DijkstraAlgorithm.shortestPath(edges, v, src)
    print(ans[1:])