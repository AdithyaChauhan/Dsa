class Solution {
    public int diagonalSum(int[][] matrix) {
        if(matrix[0].length == 1) {
            return matrix[0][0];
        }
        int sum = 0;
        int n = matrix[0].length;
        for(int i = 0; i < n; i++) {
            sum += matrix[i][i] + matrix[i][n - i - 1];
        } 
        
        if(n % 2 == 1) {
            int p = n - 1;
            sum = sum - matrix[p/2][p/2];
        }
        
        return sum;
    }
}