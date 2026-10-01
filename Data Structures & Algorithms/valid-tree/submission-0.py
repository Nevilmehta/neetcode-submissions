class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a tree must have n-1 edges
        if len(edges) != n-1:
            return False

        graph = [[] for _ in range(n)]

        # build graph
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(0)

        # every node must be connected
        return len(visited) == n
