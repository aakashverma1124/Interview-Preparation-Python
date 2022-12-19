import heapq

class TopFrequentElement:

    @staticmethod
    def topKFrequent(nums, k):

        hash_map = dict()
        for i in nums:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1

        max_heap = []
        heapq.heapify(max_heap)

        for key, value in hash_map.items():
            heapq.heappush(max_heap, (-value, key))

        res = list()
        while k:
            value, key = heapq.heappop(max_heap)
            res.append(key)
            k -= 1

        return res

if __name__ == '__main__':
	nums = [1,1,1,2,2,3]
	k = 2
	ans = TopFrequentElement.topKFrequent(nums, k)
	print(ans)
