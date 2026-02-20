class Solution {
    public int singleNonDuplicate(int[] a) {
        int start = 0;
        int n = a.length;
        int end = n - 1;
        int mid = 0;
        while(start < end) {
            mid = (start + end)/2;
            if(mid % 2 == 0) {
                if(a[mid] == a[mid + 1]) start = mid + 2;
                else end = mid;
            }
            else {
                if(a[mid] == a[mid - 1]) start = mid + 1;
                else end = mid - 1;
            }
        }
        if (start == end) return a[start];
        else return -1;  
    }
}