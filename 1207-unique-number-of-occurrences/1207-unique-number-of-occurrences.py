class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        x = {}
        y = set()
        for num in arr:

            x[num] = x.get(num, 0 ) + 1

        for val in x.values():

            if val in y:
                return False
            y.add(val)
        
        return True