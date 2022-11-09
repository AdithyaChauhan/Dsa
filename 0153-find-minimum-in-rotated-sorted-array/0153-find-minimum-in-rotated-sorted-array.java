class Solution {
    public int findMin(int[] arr) {
        int s = 0;
        int e = arr.length - 1;
        int n = arr.length;        
        int mid = 0;
        
        if(n == 0) {
            return -1;
        }
        
        if(arr[s] < arr[e] || n == 1) {
            return arr[s];
        }
        while (s <= e) {
            mid = s + (e - s) / 2;
            if (mid < e && arr[mid] > arr[mid + 1]) {
                return arr[mid + 1];
            }
            if (mid > s && arr[mid] < arr[mid - 1]) {
                return arr[mid];
            }
            if (arr[mid] <= arr[s]) {
                e = mid - 1;
            } else {
                s = mid + 1;
            }
        }
        return - 1;
    }
}