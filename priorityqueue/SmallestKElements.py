from heapq import *

class SmallestKElements:

	@staticmethod
	def smallestKElements(arr, k):
		max_heap = []
		
		for i in range(len(arr)):
			heappush(max_heap, -arr[i])
			if(len(max_heap) == k + 1):
				heappop(max_heap)
		
		ans = []
		
		while max_heap:
			ans.append(-heappop(max_heap))

		return ans

if __name__ == '__main__':
	arr = [1, 4, 5, 3, 7, 8, 6, 10]
	k = 3
	ans = SmallestKElements.smallestKElements(arr, k)
	for a in ans:
		print(a, end = " ")