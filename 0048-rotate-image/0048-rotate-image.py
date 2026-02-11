class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                if i != j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix[0]) // 2):
                matrix[i][j], matrix[i][n - j] = matrix[i][n - j], matrix[i][j]
