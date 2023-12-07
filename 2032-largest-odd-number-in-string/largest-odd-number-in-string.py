class Solution:
    def largestOddNumber(self, num: str) -> str:
        for length in range(len(num)):
            if int(num[len(num)-1 - length:len(num) - length]) % 2 == 1:
                return num[ : len(num) - length ]
        return ""