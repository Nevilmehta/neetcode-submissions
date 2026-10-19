import heapq
from collections import defaultdict
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, price in flights:
            graph[u].append((v, price))

        min_heap = [(0, src, 0)]   #(cost, city, stops)
        best = {}

        while min_heap:
            cost, city, stops = heapq.heappop(min_heap)

            if city == dst:
                return cost

            if stops > k:
                continue

            if (city, stops) in best and best[(city, stops)] <= cost:
                continue

            best[(city, stops)] = cost

            for neighbor, price in graph[city]:
                heapq.heappush(
                    min_heap,
                    (cost + price, neighbor, stops + 1)
                )

        return -1