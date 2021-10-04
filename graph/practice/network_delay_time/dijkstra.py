from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        elapsed = [float("inf")] * n
        heap = [(0, k)]
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u-1].append((v,w))

        while heap:
            time, node = heapq.heappop(heap)
            if time < elapsed[node-1]:
                elapsed[node-1] = time

                for v, w in graph[node-1]:
                    heapq.heappush(heap, (time + w, v))

        return max(elapsed) if max(elapsed) < float("inf") else - 1
