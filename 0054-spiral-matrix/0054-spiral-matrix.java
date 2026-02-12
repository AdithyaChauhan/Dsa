class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int frow = matrix.length - 1;
        int fcol = matrix[0].length - 1;
        int row = 0;
        int col = 0;
        int z = 0;
        int m = matrix.length;
        int n = matrix[0].length;
        int t = m*n;
        List<Integer> list = new ArrayList<>(t);
        while(z < t){
            //top
            
            for(int i = row,j = col; j <= fcol && z < t; j++){
                list.add(matrix[i][j]);
                z++;
            }
            row++;
            //right wall
            for(int i = row,j = fcol; i <= frow && z < t;i++){
                list.add(matrix[i][j]);
                z++;
            }
            fcol--;
            //bottom 
            for(int i =frow,j = fcol;j >= col && z < t; j--){
                list.add(matrix[i][j]);
                z++;
            }
            frow--;
        
            //left
            for(int i = frow,j = col; i >= row && z < t; i--){
                list.add(matrix[i][j]);
                z++;
            }
            col++;
        }
        return list;
    }
}