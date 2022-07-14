class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i in range(len(points)):
            x, y =   points[i][0], points[i][1]
            minHeap.append([sqrt((0-x)**2 + (0-y)**2),x,y])
            
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x,y = heapq.heappop(minHeap)
            res.append([x,y])
            k -=1
            
        return res
        