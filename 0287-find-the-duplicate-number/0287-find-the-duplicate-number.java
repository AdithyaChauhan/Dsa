class Solution {
    public int findDuplicate(int[] nums) {
        int n = nums.length;
        int first = n;
        int second = n;
        do{
            first = nums[first-1];
            second = nums[nums[second-1]-1];
        }while(first != second);
        first = n;
        
        while(first != second){
            first= nums[first-1];
            second = nums[second-1];
        }
        
        return first;
    }
}