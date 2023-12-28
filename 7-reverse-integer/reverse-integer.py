class Solution:
    def reverse(self, x: int) -> int:
        new = str(x)[::-1]
        if new[-1] == "-":
            new = - int(new[:-1])
        else:
            new = int(new)
        
        if (new < -2**31) or (new > 2**31 - 1):
            return 0
        else:
            return new