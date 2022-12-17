from heapq import *

class FrequencySort:

	@staticmethod
	def sort_characters(s):
		
		hash_map = dict()
		for ch in s:
			hash_map[ch] = hash_map.get(ch, 0) + 1

		max_heap = list()
		for key, value in hash_map.items():
			heappush(max_heap, (-value, key))

		ans = []
		while max_heap:
			value, key = heappop(max_heap)
			freq = -value
			for i in range(freq):
				ans.append(key)

		return ''.join(ans)

if __name__ == '__main__':
	s = "apaprsqpp";
	ans = FrequencySort.sort_characters(s)
	print(ans)