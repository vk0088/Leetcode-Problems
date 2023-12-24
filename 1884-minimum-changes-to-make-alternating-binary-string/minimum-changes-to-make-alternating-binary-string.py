import numpy as np
class Solution:
    def minOperations(self, s: str) -> int:
        # generate a pair of bool mask
        n = len(s)
        bool_1 = []
        count = 0
        while count < n:
            # if count is an even number
            if count % 2 == 0:
                bool_1.append(1)
                count += 1
            else:
            # if count is an odd number
                bool_1.append(0)
                count += 1
        s = np.array(list(s))
        s_bool = s.astype(bool)
        bool_1 = np.array(bool_1, dtype = bool)
        # bool_2 is the reverse of bool_1
        bool_2 = ~bool_1
        b1_s = n - (s_bool != bool_1).sum()
        b2_s = n - (s_bool != bool_2).sum()
        return min(b1_s, b2_s)