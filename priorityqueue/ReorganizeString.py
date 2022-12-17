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
		while len(max_heap) >= 2:
			value1, key1 = heappop(max_heap)
			freq1 = -value1
			value2, key2 = heappop(max_heap)
			freq2 = -value2

			ans.append(key1)
			ans.append(key2)

			freq1 -= 1
			freq2 -= 1

			if(freq1 > 0):
				heappush(max_heap, (-freq1, key1))

			if(freq2 > 0):
				heappush(max_heap, (-freq2, key2))

		if len(max_heap) == 0:
			return ''.join(ans)
		else:
			value, key = heappop(max_heap)
			freq = -value
			if freq == 1:
				ans.append(key)
				return ''.join(ans)
			else:
				return ""

	# you can use this function also
	@staticmethod
	def sort_characters2(s):
		
		hash_map = dict()
		for ch in s:
			hash_map[ch] = hash_map.get(ch, 0) + 1

		max_heap = list()
		for key, value in hash_map.items():
			heappush(max_heap, (-value, key))

		ans = []
		while len(max_heap) >= 2:
			value1, key1 = heappop(max_heap)
			value2, key2 = heappop(max_heap)

			ans.append(key1)
			ans.append(key2)

			if(value1 + 1 < 0):
				heappush(max_heap, (value1 + 1, key1))

			if(value2 + 1 < 0):
				heappush(max_heap, (value2 + 1, key2))

		if len(max_heap) == 0:
			return ''.join(ans)
		else:
			value, key = heappop(max_heap)
			if value == -1:
				ans.append(key)
				return ''.join(ans)
			else:
				return ""

if __name__ == '__main__':
	s = "aaabcdddaa";
	# both will give same answers
	ans = FrequencySort.sort_characters(s)
	ans2 = FrequencySort.sort_characters2(s)
	print(ans)
	print(ans2)