class Solution:
    def largestGoodInteger(self, num: str) -> str:
        targets = [str(i * 111) for i in range(9, 0, -1)] + ["000"] # [999, 888, ..., 000]

        result = ""
        for target in targets:
            if target in num:
                result = target
                break;
        
        return result
