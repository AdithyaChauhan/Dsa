class Solution:
    def isHappy(self, n: int) -> bool:

        x = n
        ans = 0
        seen = set()
        
        while ans not in seen:
            seen.add(ans)
            ans = 0

            while x > 0:

                ans += (x % 10)*(x%10)
                x = x // 10
            
            if ans == 1:
                return True
            x = ans
        
        return False