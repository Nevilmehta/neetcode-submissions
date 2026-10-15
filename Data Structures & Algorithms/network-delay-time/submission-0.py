import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        # 1. build adjacency list
        for u,v,w in times:
            graph[u].append((v,w))

        # 2. initialize the min heap and distances
        min_heap = [(0,k)]
        dist = {}

        # 3. process nodes by smallest distance
        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in dist:
                continue

            dist[node] = time

            # 4. Explore neighbours
            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(min_heap, (time + weight, neighbor))

        if len(dist) != n:
            return -1

        # 5. return shortest distances
        return max(dist.values())