class Solution {
    public int shipWithinDays(int[] weights, int D) {
        int left = 0, right = 0;
        for (int w = 0; w < weights.length; w++) {
            left = Math.max(left, weights[w]);
            right += weights[w];
        }
        while (left < right) {
            int mid = (left + right) / 2, need = 1, cur = 0;
            for (int w = 0; w < weights.length; w++) {
                if (cur + weights[w] > mid) {
                    need += 1;
                    cur = 0;
                }
                cur += weights[w];
            }
            if (need > D) left = mid + 1;
            else right = mid;
        }
        return left;
    }
}