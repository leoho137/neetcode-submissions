class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix) - 1
        m = 0
        while t <= b:
            m = int((t + b) // 2)
            if matrix[m][0] == target:
                return True
            if matrix[m][0] > target:
                b = m - 1
            else:
                if m < len(matrix) - 1 and matrix[m + 1][0] > target:
                    break
                else:
                    t = m + 1
        l, r = 0, len(matrix[0]) - 1
        c = 0
        while l <= r:
            mid = int((l + r) // 2)
            if matrix[m][mid] == target:
                return True
            if matrix[m][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
        
