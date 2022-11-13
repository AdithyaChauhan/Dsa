class Solution {
    public int countNegatives(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;        
        int count = 0;
        for(int i = 0; i < n; i++) {
            int start = 0;
            int end = m - 1;
            int mid = 0;            
            while(start <= end) {
                mid = start + (end - start) /2;
                if(grid[i][mid] >= 0) {
                    start = mid + 1;
                }
                else if(grid[i][mid] < 0 && mid - 1 >= 0 && grid[i][mid - 1] < 0) {
                    end = mid -1;
                } else {
                    count += m - mid;
                    break;
                }
            }
        }
        return count;
    }
}