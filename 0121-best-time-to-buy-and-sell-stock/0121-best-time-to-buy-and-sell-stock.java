class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int profit = 0;
        int temp = prices[0];
        for(int i = 1; i < n; i++) {
            if(prices[i] < temp) {
                temp = prices[i];
            }
            else if(prices[i] - temp > profit) {
                profit = prices[i] - temp;
            }
        }
        return profit;
    }
}