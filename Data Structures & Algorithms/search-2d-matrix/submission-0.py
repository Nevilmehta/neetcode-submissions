class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_matrix = [item for row in matrix for item in row]
        left, right = 0, len(flat_matrix)-1
        while left<=right:
            mid = (left + right)//2

            if flat_matrix[mid]==target:
                return True
            elif flat_matrix[mid]<target:
                left = mid + 1
            else:
                right = mid - 1

        return False
