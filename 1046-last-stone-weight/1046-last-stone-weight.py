class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        
        while len(stones) > 1:
            left = heapq.heappop(stones)
            right = heapq.heappop(stones)
            if left != right: 
                heapq.heappush(stones, (min(left,right) - max(left,right)))
        if len(stones) == 1:
            return -stones[0]
        if len(stones) == 0:
            return 0
            