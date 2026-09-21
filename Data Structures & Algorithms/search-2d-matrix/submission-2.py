class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) * len(matrix[0])
        n_len = len(matrix[0])

        if matrix[0][0] == target or matrix[len(matrix)-1][len(matrix[0])-1] == target:
            return True
        

        while low <= high:
            mid = (low + high) // 2
            m = (mid-1) // n_len 
            n = (mid-1) % n_len

            if matrix[m][n] == target:
                return True

            if matrix[m][n] < target:
                low = mid + 1
            else: 
                high = mid - 1
        return False
