class Solution {
    public void sortColors(int[] nums) {
        int m = 0, n = nums.length - 1, i = 0;
        while (i <= n) {
            if (nums[i] == 0) {
                nums[i] = nums[m];
                nums[m] = 0;
                m++;
            }
            if (nums[i] == 2) {
                nums[i] = nums[n];
                nums[n] = 2;
                n--;
                i--;
            }
            i++;
        }
    }
}