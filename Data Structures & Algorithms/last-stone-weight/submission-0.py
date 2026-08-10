import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap)>1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x!=y:
                heapq.heappush(heap, y-x)

        if heap:
            return -heap[0]

        return 0