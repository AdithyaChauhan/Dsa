class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temp)
        for i in range(len(temp)):
            while stack and temp[i]> temp[stack[-1]]:
                x= stack.pop()
                ans[x] = i - x
            else:
                stack.append(i)
        
        return ans