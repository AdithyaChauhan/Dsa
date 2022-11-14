class Solution {
    public boolean searchMatrix(int[][] matrix, int target) 
    {
        if(matrix.length == 1) {
            
        }
        int rows = matrix.length;
        int cols = matrix[0].length;
        if (rows == 1) {
            return binarysearch(matrix, 0, 0, cols - 1, target);
        }
        int rStart = 0;
        int rEnd = rows - 1;
        int cMid = cols / 2;
        while (rStart < (rEnd - 1)) {
            int mid = rStart + (rEnd - rStart) / 2;
            if (matrix[mid][cMid] == target) {
                return true;
            }
            if (matrix[mid][cMid] < target) {
                rStart = mid;
            } else {
                rEnd = mid;
            }

        }
        if (matrix[rStart][cMid] == target) {
            return true;
        }
        if (matrix[rStart + 1][cMid] == target) {
            return true;
        }
        //search in 1st half
        if(cMid -1 >= 0 && target <= matrix[rStart][cMid - 1]){
            return binarysearch(matrix,rStart,0,cMid - 1,target);
        }
        //search in 2nd half
        if(cMid + 1 < matrix[0].length && target >= matrix[rStart][cMid + 1] && target <= matrix[rStart][cols - 1]){
            return binarysearch(matrix,rStart,cMid + 1,cols - 1,target);
        }
        //search in 3rd half
        if(cMid - 1 >= 0 && target <= matrix[rStart + 1][cMid - 1]){
            return binarysearch(matrix,rStart + 1,0,cMid - 1,target);
        }
        //search in 4th half
        else if(cMid + 1 < matrix[0].length) {
            return binarysearch(matrix,rStart + 1,cMid + 1,cols - 1,target);
        }
        else 
            return false;
    
    }
    
    static boolean binarysearch(int[][] matrix, int row, int cStart, int cEnd, int target) {
        while (cStart <= cEnd) {
            int mid = cStart + (cEnd - cStart) / 2;
            if (matrix[row][mid] == target){
                return true;
            }
            if (matrix[row][mid] < target){
                cStart = mid + 1;
            }
            else{
                cEnd = mid - 1;
            }
        }
        return false;
    }
}