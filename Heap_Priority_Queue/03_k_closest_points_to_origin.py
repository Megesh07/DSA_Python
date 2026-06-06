import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        pts = []
        for x, y in points:
            dist = (abs(x) ** 2) + (abs(y) ** 2)
            pts.append([dist, x, y])
        res = []
        heapq.heapify(pts)
        for i in range(k):
            dist, x, y = heapq.heappop(pts)
            res.append([x, y])
        return res
