class Solution {
    static int smallestDivisor(int[] nums, int threshold) {
        int min = 1, max = Integer.MIN_VALUE, ans = -1;
        for(int i = 0; i < nums.length; i++) {
            max = Math.max(max, nums[i]);
        }

        int mid = 0;
        while (min <= max) {
            mid = min + (max-min)/2;
            int s= 0;

            for(int i =0; i < nums.length; i++) {
                if(nums[i] % mid == 0) {
                    s += ((double)nums[i]) /(double)(mid);
                }
                else s += nums[i]/mid + 1;
            }
            if(s <= threshold) {
                ans = mid;
                max = mid - 1;

            }
            else min = mid + 1;
        }
        return ans;
    }
}