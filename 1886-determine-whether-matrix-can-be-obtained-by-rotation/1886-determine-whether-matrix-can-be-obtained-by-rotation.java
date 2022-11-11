class Solution {
    public boolean findRotation(int[][] mat, int[][] target) {
        
        int n = mat.length;
        int[][] arr = new int[n][n];
        arr = mat;
        
        for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++)
                    System.out.println(arr[i][j]);
            }
        
        for (int count = 1; count <= 4; count++) {
            int[][] temp = new int[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++)
                    temp[j][n - 1 - i] = arr[i][j];
            }
            
            arr = temp;
            if (check(arr, target)) {
                return true;
            }
        }
        return false;
    }

    public boolean check(int[][] mat, int[][] target) {
        int n = mat.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] != target[i][j])
                    return false;
            }
        }
        return true;
    }
}