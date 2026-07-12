class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        rowStart = 0
        rowEnd = len(matrix) - 1
        colStart = 0
        colEnd = len(matrix[0]) - 1

        while rowStart <= rowEnd:
            mid = rowStart + (rowEnd - rowStart) // 2

            if matrix[mid][0] == target:
                return True
                
            if matrix[mid][0] > target:
                rowEnd = mid - 1
            else:
                if matrix[mid][colEnd] >= target:
                    while colStart <= colEnd:
                        x = colStart + (colEnd - colStart) // 2

                        if matrix[mid][x] == target:
                            return True
                        if matrix[mid][x] > target:
                            colEnd = x - 1
                        else:
                            colStart = x + 1
                    return False
                rowStart = mid + 1
        
        return False
        
