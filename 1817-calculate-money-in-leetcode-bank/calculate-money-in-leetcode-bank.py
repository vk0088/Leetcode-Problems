class Solution:
    def totalMoney(self, n: int) -> int:
        return n//7*28 + ((n//7-1)*(n//7))*7//2 + (floor(n/7)*(n%7)) + (n%7)*(n%7+1)//2