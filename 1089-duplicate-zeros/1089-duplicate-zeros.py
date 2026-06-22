class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        start = 0
        n = len(arr)
        while start < n - 1:
            if arr[start] == 0:
                k = n- 1
                while k > start + 1:
                    arr[k] = arr[k - 1]
                    k -= 1
                
                arr[start + 1] = 0
                
                start = start + 2
            
            else:
                start += 1

        return arr