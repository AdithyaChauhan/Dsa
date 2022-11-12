class Solution {
    public int searchInsert(int[] arr, int target) {
        int start = 0;
        int end = arr.length-1;
        while(start <= end)
        {
            //find middle element
            //int mid = 9start +end ) /2;//might be possible that (start + end) exceed the range of java
            int mid = start + (end-start)/2;
            if(target <arr[mid]) {
                end = mid - 1;
            }
            else if(target > arr[mid])
            {
                start = mid + 1;
            }
            else {
                return mid;
            }
        }
        return start;
    }
}