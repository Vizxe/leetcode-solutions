# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/
from collections import defaultdict
from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        depth = -1
        visited = {1}
        queue = deque([1])

        while queue:
            depth += 1
            for _ in range(len(queue)): 
                node = queue.popleft()
                for nb in adj[node]:
                    if nb not in visited:
                        visited.add(nb)
                        queue.append(nb)
        odds = 1
        for i in range(2, depth + 1):
            odds = (2*odds) % (1e9 + 7)
        return int(odds)
