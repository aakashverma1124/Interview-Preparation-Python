from heapq import *

class MeetingRoomsII:

	def minimum_rooms(meetings):

		meetings.sort(key = lambda x : x[0])
		min_heap = []

		for meeting in meetings:
			if len(min_heap) > 0 and meeting[0] >= min_heap[0]:
				heappop(min_heap)
			heappush(min_heap, meeting[1])

		return len(min_heap)

if __name__ == '__main__':
	meetings = [[1, 4], [2, 3], [2, 3], [3, 5], [1, 4], [6, 8], [4, 7], [7, 9]]
	rooms = MeetingRoomsII.minimum_rooms(meetings)
	print(rooms)
