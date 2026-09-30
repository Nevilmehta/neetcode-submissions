class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]

        # build graph
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        visiting = set()
        visited = set()

        def dfs(course):
            # cycle found
            if course in visiting:
                return False

            # already completely checked
            if course in visited:
                return True

            visiting.add(course)

            for prerequisite in graph[course]:
                if not dfs(prerequisite):
                    return False

            visiting.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True