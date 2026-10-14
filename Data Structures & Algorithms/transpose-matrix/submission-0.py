class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])
        res = [[0] * r for _  in range(c)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[j][i]=matrix[i][j]
        return res
    