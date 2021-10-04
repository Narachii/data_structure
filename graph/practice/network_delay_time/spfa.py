from collections import defaultdict
from collections import deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """ SPFA """
        distance = [float("inf") for _ in range(n)]
        distance[k-1] = 0
        queue = deque([(0,k)])
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))
            
        while queue:
            time, node = queue.popleft()
            for v, w in graph[node]:
                if time + w < distance[v-1]:
                    distance[v-1] = time + w
                    queue.append((distance[v-1],v))
                    
        return max(distance) if max(distance) < float("inf") else -1
