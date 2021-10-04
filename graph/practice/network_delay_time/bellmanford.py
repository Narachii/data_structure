class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance = [float("inf") for _ in range(n)]
        distance[k-1] = 0

        for _ in range(n-1):
            for u, v, w in times:
                if distance[u-1] + w < distance[v-1]:
                    distance[v-1] = distance[u-1] + w
        return max(distance) if max(distance) < float("inf") else -1
