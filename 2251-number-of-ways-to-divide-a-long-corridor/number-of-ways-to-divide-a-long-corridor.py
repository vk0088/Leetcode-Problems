class Solution:
    def numberOfWays(self, corridor: str) -> int:
        m = 10**9+7
        seat = corridor.count('S')
        if seat%2!=0 or seat<2: return 0
        if seat==2: return 1
        now = corridor.split('S')
        ans = 1
        print(now)
        for i in range(2,len(now)-1,2):
            ans *= (len(now[i])+1)
            ans %= m
        return ans