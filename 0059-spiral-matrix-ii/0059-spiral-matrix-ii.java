class Solution {
    public int[][] generateMatrix(int n) {
        int[][] spr = new int[n][n];

        int maxc = n-1;
        int maxr = n-1;
        int minc = 0;
        int minr = 0;
        int tne = n*n;
        int cnt = 1;
/*
1  2  3
4  5  6
7  8  9
 */
        while (cnt<=tne) {
            //top wall
            for (int i = minr,j=minc; j <= maxc&&cnt<=tne; j++) {
                spr[i][j] = cnt;
                cnt++;
            }
            minr++;
            //right wall

            for (int i = minr, j = maxc; i <= maxr&&cnt<=tne; i++) {
                spr[i][j] = cnt;
                cnt++;
            }
            maxc--;
            //bottom wall
            for (int i = maxr, j = maxc; j >= minc&&cnt<=tne;j--) {
                spr[i][j] = cnt;
                cnt++;
            }
            maxr--;
            //left wall
            for (int i = maxr, j = minc; i >= minr&&cnt<=tne; i--) {
                spr[i][j] = cnt;
                cnt++;
            }
            minc++;
        }
        return spr;
    }
}