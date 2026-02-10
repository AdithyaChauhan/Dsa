class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])

        col0 = 1

        # Step 1: mark
        for i in range(rows):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 2: zero inner matrix (reverse)
        for i in range(rows - 1, 0, -1):
            for j in range(cols - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 3: first row
        if matrix[0][0] == 0:
            for j in range(cols):
                matrix[0][j] = 0

        # Step 4: first column
        if col0 == 0:
            for i in range(rows):
                matrix[i][0] = 0
