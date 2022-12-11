from heapq import * 
class KClosestPointsToOrigin:

	@staticmethod
	def kClosestPoints(points, k):
		max_heap = []
		for i in range(len(points)):
			x = points[i][0]
			y = points[i][1]
			distance = x * x + y * y
			heappush(max_heap, (-distance, x, y))
			if(len(max_heap) == k + 1):
				heappop(max_heap)

		ans = []
		while max_heap:
			d, x, y = heappop(max_heap)
			ans.append([x, y])

		return ans

if __name__ == '__main__':
	points = [[-4, 3], [-1, 1], [5, 5], [3, 1], [-4, -3], [2, -2]]
	k = 3
	ans = KClosestPointsToOrigin.kClosestPoints(points, k)
	for point in ans:
		print(point[0], end = " ")
		print(point[1])