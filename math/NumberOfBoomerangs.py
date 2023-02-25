class Solution:

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        for i in range(len(points)):
            m = dict()
            for j in range(len(points)):
                if i != j:
                    dis = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                    m[dis] = m.get(dis, 0) + 1
            for key, value in m.items():
                if value >= 2:
                    count += (value * (value - 1))
        return count