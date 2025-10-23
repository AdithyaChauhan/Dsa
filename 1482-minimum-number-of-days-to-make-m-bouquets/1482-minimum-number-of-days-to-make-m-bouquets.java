class Solution {
    public int minDays(int[] nums, int m, int k) {
        int n = nums.length;
        if(m*k > n) return -1;
        int max = nums[0];
        int min = max;
        int ans = 0;
        for(int i = 0; i < n; i++) {
            if(nums[i] > max) max = nums[i];
            if(nums[i] < min) min = nums[i];
        }  
        int pairs = m, mid = -1;
        while(min <= max) {
            mid = min + (max - min)/2;
            if(count(nums, mid, m, k)) {
                max = mid - 1;
            } else min = mid + 1;

        }
            return min;

    }
    static boolean count(int[] nums, int day, int m , int k) {
        int n = nums.length;
        int ct = 0;
        int pairs = 0;

        for(int i = 0; i < n; i++) {
            if(nums[i] <= day) {
                ct++;
            }
            else {
                pairs += ct/k;
                ct = 0;
            }
        }
        pairs += ct/k;
        return (pairs >=m);
    }
}