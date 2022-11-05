class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k %  n;
        if( n == 1 && n == 0) {
            return;
        }
        
        for( int  i = 0,j = n - 1 - i; i <= j; i++, j--) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
        int p = 0, q = 0;
        for(int a = 0,b = k - 1; a <= b; a++, b--) {
            p = nums[a];
            nums[a] = nums[b];
            nums[b] = p;
        }
        
        for(int a = k,b = n - 1; a <= b; a++, b--) {
            p = nums[a];
            nums[a] = nums[b];
            nums[b] = p;
        }
    }
}