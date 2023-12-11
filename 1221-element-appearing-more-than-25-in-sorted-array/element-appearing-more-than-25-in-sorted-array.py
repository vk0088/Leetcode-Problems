class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        total_len = len(arr)
        ans = {}
        set_ans = list(set(arr))
        for i in set_ans:
            ans[i] = (arr.count(i) / total_len) * 100
        ans = [k for k, v in ans.items() if max(ans.values()) == v]
        return ans[0]