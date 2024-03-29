class Solution {
    public int numDistinct(String s, String t) {
        int[][] dp = new int[t.length()+1][s.length()+1];
        Arrays.fill(dp[0], 1);
        for (int i = 1; i < t.length()+1; i++) {
            char c = t.charAt(i-1);
            for (int j = 1; j < s.length() + 1; j++) {
                if (c == s.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1];
                }
                else dp[i][j] = dp[i][j-1];
            }
        }
        //for (int[] row : dp) System.out.println(Arrays.toString(row));
        return dp[t.length()][s.length()];
    }
}