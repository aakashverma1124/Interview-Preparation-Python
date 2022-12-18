from heapq import *
from collections import deque

class ReorganizeStringKDistanceApart:

	@staticmethod
	def sort_characters(s, k):
		
		hash_map = dict()
		for ch in s:
			hash_map[ch] = hash_map.get(ch, 0) + 1

		max_heap = list()
		for key, value in hash_map.items():
			heappush(max_heap, (-value, key))

		queue = deque()
		result = []

		while max_heap:
			value, key = heappop(max_heap)
			freq = -value

			result.append(key)
			freq -= 1
			queue.append((freq, key))
			if(len(queue) == k):
				val, ch = queue.popleft()
				if val > 0:
					heappush(max_heap, (-val, ch))

		if len(result) == len(s):
			return ''.join(result)
		else:
			return ""

if __name__ == '__main__':
	s = "aabbcc"
	k = 3
	ans = ReorganizeStringKDistanceApart.sort_characters(s, k)
	print(ans)
