class Solution:
    def intToRoman(self, num: int) -> str:
        R = ['I', 'V', 'X', 'L', 'C', 'D', 'M', '(5K)', '(10K)']
        i1, i5, s = 0, 1, ''
        while num:
            r1, r5, r10 = R[i1], R[i5], R[i1 + 2]
            s = ['', r1, r1*2, r1*3, r1+r5, r5, r5+r1, r5+r1*2, r5+r1*3, r1+r10][num % 10] + s  # L->R
            num, i1, i5 = num // 10, i1 + 2, i5 + 2
        return s