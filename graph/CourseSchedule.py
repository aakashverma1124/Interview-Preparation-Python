from collections import deque
class CourseSchedule:
    def build_graph(v, edges):
        graph = []
        indegree = dict()
        for i in range(v):
            graph.append(list())
            indegree[i] = 0
        for edge in edges:
            graph[edge[0]].append(edge[1])
            indegree[edge[1]] += 1
        return graph, indegree

    def can_be_done(v, edges):
        graph, indegree = CourseSchedule.build_graph(v, edges)
        queue = deque()
        
        for key, value in indegree.items():
            if value == 0:
                queue.append(key)
        
        sorted_order = []
        while queue:
            curr_node = queue.popleft()
            sorted_order.append(curr_node)

            for nbr in graph[curr_node]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    queue.append(nbr)
        
        return True if len(sorted_order) == v else False

if __name__ == '__main__':
    v = 7
    edges = [[5, 1], [5, 2], [6, 2], [6, 3], [1, 4], [2, 0], [3, 0]]
    print(CourseSchedule.can_be_done(v, edges))

        