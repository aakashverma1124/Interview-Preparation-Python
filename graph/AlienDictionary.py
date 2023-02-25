from collections import deque

class AlienDictionary:
    def build_graph(n, k, words):
        graph = dict()
        indegree = dict()
        for i in range(97, 97 + k):
            graph[chr(i)] = list()
            indegree[chr(i)] = 0
        for i in range(len(words) - 1):
            curr_word = words[i]
            next_word = words[i + 1]
            for j in range(min(len(curr_word), len(next_word))):
                if curr_word[j] != next_word[j]:
                    graph[curr_word[j]].append(next_word[j])
                    indegree[next_word[j]] += 1
                    break
        return graph, indegree

    def find_order(n, k, words):
        graph, indegree = AlienDictionary.build_graph(n, k, words)
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
        
        return ''.join(sorted_order) if len(sorted_order) == k else ""

if __name__ == '__main__':
    n = 5
    k = 4
    words = ["baa", "abcd", "abca", "cab", "cad"]
    print(AlienDictionary.find_order(n, k, words))

        