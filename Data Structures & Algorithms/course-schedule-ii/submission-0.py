class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]

        # build graph
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        visiting = set()
        visited = set()
        result = []

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
            result.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return result