class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num) - 1
        ans = ""
        while n >= 0:
            if int(num[n]) %2 == 1:
                return num[:n+1]
            else:
                n -= 1
        return ""