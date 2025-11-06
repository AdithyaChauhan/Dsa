class Solution {
    public int nextGreaterElement(int n) {
      char[] arr = String.valueOf(n).toCharArray();
        
        // Finding the first index which should be swapped
        // Finding a number which is less than it's right value
        // For eg. n = 6537421, so our i will be 2 (arr[2] = 3)
        int i = arr.length - 2;
        while (i >= 0 && arr[i] >= arr[i + 1])
            i--;
        
        // Checking if we have the maximum permutation of our number
        // If we do then next smallest number does not exist
        if (i == -1)
            return -1;
        
        // Finding the second index which should be swapped
        // Finding a number just greater than arr[i]
        // For eg. n = 6537421, so our j will be 5 (arr[j] = 4)
        int j = arr.length - 1;
        while (arr[j] <= arr[i])
            j--;
        
        // Swapping the two indices
        // After swap n becomes 6547321, which is not the final answer. 
        // Though we make an observation that from i + 1 till the end of array is now in descending order 
        swap(arr, i, j);
        
        // So we reverse that part by sorting the array
        Arrays.sort(arr, i + 1, arr.length);
        
        long ans = Long.parseLong(new String(arr));
        
        // If ans which is long is out of range we return -1
        if (ans > Integer.MAX_VALUE)
            return -1;
        else
            return (int)ans;
    }
    
    public void swap(char[] arr, int i, int j) {
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}