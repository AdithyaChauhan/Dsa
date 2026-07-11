class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        
        dist = [0] * 1001
        
        for numPassengers, start, end in trips:
            dist[start] += numPassengers
            dist[end] -= numPassengers
        
        currPassengers = 0

        for passengers in dist:
            currPassengers += passengers
            if currPassengers > capacity:
                return False
        
        return True