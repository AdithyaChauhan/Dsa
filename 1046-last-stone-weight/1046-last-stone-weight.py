class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort()
        print(stones)
        while len(stones) >1:
            stones[len(stones) - 2] = max(stones[len(stones) - 1], stones[len(stones) - 2]) - min(stones[len(stones) - 1], stones[len(stones) - 2])
            stones.pop(len(stones) - 1)
            stones.sort()

        return stones[0]