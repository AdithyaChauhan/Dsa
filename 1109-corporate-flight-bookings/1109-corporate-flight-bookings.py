class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        op = [0] * n

        for l, r, seats in bookings:
            op[l - 1] += seats
            if r < n:
                op[r] -= seats

        for i in range(1, n):
            op[i] += op[i - 1]

        return op